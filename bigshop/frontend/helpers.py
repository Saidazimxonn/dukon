from .models import LiveMessage

def create_ad(post_request):
    name = post_request.get('name', '')
    full_name = post_request.get('f_name', '')
    phone = post_request.get('phone', '')
    message = post_request.get('message', '')
    message_long =post_request.get('message_long', '')
    LiveMessage.objects.create(
            name=name,
            full_name=full_name,
            phone=phone,
            message=message,
            message_long=message_long,
    )


