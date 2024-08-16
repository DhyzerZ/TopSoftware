from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages


def homePageView(request):
    return render(request, 'pages/home.html')

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 499.99},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 29.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 199.99},
    ]
    
class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {
            "title": "Products - Online Store",
            "subtitle": "List of Products",
            "products": Product.products,
        }
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            # Convertimos el id a un entero y verificamos si es válido
            product = Product.products[int(id)-1]
            viewData = {
                "title": f"{product['name']} - Online Store",
                "subtitle": f"{product['name']} - Product Information",
                "product": product,
            }
            return render(request, self.template_name, viewData)
        except (IndexError, ValueError):
            # Redirigir a la página de inicio si el id no es válido
            return HttpResponseRedirect(reverse('home'))

class ProductForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    price = forms.FloatField(required=True, min_value=0)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('The price must be greater than zero.')
        return price
    
class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create Product - Online Store",
            "form": form,
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Enviar un mensaje de éxito
            messages.success(request, 'Product created.')
            return redirect('index')  # Redirige al listado de productos
        else:
            viewData = {
                "title": "Create Product - Online Store",
                "form": form,
            }
            return render(request, self.template_name, viewData)

