from django import template
from products.models import Product, UserRating

# Tags for getting likes/dislikes on product IDs

register = template.Library()

# LIKED TAGS
@register.simple_tag
def get_liked(prod_id):
	try:
		product = Product.objects.get(id=prod_id)
	except Product.DoesNotExist:
		return None
	liked = UserRating.objects.filter(product=product, rating='liked')
	return str(len(liked))

# DISLIKED TAGS	
@register.simple_tag
def get_disliked(prod_id):
	try:
		product = Product.objects.get(id=prod_id)
	except Product.DoesNotExist:
		return None
	disliked = UserRating.objects.filter(product=product, rating='disliked')
	return str(len(disliked))