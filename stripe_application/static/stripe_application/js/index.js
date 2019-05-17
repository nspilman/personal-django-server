var stripe = Stripe('pk_live_L3DnVrjgBupynZtWEHe7XCnH00cP0TAQHZ');

var checkoutButton = document.getElementById('checkout-button-sku_F5JZ5IWWvd7xRr');
checkoutButton.addEventListener('click', function () {
  // When the customer clicks on the button, redirect
  // them to Checkout.
  stripe.redirectToCheckout({
    items: [{sku: 'sku_F4BvA7cLXZxsES', quantity: 1},
            {sku: 'sku_F5JZ5IWWvd7xRr', quantity: 1}],

    // Do not rely on the redirect to the successUrl for fulfilling
    // purchases, customers may not always reach the success_url after
    // a successful payment.
    // Instead use one of the strategies described in
    // https://stripe.com/docs/payments/checkout/fulfillment
    successUrl: 'https://natespilman.com',
    cancelUrl: 'https://natespilman.com/canceled',
  })
  .then(function (result) {
    if (result.error) {
      // If `redirectToCheckout` fails due to a browser or network
      // error, display the localized error message to your customer.
      var displayError = document.getElementById('error-message');
      displayError.textContent = result.error.message;
    }
  });
});