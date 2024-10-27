from django.urls import path
from products import views


urlpatterns = [
    
    path("", views.products , name="products"),
    path("product-review/<str:product_name>/", views.productreview , name="productreview"),
    path("payment/", views.payment , name="payment")
]
