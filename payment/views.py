import razorpay
from django.conf import settings
from django.shortcuts import render

def payment_page(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    
    # Create order
    payment = client.order.create({
        "amount": 50000,  # amount in paisa: ₹500
        "currency": "INR",
        "payment_capture": 1
    })

    context = {
        'payment': payment,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID
    }
    return render(request, 'payment/payment_page.html', context)