
from django.urls import path, include
from payu_payment.views import payu_checkout, payu_success, payu_failure, PayuView


urlpatterns = [
    path('payu', PayuView.as_view(), name='payu'),
    path('payu_checkout', payu_checkout, name="checkout"),
    path('payu/failure', payu_failure, name="payufailure"),
    path('payu/success', payu_success, name="payusuccess"),
]
