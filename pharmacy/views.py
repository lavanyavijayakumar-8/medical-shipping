from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, Prescription, Order
from django.db.models import Q
import pytesseract
from PIL import Image

def home_view(request):
    medicines = Medicine.objects.all()[:12] # Show featured medicines
    return render(request, 'home.html', {'medicines': medicines})

def search_view(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Medicine.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query))
    return render(request, 'search.html', {'results': results, 'query': query})

def upload_prescription_view(request):
    if request.method == 'POST' and request.FILES.get('prescription_image'):
        image_file = request.FILES['prescription_image']
        # Create prescription record
        prescription = Prescription(image=image_file)
        if request.user.is_authenticated:
            prescription.user = request.user
        prescription.save()

        # Try to parse text from image using pytesseract
        try:
            img = Image.open(prescription.image.path)
            # You need tesseract executable installed on the system for this to work
            # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            # Here we just try, if it fails due to missing tesseract, we skip it
            text = pytesseract.image_to_string(img)
            prescription.parsed_text = text
            prescription.save()
            
            # Simple keyword matching (very basic)
            words = text.split()
            matched_medicines = Medicine.objects.filter(name__in=words)
            if matched_medicines.exists():
                return render(request, 'search.html', {'results': matched_medicines, 'query': 'Prescription Match'})
        except Exception as e:
            print("OCR Failed:", e)
        
        # If no matches or OCR fails, redirect to search page with generic message
        return redirect('search')
        
    return render(request, 'upload.html')

def checkout_view(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.method == 'POST':
        address = request.POST.get('address')
        # Create order
        order = Order(total_price=medicine.price, shipping_address=address)
        if request.user.is_authenticated:
            order.user = request.user
        order.save()
        order.medicines.add(medicine)
        return render(request, 'checkout_success.html', {'order': order})

    return render(request, 'checkout.html', {'medicine': medicine})
