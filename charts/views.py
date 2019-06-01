import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from products.models import Product, UserProfile, UserRating
from checkout.models import OrderLineItem, Order
from django.db.models import Count, Sum
from django.db.models.functions import Lower


# Create your views here.

#Convert datetimes into str for JSON Dump
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super(LazyEncoder, self).default(obj)

def charts(request):
	
	#--------------------------------------------
	#CREATE Chart for number of category products
	#--------------------------------------------
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
				'borderRadius': 5,
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
	
	#-----------------------------------------
	#CREATE Chart for number of orders by date
	#-----------------------------------------
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
		 		'borderRadius': 5,
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

    #-----------------------
	#CREATE Chart by Ratings 
	#-----------------------
	dataset3 = \
	UserRating.objects.values('rating')\
	    		 .order_by('rating')\
	             .annotate(count=Count('rating'))
	
	# Create lists
	rating = list()
	count_series3 = list()
	# Append the values & formatting
	for entry in dataset3:
		rating.append(entry['rating'])
		count_series3.append(entry['count'])
		
	# Highcharts Configuration
	count_series3 = {'name': 'Ratings',
		            'data': count_series3
 	}
 
	chart4 = {
		'chart': {
			'type':'column', 
			'borderRadius': 20,
		    'borderWidth':2,
		    'marginTop':50,
		    'marginLeft':65,
		    'marginRight':10
		 },
		 'colors': ['#b22222', '#75bf00'],
		 'credits': {
		 	'position':{
		 	   'align':'left','x':50}
		 },     	  
		 'title': {
		 	'text':'Product Ratings'
		 },
	     'legend': {
	     	'enabled':'false'
	     },
	     'xAxis': {
		 	'categories':rating,
		 },
		 'yAxis': {
		 	'title': {
		 		'text':'Number of ratings'}
		 },
	 	 'series': [
	 	 	count_series3
	 	 ],
		 'plotOptions': {
		 	'series':{
		 		'borderRadius': 5,
		 		'colorByPoint':'true'
		 	},
		    'column':{
		    	'groupPadding':0,
		    	'pointPadding':0.1
		    }
		    
		 },
	}
	
	# Convert to JSON
	dump4 = json.dumps(chart4)
	
	#---------------------------- 
	#CREATE Chart by User Ratings
	#----------------------------
	dataset4 = \
	UserRating.objects.values('user_profile__user__username')\
	    		 .order_by(Lower('user_profile__user__username'))\
	             .annotate(count=Count('user_profile__user__username'))
	
	# Create lists
	rating = list()
	count_series4 = list()
	
	# Append the values & formatting
	for entry in dataset4:
		rating.append(entry['user_profile__user__username'])
		count_series4.append(entry['count'])
		
	# Highcharts Configuration
	count_series4 = {'name': 'Ratings',
		            'data': count_series4
 	}
 
	chart5 = {
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
		 	'text':'Product Ratings by User'
		 },
	     'legend': {
	     	'enabled':'false'
	     },
	     'xAxis': {
		 	'categories':rating,
		 },
		 'yAxis': {
		 	'title': {
		 		'text':'Number of ratings'}
		 },
	 	 'series': [
	 	 	count_series4
	 	 ],
		 'plotOptions': {
		 	'series':{
		 		'borderRadius': 5,
		 		'colorByPoint':'true'
		 	},
		    'column':{
		    	'groupPadding':0,
		    	'pointPadding':0.1
		    }
		    
		 },
	}
	
	# Convert to JSON
	dump5 = json.dumps(chart5)
	
	return render(request, 'charts.html', {'chart1': dump1, 'chart3': dump3, 'chart4': dump4, 'chart5': dump5})