from django.shortcuts import render , HttpResponse , get_object_or_404
from products.models import Product
# Create your views here.



def products(request):
    return render(request, 'demo.html')

def productreview(request , product_name):
    product = get_object_or_404(Product, product_name=product_name)
    
    # You can add any additional data you need for the product review here
    # For example, you can retrieve and pass reviews related to the product
    
    context = {
        'product': product,
        # Add other context data as needed
    }
    



  
        

    return render(request, 'product_review.html' , context)

def payment(request):
    return render(request , 'payment.html')