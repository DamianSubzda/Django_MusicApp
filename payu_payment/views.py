from django.shortcuts import render
from django.views import View
from paywix.payu import Payu
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group


from main.models import *

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

payu = Payu(merchant_key, merchant_salt, surl, furl, mode)


class Temp():
    x = None

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PayuView(View):
    user_id = None
    template_name = 'payu/payu.html'

    def get(self, request, *args, **kwargs):
        global temp_x
        temp_x = Temp()
        temp_x.setX(request.user.id)
        import uuid
        payload = {
            "amount": 100,
            "firstname": "renjith",
            "email": "renjithsraj@live.com",
            "phone": 9746272610,
            "lastname": "s raj",
            "productinfo": "Test Product",
            "address1": "Test address 1",
            "address2": "Test Address 2",
            "city": "Test city",
            "state": "Test state",
            "country": "Test country",
            "zipcode": 673576,
            "txnid": uuid.uuid1()
        }
        return render(request, self.template_name, {'posted': payload})

    def post(self, request, *args, **kwargs):
        data = {k: v[0] for k, v in dict(request.POST).items()}
        data.pop('csrfmiddlewaretoken')
        payu_data = payu.transaction(**data)
        return render(request, 'payu/checkout.html', {"posted": payu_data})


# Payu Checkout
@csrf_exempt
def payu_checkout(request):
    if request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        data.pop('csrfmiddlewaretoken')
        payu_data = payu.transaction(**data)
        return render(request, 'payu/checkout.html', {"posted": payu_data})
    return render(request, 'payu/payu.html', {'posted': ""})


# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return render(request, 'payu/payufailure.html')


# Payu success return page
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    user_id = temp_x.getX()
    user1 = User.objects.filter(id=user_id)
    my_group = Group.objects.get(name='premiumUser')
    my_group.user_set.add(user1[0])
    return render(request, 'payu/payusuccess.html')
