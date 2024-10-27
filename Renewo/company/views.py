from django.shortcuts import render , HttpResponse,redirect
from home.models import company

# Create your views here.
def companys(request):
    return render(request , 'company.html')

def companyinfo(request):
    
    if request.method == 'POST':
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
            

        com=company(companyname = fname,companylast=lname, companyphone=phone , companyaddress=address,pincode=pincode, city=city, state=state)
        com.save()
        return redirect('/companys')

    return render(request , 'company_info.html')