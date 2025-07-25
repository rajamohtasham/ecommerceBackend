from django.shortcuts import render



def home(request):
    return render(request, 'store/home.html')

def products(request):
    return render(request, 'store/products.html')

def product_detail(request, id):
    return render(request, 'store/product_detail.html', {'id': id})
