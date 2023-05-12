from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from my.services import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render


@method_decorator(login_required(), name="dispatch")
class MyOrdersView(TemplateView):
    #
    def get_template_names(self):
        return (
            "myadmin/orders.html"
            if self.request.user.groups.filter(id=2)
            else "my/orders.html"
        )

    # Rendering template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(orders_context(self.request.user))
        return context

    pass


# Представление для формы оформления заказа
@login_required
def confirm_view(request, id):
    if request.method == "POST":
        confirm_logic(request.POST["order"], request.POST["address"], request.user)
        return redirect("/")
    context = confirm_context(id, request.user)
    return render(request, "my/confirm.html", context)


# Представление для страницы заказа
@login_required
def order_view(request: object, id: int):
    context = order_context(request.user, id)
    return render(request, "my/order.html", context)


# Представление для страницы оформления заказа
@login_required
def make_order(request):
    context = {}
    profile, created = Profile.objects.get_or_create(user=request.user)
    default_address = profile.active_address.address
    # address = request.POST['address']
    if request.method == "POST":
        make_order_logic(request.user, request.POST["address"])
        return redirect("/my")
    return render(request, "my/make_order.html", context)
