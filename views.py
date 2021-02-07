from django.shortcuts import render
from django.http import HttpResponse
from .models import Allproduct
#HttpResponse is function to show message on web

def Home(request):
	product1='Home&Garden'
	product2='Furnitures'
	product3='Decoration'

	context = {'product1':product1,'product2':product2,'product3':product3}
	return render(request,'myapp/home.html',context) #folder which collect html


def About(request):
	return render(request, 'myapp/about.html')

def Contact(request):
	return render(request, 'myapp/contact.html')

def Garden(request):
	return render(request, 'myapp/garden.html')



def AddProduct(request):
	if request.method == 'POST':
		data = request.POST.copy()
		name = data.get('name')
		price = data.get('price')
		detail = data.get('detail')
		imageurl = data.get('imageurl')

		#Build database

		new = Allproduct()
		new.name = name
		new.price = price
		new.detail = detail
		new.imageurl = imageurl
		new.save()

	return render(request, 'myapp/addproduct.html')





def Product(request):
	product = Allproduct.objects.all() #import data from model (Allproduct)
	context = {'product':product} #get data into product
	return render(request, 'myapp/allproduct.html', context)

