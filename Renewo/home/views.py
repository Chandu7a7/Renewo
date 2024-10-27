from django.shortcuts import render , HttpResponse , redirect
from django.utils import timezone
from django.contrib.auth import login , authenticate
from django.contrib import messages
from django.contrib.auth.models import User 
import datetime
from seller.models import homeseller
from products.models import Cart
from products.models import *


def index(request):
    products = Product.objects.all()
    # products_to_display = products[:6]
    

    context={'products':products}   

 
    return render(request , 'index.html',context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        #pass2 = request.POST.get('pass2')

        user = User.objects.create(username=username , email=email )
        user.set_password(password)
        user.save()

        return redirect('/signin')
     

    return render(request, 'signup.html')


def signin(request):
     if request.method == 'POST':
         username = request.POST.get('uname')
         password = request.POST.get('pass1')

         if not User.objects.filter(username=username).exists():
             messages.error(request,"error user")
             return redirect('/signin')
         
         user = authenticate(username=username , password=password)
         if user is None:
             messages.error(request , 'error suer')
             return redirect('/signin')
         
         else:
             login(request , user)
             return redirect('/')

     return render(request , 'login.html')





def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)
    
def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity', 1))

        # Get the user's cart or create a new one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Check if the product is already in the cart, and update its quantity if so
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product_name=product_name)
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()

        return redirect('cart')

def search(request):
    # results=Product.objects.all()
    query = request.GET.get('aman')
    results = []

    if query:
        # Perform a search query on your Product model
        results = Product.objects.filter(product_name__icontains=query)
    context = {'results': results}
   
    return render(request , 'search.html', context)
