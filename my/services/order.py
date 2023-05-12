from django.shortcuts import get_object_or_404
from core.models import Jewelry
from my.models import Order
from my.models import Position
from my.models import Profile


"""
This function creates a context dictionary for a user's jewelry and orders. 

Input: user - object (represents a user in the system)
Output: context - dict (contains information about the user's jewelry and orders)"""


def user_index_context(user: object) -> dict:
    context = dict(
        jewelry=Jewelry.objects.filter(user=user, is_editable=True).values(
            "id", "name", "type__name", "material__name", "preview"
        ),
        orders=Position.objects.select_related(
            "jewelry", "order", "jewelry__type", "jewelry__material"
        )
        .filter(order__user=user)
        .values("id", "order__order_date", "jewelry__id", "jewelry__name"),
    )
    return context


"""
This function creates a context dictionary for a user's jewelry and orders. 
It takes in a user object and returns a dictionary containing information about the user's jewelry and orders. 

Input: user - object (represents a user in the system)
Output: context - dict (contains information about the user's jewelry and orders)
"""


def admin_index_context(user: object) -> dict:
    context = dict(
        jewelry=Jewelry.objects.filter(user=user).values(
            "id", "name", "type__name", "material__name", "preview"
        ),
        orders=Position.objects.all()
        .select_related("order", "jewelry", "jewelry__type", "jewelry__material")
        .values("id", "order__order_date", "jewelry__id", "jewelry__name"),
        admin=True,
    )
    return context


"""
This function creates a context dictionary for a user's orders. It takes in a user object and returns a dictionary containing information about the user's orders. 

Input: user - object (represents a user in the system)
Output: context - dict (contains information about the user's orders)

The context dictionary contains one key: 'orders'. 
The 'orders' key contains a queryset of Position objects filtered by the user, 
with all related fields selected using the select_related() method. 
Only specific fields 
('id', 'order__order_date', 'jewelry__id', 'jewelry__name', 'order__user', 'order__status') 
are selected using the values() method. 

If the user belongs to a group with id=2 (i.e. is a staff member), 
all Position objects are returned regardless of the order's user. 
Otherwise, only Position objects where the order's user matches the input user are returned.
"""


def orders_context(user: object) -> dict:
    context = {}
    if user.groups.filter(id=2):
        context["orders"] = (
            Position.objects.all()
            .select_related("order", "jewelry", "order__user")
            .values(
                "id",
                "order__order_date",
                "jewelry",
                "order__id",
                "jewelry__id",
                "order__user__name",
            )
        )
    else:
        context["orders"] = (
            Position.objects.all()
            .select_related("order", "jewelry", "order__user")
            .filter(order__user=user)
            .values(
                "id",
                "order__order_date",
                "jewelry__id",
                "jewelry__name",
                "order__user",
                "order__status",
                "order__id",
            )
        )
    return context


def user_order_context(user: object, id: int) -> dict:
    context = {}
    positions = Position.objects.select_related("order__user_id", "jewelry").get(pk=id)
    if positions.order__user_id != user.pk:
        return {}
    context["positions"] = positions
    return context


"""
his function retrieves the information of an order and creates a context dictionary to be used in the order detail view.

Input: 
- user: object - the user object
- id: int - the id of the order

Output:
- dictionary - a context dictionary containing the positions of the order, its status, the user's profile, 
and the total cost of the order. 
If the user is not authorized to view the order or the order does not exist, an empty dictionary is returned.
"""


def order_context(user: object, id: int):
    profile, created = Profile.objects.get_or_create(user=user)
    positions = list(
        Position.objects.select_related("order", "jewelry")
        .filter(order_id__exact=id)
        .values(
            "order__update_time",
            "order__order_date",
            "order__status",
            "price",
            "jewelry__name",
            "jewelry__id",
            "jewelry__material__name",
            "quantity",
            "jewelry__preview",
            "jewelry__cost",
            "jewelry__weight",
        )
    )
    total = 0
    for row in positions:
        total += row["jewelry__cost"]
    order = Order.objects.get(id=id)
    if not user.groups.filter(id=2) and user != positions[0].order.user:
        return {}
    return {
        "positions": positions,
        "status": order.status_representation,
        "profile": profile,
        "total": total,
    }


"""
This function confirms an order by updating its address and status.

Input:
- id: int - the primary key of the order to be confirmed
- address: str - the new address for the order
- user: object - the user who placed the order

Output:
- None 
"""


def confirm_logic(id: int, address: str, user: object):
    order = get_object_or_404(model=Order, pk=id, user=user)
    order.address = address
    order.status = 1
    order.save()
    return


# Функция, возвращающая контекст заказа
def confirm_context(id: int, user: object):
    order = get_object_or_404(model=Order, pk=id, user=user)
    return order
