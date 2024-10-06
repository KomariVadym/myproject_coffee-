from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Coffee
#from django.contrib import messages
#from .forms import UserRegisterForm
#import stripe
#from django.conf import settings
#from django.shortcuts import render, redirect
#from django.views import View
#from .models import Order
#from .forms import PaymentForm

def home(request):
    coffees = Coffee.objects.all()
    return render(request, 'home.html', {'coffees': coffees})

#Користувачі
"""def save_order(order):
    con = sqlite3.connect("orders.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO orders(name, coffee) VALUES(?, ?, ?, ?);",
        (order["name"], order[coffee"]),
    )
    con.commit()
    con.close()

def get_orders():
    con = sqlite3.connect("orders.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()
    con.close()
    return rows"""


#Платіжна система
"""def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})"""

"""class PaymentView(View):
    def get(self, request):
        form = PaymentForm()
        return render(request, 'payment.html', {'form': form, 'publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            stripe_token = form.cleaned_data['stripeToken']
            amount = 1000  # Amount in cents
            try:
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    description='Example charge',
                    source=stripe_token,
                )
                Order.objects.create(amount=amount, description='Example charge')
                return redirect('success')
            except stripe.error.CardError as e:
                return render(request, 'payment.html', {'form': form, 'error': str(e)})
        return render(request, 'payment.html', {'form': form})"""