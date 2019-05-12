import json
from django.shortcuts import render
from products.models import Product
from django.db.models import Count, Sum

# Create your views here.
def charts(request):
	
	#Count how many category objects per distinct category
	dataset = \
	Product.objects.values('category') \
    	   .order_by('category') \
		   .annotate(count=Count('category'))
	print(dataset)
	
	#Create lists
	categories = list()
	count_series = list()	
	
	#Append the values & formatting
	for entry in dataset:
		categories.append('%s Category' % entry['category'])
		count_series.append(entry['count'])
	print(categories)
	print(count_series)
        
	#return render(request, 'charts.html', {'dataset': dataset})
	
	return render(request, 'charts.html', {
        'categories': json.dumps(categories),
        'count_series': json.dumps(count_series)
	})