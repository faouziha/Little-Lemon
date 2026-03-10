from django.contrib import messages
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    menu_data = Menu.objects.all()[:3]
    return render(request, 'index.html', {"menu_data": menu_data})

def menu(request):
    # Fetch all items for the full menu page
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {"menu_data": menu_data})

def book(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        guests = request.POST.get('No_of_guests')
        date = request.POST.get('Booking_date')
        time = request.POST.get('Booking_time') # <-- Grab the new time field
        
        # DOUBLE BOOKING CHECK
        # .filter().exists() returns True if a row with this date & time is already in the DB
        if Booking.objects.filter(Booking_date=date, Booking_time=time).exists():
            # Send an error message instead of saving
            messages.error(request, f"Sorry! {time} on {date} is already booked. Please choose another time.")
        else:
            # If it's free, save it!
            Booking.objects.create(
                Name=name,
                No_of_guests=guests,
                Booking_date=date,
                Booking_time=time
            )
            messages.success(request, f"Awesome {name}! Your table for {guests} is confirmed for {date} at {time}.")
            
    return render(request, 'book.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
