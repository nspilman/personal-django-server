from django.shortcuts import render
import stripe

# Create your views here.

def donate(request,amount):
    stripe.api_key = 'sk_test_vv5GzNqNvLlRs5IfjoRKa7Pu00LYGSboP3'
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
    'name': 'Donation',
    'description': 'Donation to Arts on the Hudson',
    'images': ['https://example.com/t-shirt.png'],
    'amount': amount,
    'currency': 'usd',
    'quantity': 1,
  }],
  success_url='https://natespilman.com/',
  cancel_url='https://natespilman.com/cancel',
)
    return render(request,'stripe_application/complex.html',{'sessionId':session['id']})

def simple(request):
    return render(request,'stripe_application/simple.html')