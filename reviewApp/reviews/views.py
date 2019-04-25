from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import ContactForm

def home(request):
	return render(request, 'reviews/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'reviews/about.html', {'title': 'About Us'})

def contact(request):
	form = ContactForm()
	return render(request, 'reviews/contact.html', {'title': 'Contact Us', 'form':form})

class ProductListView(ListView):
	model = Product
	template_name = 'reviews/products.html'
	object_context_name = 'products'
	ordering = ['-name']

class ProductDetailView(DetailView):
	model = Product

# Create your views here.
