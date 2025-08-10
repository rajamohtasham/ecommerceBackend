from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Product
from .forms import CustomUserCreationForm, ProductForm
from django.contrib.auth import get_user_model, logout
from .models import CartItem, Order, OrderItem
from django.core.files.storage import FileSystemStorage


def home(request):
    products = Product.objects.all()[:4]
    return render(request, 'store/home.html', {'products': products})


def products(request):
    query = request.GET.get('q')
    product_list = Product.objects.all()

    if query:
        product_list = product_list.filter(
            name__icontains=query) | product_list.filter(category__icontains=query)

    paginator = Paginator(product_list, 8)  # Show 8 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'store/products.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})


def staff_check(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(staff_check)
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        stock = request.POST.get('stock')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Save product
        product = Product(
            name=name,
            price=price,
            category=category,
            stock=stock,
            description=description,
            image=image
        )
        product.save()

        messages.success(request, 'Product added successfully!')
        return redirect('add_product')

    return render(request, 'store/add_product.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🎉 Account created successfully! Please log in below.')
            return redirect('login')
        else:
            messages.error(request, '⚠️ Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'store/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity

    request.session['cart'] = cart
    messages.success(request, f"{product.name} added to cart.")
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        messages.success(request, 'Item removed from cart.')
    request.session['cart'] = cart
    return redirect('view_cart')


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[str(product_id)] = quantity
            messages.success(request, 'Cart updated.')
        else:
            cart.pop(str(product_id), None)
            messages.success(request, 'Item removed from cart.')

        request.session['cart'] = cart
    return redirect('view_cart')


@login_required(login_url='login')
def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })

    if request.method == 'POST':
        messages.success(request, '✅ Order placed successfully!')
        request.session['cart'] = {}  # clear cart
        return redirect('order_success')

    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def order_success(request):
    return render(request, 'store/order_success.html')
