from django.contrib import admin
from .models import Medicine, Prescription, Order

admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Order)
