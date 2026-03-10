from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Booking, Menu

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    # Field names must match models.py EXACTLY (Case Sensitive)
    list_display = ["Name", "No_of_guests", "Booking_date", "Booking_time"]
    
    fieldsets = (
        ("Reservation Details", {
            "fields": ["Name", "No_of_guests", "Booking_date", "Booking_time"],
        }),
    )

@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    list_display = ["Title", "Price", "Inventory"]
    
    fieldsets = (
        ("Item Information", {
            "fields": ["Title", "Price", "Inventory"],
        }),
    )