#
# File: api/models.py
#
from django.db import models
from django.contrib.auth.models import User

# Main model for every battery pack
class Pack(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IQC_PENDING', 'IQC Pending'),
        ('IN_STOCK', 'In Stock'),
        ('FA_PENDING', 'FA Pending'),
        ('FA_IN_PROGRESS', 'FA In Progress'),
        ('REPAIRED', 'Repaired'),
        ('EOL_TEST_PENDING', 'EOL Test Pending'),
        ('READY_TO_SHIP', 'Ready to Ship'),
        ('SHIPPED', 'Shipped'),
    ]

    serial_number = models.CharField(max_length=100, unique=True, primary_key=True)
    part_number = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True, related_name='packs')
    rma_number = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # For FIFO
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_number

# Model for warehouse locations
class Location(models.Model):
    ZONE_CHOICES = [
        ('NEW', 'New Packs Zone'),
        ('FA', 'Failure Analysis Zone'),
        ('REPAIRED', 'Repaired Packs Zone'),
        ('SHIPPING', 'Shipping Zone'),
    ]

    location_code = models.CharField(max_length=50, unique=True) # e.g., A-01-03-05
    zone = models.CharField(max_length=20, choices=ZONE_CHOICES)

    def __str__(self):
        return self.location_code

# Model for the Failure Analysis process
class FailureAnalysisReport(models.Model):
    pack = models.OneToOneField(Pack, on_delete=models.CASCADE)
    assigned_engineer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    issue_description = models.TextField()
    root_cause = models.TextField(null=True, blank=True)
    lv_log_file = models.FileField(upload_to='logs/lv/', null=True, blank=True)
    parsed_log_data = models.JSONField(null=True, blank=True) # Store parsed JSON data
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    eol_test_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"Report for {self.pack.serial_number}"

# Model for Audit Trail
class PackHistory(models.Model):
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name='history')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255) # e.g., "Status changed from NEW to FA_PENDING"
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(null=True, blank=True) # For extra context

    class Meta:
        ordering = ['-timestamp'] # Show newest history first

    def __str__(self):
        return f"{self.pack.serial_number} - {self.action} at {self.timestamp}"