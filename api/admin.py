#
# File: api/admin.py
#
from django.contrib import admin
from .models import Pack, Location, FailureAnalysisReport, PackHistory

# The admin.site.register() function is how you make a model
# appear on the admin site.

admin.site.register(Pack)
admin.site.register(Location)
admin.site.register(FailureAnalysisReport)
admin.site.register(PackHistory)