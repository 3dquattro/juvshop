from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from my.services import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from my.forms import RegisterForm, AddressForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView


# cbv for index-page in personal acc.
@method_decorator(login_required(), name="dispatch")
class MyIndexView(TemplateView):
    # Separating view for different groups
    def get_template_names(self):
        return (
            "myadmin/index.html"
            if self.request.user.groups.filter(id=2)
            else "myadmin/index.html"
        )

    # Rendering template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.groups.filter(id=2):
            context.update(admin_index_context(self.request.user))
        else:
            context.update(user_index_context(self.request.user))
        return context

    pass


# Login form
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        print(email)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.META["HTTP_REFERER"])
        else:
            return HttpResponseNotFound("Вы уже авторизованы")
    else:
        return render(request, "registration/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect(request.META["HTTP_REFERER"])


def signup_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("/")
    form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


# View for password change
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "my/registration/change_password.html"
    success_url = "/my"


# Class is made to optimize import in urls.py and structurize code
class ProfileViews:
    # index view-method for Profile
    @login_required
    def index_view(request):
        if request.method == "POST":
            profile_index_post_logic(request.user, request.POST)
        context = profile_index_get_context(request.user)
        return render(request, "my/profile/index.html", context)

    @login_required
    def addresses_index(request):
        context = addresses_index_context(request.user)
        return render(request, "my/profile/addresses/index.html", context)

    class AddressEdit(LoginRequiredMixin, UpdateView):
        template_name = "my/profile/addresses/edit.html"
        form_class = AddressForm
        success_url = "/my/profile/addresses"
        model = Address

        def dispatch(self, request, *args, **kwargs):
            address = self.get_object()
            profile = Profile.objects.get(user=request.user)
            if profile != address.profile:
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)

    class AddressDelete(LoginRequiredMixin, DeleteView):
        template_name = "my/profile/addresses/delete.html"
        success_url = "/my/profile/addresses"
        model = Address

        def dispatch(self, request, *args, **kwargs):
            address = self.get_object()
            profile = Profile.objects.get(user=request.user)
            if profile != address.profile:
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)

    class AddressCreate(LoginRequiredMixin, CreateView):
        template_name = "my/profile/addresses/create.html"
        success_url = "/my/profile/addresses"
        model = Address
        form_class = AddressForm

        def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs["request"] = self.request
            return kwargs
