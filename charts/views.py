import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from products.models import Product
from checkout.models import OrderLineItem, Order
from django.db.models import Count, Sum

# Create your views here.

#Convert datetimes into str for JSON Dump
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super(LazyEncoder, self).default(obj)

def charts(request):
	
	#CREATE Chart for number of category products
	#Count how many category objects per distinct category
	dataset = \
	Product.objects.values('category')\
	       .order_by('category')\
	       .annotate(count=Count('category'))
	
	# Create lists
	categories = list()
	count_series = list()
	# Append the values & formatting
	for entry in dataset:
		categories.append(entry['category'])
		count_series.append(entry['count'])
		
	# Highcharts Configuration
	count_series = {
		'name': 'Products',
		'data': count_series
 	}
	
	chart1 = {
		'chart': {
			'type':'column', 
			'borderRadius': 20,
		    'borderWidth':2,
		    'marginTop':50,
		    'marginLeft':65,
		    'marginRight':10
		},
		'credits': {
			'position':{
			   'align':'left','x':50}
		},     	  
		'title': {
			'text':'Products by Categories'
		},
	    'legend': {
	    	'enabled':'false'
	    },
		'yAxis': {
			'title': {
				'text':'Number of Parts'}
		},
		'xAxis': {
			'categories':categories
		},
	 	'series': [
	 		count_series
	 	],
		'plotOptions': {
			'series':{
				'colorByPoint':'true'
			},
		    'column':{
		    	'groupPadding':0,
		    	'pointPadding':0.1
		    }
		},
	}
	
	# Convert to JSON
	dump1 = json.dumps(chart1)
	
	
	#CREATE Chart for number of products sold
	dataset1 = \
	OrderLineItem.objects.values('quantity')\
	    		 .order_by('quantity')\
	             .annotate(count=Count('quantity'))
	
	# Create lists
	count_series1 = list()
	
	# Append the values & formatting
	for entry in dataset1:
		count_series1.append(entry['count'])
	
	# Highcharts Configuration	
	count_series1 = {
		'name':'Products Sold',
	    'data':count_series1
	}
	
	chart2 = {
		'chart': {
			'type':'gauge',
			'borderRadius': 20,
		    'borderWidth':2,
		},
		'series': [count_series1],
        'title': {
        	'text':'Products Sold'
        },
        'pane': {
        	'startAngle':-90,
            'endAngle':90,
            'backgroundColor':'#DDD',
        },
        'yAxis': {
        	'min':0,
        	'max':100,
        	'minorTickInterval':5,
        	'minorTickWidth':1,
        	'minorTickLength':10,
        	'minorTickPosition':'inside',
        	'minorTickColor':'#55BF3B',
        	'tickPixelInterval':60,
        	'tickWidth':2,
        	'tickPosition':'inside',
        	'tickLength':'inside',
        	'tickColor':'#666'
        },
        'credits': {
        	'position': {
        		'align':'left','x':50
        	 }
        },  
    }
        
	# Convert to JSON
	dump2 = json.dumps(chart2)
	
	
	#CREATE Chart for number of orders by date
	#Count how many date objects per distinct date
	dataset2 = \
	Order.objects.values('date')\
	    		 .order_by('date')\
	             .annotate(count=Count('date'))
	
	# Create lists
	dates = list()
	count_series2 = list()
	# Append the values & formatting
	for entry in dataset2:
		dates.append(entry['date'])
		count_series2.append(entry['count'])
	
		# Highcharts Configuration
	count_series2 = {'name': 'Orders',
		            'data': count_series2
 	}
	
	chart3 = {
		'chart': {
			'type':'column', 
			'borderRadius': 20,
		    'borderWidth':2,
		    'marginTop':50,
		    'marginLeft':65,
		    'marginRight':10
		 },
		 'credits': {
		 	'position':{
		 	   'align':'left','x':50}
		 },     	  
		 'title': {
		 	'text':'Orders by Date'
		 },
	     'legend': {
	     	'enabled':'false'
	     },
		 'yAxis': {
		 	'title': {
		 		'text':'Number of Orders'}
		 },
		 'xAxis': {
		 	'categories':dates
		 }, 
	 	 'series': [
	 	 	count_series2
	 	 ],
		 'plotOptions': {
		 	'series':{
		 		'colorByPoint':'true'
		 	},
		    'column':{
		    	'groupPadding':0,
		    	'pointPadding':0.1
		    }
		 },
	}
	
	# Convert to JSON
	dump3 = json.dumps(chart3, cls=LazyEncoder)

	return render(request, 'charts.html', {'chart1': dump1, 'chart2': dump2, 'chart3': dump3})