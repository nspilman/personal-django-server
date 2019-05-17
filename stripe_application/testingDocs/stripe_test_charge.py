import stripe

stripe.api_key = 'sk_test_vv5GzNqNvLlRs5IfjoRKa7Pu00LYGSboP3'

charge = stripe.Charge.create(
  amount=999,
  currency='usd',
  source='tok_visa',
  receipt_email='jenny.rosen@example.com',
)

print(charge)