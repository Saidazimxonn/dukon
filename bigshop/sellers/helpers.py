from .models import Order

def order_create(post_request):
    name = post_request.get('name', '')
    phone = post_request.get('phone', '')
    province = post_request.get('province', '')
    count_product = post_request.get('count_product', '')
    product_name = post_request.get('product_name', '')
    price = post_request.get('price', '')

    Order.objects.create(
        name=name,
        phone=phone,
        province=province,
        count_product=count_product,
        product_name=product_name,
        price=price,
    )