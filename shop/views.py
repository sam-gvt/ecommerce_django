from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator

def index(request):
    product_objects = Products.objects.all()

    # search item
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # Paginator code
    paginator = Paginator(product_objects, 3)
    page = request.GET.get('page')
    if page is None:
        page = 1
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects, 'page_number': page})

def detail(request, id):
    product_object = Products.objects.get(id = id)
    return render(request, 'shop/detail.html', {'product_object' : product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get("items", "")

        email = request.POST.get("email","")
        first_name = request.POST.get("first_name","")
        last_name = request.POST.get("last_name","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zip_code = request.POST.get("zip","")
        phone_number = request.POST.get("phone","")

        order = Order(
            items=items,
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone_number=phone_number,
        )
        order.save()


    return render(request, 'shop/checkout.html')