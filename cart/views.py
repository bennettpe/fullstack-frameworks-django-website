# CART Views
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# VIEW cart
@login_required
def view_cart(request):
    """
    A View that renders the cart contents page
    """
    return render(request, "cart.html")

# ADD to cart
@login_required
def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


#ADJUSTMENT to cart
@login_required
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
#REMOVE from cart
@login_required
def remove_from_cart(request, id):
    """ 
    Remove item from cart 
    """
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect('view_cart')