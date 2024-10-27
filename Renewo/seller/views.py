from django.shortcuts import render , HttpResponse,redirect
from seller.models import homeseller

# Create your views here.

def seller(request):
    
    return render(request , 'seller.html')

def sellerinfo(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
            

        sell=homeseller(first_name = fname,last_name=lname, phone=phone , address=address,pincode=pincode, city=city, state=state)
        sell.save()
        return redirect('/seller')
    return render(request , 'seller_info.html')