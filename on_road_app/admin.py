from django.contrib import admin
from .models import Customer,Mechanic,Bookings,Fire,SOS,Feedback

# Register your models here.
admin.site.register(Customer)
admin.site.register(Mechanic)
admin.site.register(Bookings)
admin.site.register(Fire)
admin.site.register(SOS)
admin.site.register(Feedback)
