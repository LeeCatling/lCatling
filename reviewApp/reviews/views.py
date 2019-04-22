from django.shortcuts import render

def home(request):
	return render(request, 'reviews/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'reviews/about.html', {'title': 'About Us'})

def contact(request):
	return render(request, 'reviews/contact.html', {'title': 'Contact Us'})

def product(request):
	return render(request, 'reviews/product.html', {'title': 'Product'})

# Create your views here.
