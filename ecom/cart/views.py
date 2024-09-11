from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages




def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Check if the action is 'post'
    if request.POST.get('action') == 'post':
        # Get product_id from POST data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Lookup product in DB using the Product model
        product = get_object_or_404(Product, id=product_id)

        # Add product to cart
        cart.add(product=product, quantity=product_qty)

        # Get the quantity of items in the cart
        cart_quantity = cart.__len__()

        # Return a JSON response with the cart quantity
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product added to Cart"))
        return response



def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get Things
        product_id = int(request.POST.get('product_id'))
        # Call delete Function
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request, ("Item Deleted From Cart"))
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get product_id from POST data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("Your Cart Has Been Updated"))
        return response