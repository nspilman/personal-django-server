const stripe = Stripe('pk_test_I5zH7Kv2DKFo1gT40IHtu4xj009znB7e9j');

stripe.redirectToCheckout({
  sessionId: sessionId,
}).then((result) => {
  // If `redirectToCheckout` fails due to a browser or network
  // error, display the localized error message to your customer
  // using `result.error.message`.
});
