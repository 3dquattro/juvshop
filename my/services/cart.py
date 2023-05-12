from core.models import Jewelry
from my.models import Order
from my.models import Position
from my.models import Cart
from datetime import datetime
from django.shortcuts import get_object_or_404


"""
Adds a jewelry item to a user's cart with the specified quantity.

Input:
- user: object - the user object for whom the item is being added to the cart
- itemid: int - the id of the jewelry item being added to the cart
- quantity: int - the quantity of the jewelry item being added to the cart

Output: None
"""


def service_add_to_cart(user: object, itemid: int, quantity: int):
    cart, created = Cart.objects.get_or_create(user_id=user.id)
    position, created = Position.objects.get_or_create(cart=cart)
    position.jewelry = Jewelry.objects.get(pk=itemid)
    position.cart = cart
    position.quantity += int(quantity)
    position.price += position.jewelry.cost * float(quantity)
    position.save()
    return


"""
This function retrieves the cart context for a given user, including the items in the cart, their details, and the total cost of the cart.

Input: user - object representing the user for which to retrieve the cart context.

Output: A dictionary containing the following keys:
- 'cart': The Cart object associated with the given user.
- 'positions': A QuerySet of Position objects representing the items in the cart, with related Jewelry, Material, and Type objects pre-loaded.
- 'total': The total cost of all items in the cart.
"""


def cart_context(user: object):
    cart, created = Cart.objects.get_or_create(user=user)
    positions = (
        Position.objects.filter(cart=cart)
        .select_related("jewelry", "jewelry__material", "jewelry__type")
        .values(
            "jewelry__name",
            "jewelry__type__name",
            "jewelry__material__name",
            "jewelry__preview",
            "jewelry__weight",
            "jewelry__cost",
            "jewelry__id",
            "price",
            "quantity",
        )
    )
    cost = 0
    for element in positions:
        cost += element["jewelry__cost"]
    return {"cart": cart, "positions": positions, "total": cost}


"""
This function makes an order for a given user, transferring the items in their cart to a new order 
and updating the jewelry items to be uneditable and private.

Input: user - object representing the user for whom the order is being made
Output: None
"""


def make_order_logic(user: object):
    cart = Cart.objects.get(user=user)
    positions = Position.objects.filter(cart=cart)
    order = Order.objects.create(user=user, status=0, order_date=datetime.now())
    for element in positions:
        element.cart = None
        element.order = order
        element.save()
        copy = element.jewelry.copy()
        copy.is_editable = False
        copy.ispublic = False
        copy.save()
        element.jewelry = copy
        element.save()
    return


def get_object_for_confirm(user: object, order: int):
    return get_object_or_404(model=Order, pk=order, user=user)
