from my.models import Order
from my.models import Message
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.db.models import Q


# Контекст для списка диалогов
# def dialogues_list_context(user: object):
#
#     if not user.groups.filter(id=2):
#         messages_list = Message.objects.filter(order__user=user)\
#             .select_related('order', 'order__user')\
#             .values('order__id').distinct()
#         return {'dialogues': messages_list}
#
#     messages_list = Message.objects.all()\
#         .select_related('order')\
#         .values('order__id').distinct()
#     return {'dialogues': messages_list}
"""Returns a dictionary containing the list of dialogue IDs associated with the user.

Input: user - object
Output: {'dialogues': list of dialogue IDs}
"""


def dialogues_list_context(user: object):
    q = Q()
    q |= Q(order__user=user)
    if user.groups.filter(id=2).exists():
        messages_list = (
            Message.objects.filter(q)
            .select_related("order")
            .values("order__id")
            .distinct()
        )
    else:
        messages_list = (
            Message.objects.select_related("order").values("order__id").distinct()
        )

    return {"dialogues": messages_list}


"""
Gets the order associated with the given user and dialogue
Input: user - object, dialogue - int
Output: order - object or None
"""


def get_order(user: object, dialogue: int):
    order = get_object_or_404(Order, pk=dialogue)
    if not (user.groups.filter(id=2) or order.user == user):
        raise PermissionDenied("Не совпадает пользователь/не администратор")
        return None
    return order


"""
Creates a new message object and saves it to the database
Input: user - object, dialogue - int, text - str
Output: None
"""


def send_message(user: object, dialogue: int, text: str):
    order = get_order(user, dialogue)
    if not order:
        return
    message = Message.objects.create(
        order=order, content=text, sender=user, send_date=datetime.now()
    )
    return


# def send_message(user: object, dialogue: int, text: str):
#     order = get_order(user, dialogue)
#     if order is None:
#         return
#     #Создаем объект сообщения
#     message = Message()
#     message.order = order
#     message.content = text
#     message.sender = user
#     message.send_date = datetime.now()
#     message.save()
#     return


"""
Returns a dictionary containing the messages, order and dialogue associated with a given dialogue ID and user.

Input: 
- dialogue - int: ID of the dialogue
- user - object: user object

Output: 
- 'messages': list of dictionaries containing message information
- 'order': order object associated with the dialogue
- 'dialogue': dialogue ID
"""


def get_messages(dialogue: int, user: object):
    order = get_order(user, dialogue)
    if order is None:
        return
    messages = (
        Message.objects.select_related("order", "sender")
        .filter(order_id__exact=dialogue)
        .values("send_date", "sender__name", "content", "sender")
    )
    return {"messages": messages, "order": order, "dialogue": dialogue}
