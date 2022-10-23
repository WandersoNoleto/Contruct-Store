import sys
from datetime import date
from io import BytesIO

from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from PIL import Image as Image_pil
from PIL import ImageDraw
from rolepermissions.decorators import has_permission_decorator

from inventory.forms import ProductForm
from inventory.models import Category, Image, Product


@has_permission_decorator('cadastrar_produtos')
def add_product(request):
    if request.method == "GET":
        categories = Category.objects.all()
        products = Product.objects.all()

        context = {
            'categories': categories,
            'products': products,
        }

        return render(request, 'add_product.html', context)

    elif request.method == "POST":
        name     = request.POST.get('name')
        category = request.POST.get('category')
        amount   = request.POST.get('amount')
        price_buy  = request.POST.get('price_buy')
        price_sell = request.POST.get('price_sell')

        product = Product(
            name = name, 
            category_id = category, 
            amount      = amount, 
            price_buy   = price_buy, 
            price_sell  = price_sell
            )

        product.save()

        for file in request.FILES.getlist('images'):
            name = f'{date.today()}-{product.id}.jpg'

            img = Image_pil.open(file)
            img = img.convert('RGB')
            img = img.resize((300,300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), "CONSTRUCT {date.today()}", (255, 255, 255))
            output = BytesIO()
            
            img.save(output, format="JPEG", quality=100)
            output.seek(0)

            final_img = InMemoryUploadedFile(
                output, 'ImageField', name, 'image/jpeg', sys.getsizeof(output), None
            )

            img_save_dj = Image(image = final_img, product=product)
            img_save_dj.save()

        messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso')
        return redirect(reverse("add_product"))

def show_product(request, slug):
    if request.method == "GET":
        product = Product.objects.get(slug=slug)
        data = product.__dict__
        data['category'] = product.category.id
        form = ProductForm(initial=data)

        context = {
            'form': form
        }

        return render(request, 'product.html', context)
