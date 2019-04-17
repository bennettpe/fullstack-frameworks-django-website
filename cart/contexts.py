# Using sessions to keep track of contents of shopping cart
# The cart items will be stored in the session when the user is logged in (they will not be added into the database). 
# However, as soon as the user logs out the cart will be lost.

from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    
    # For loop
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}