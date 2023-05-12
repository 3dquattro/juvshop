from django.shortcuts import redirect
from my.services import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def cart_view(request):
    context = cart_context(request.user)
    return render(request, "my/cart.html", context)


@login_required
def add_to_cart(request):
    service_add_to_cart(request.user, request.POST["item"], request.POST["quantity"])
    return redirect(request.META["HTTP_REFERER"])
