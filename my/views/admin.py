from core.models import Part, ProductType, PartType, Material, Jewelry
from core.forms import (
    PartForm,
    ProductTypeForm,
    PartTypeForm,
    MaterialForm,
    JewelryForm,
)
from my.tables import (
    ProductTypeTable,
    PartTypeTable,
    PartTable,
    MaterialTable,
    JewelryTable,
)
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


# region BaseClasses


class IsAdminMixin(UserPassesTestMixin):
    """
    Mixin is used for access regulation to admin part of 'my' app.
    """

    def test_func(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(id=2).exists():
            return True
        else:
            raise PermissionDenied


class AdminIndexView(IsAdminMixin, TemplateView):
    """
    Provides a way to show admin index view for some model,
    which required user to be admin
    and shows table with all objects of model
    """

    table_class = None
    model_class = None
    template_name = "myadmin/common/index.html"
    title = None
    suffix = None
    """
    Implementation of UserPassesTestMixin function.
    Required for making view accessable only for admin users
    """

    def get_context_data(self, *args, **kwargs):
        context = super(AdminIndexView, self).get_context_data(*args, **kwargs)
        context["title"] = self.title
        if self.suffix:
            context["suffix"] = self.suffix
        context["table"] = self.table_class(self.model_class.objects.all())
        return context

    pass


class AdminCreateView(IsAdminMixin, CreateView):
    """
    Provides a way to show and handle creation form for model object
    """

    form_class = None
    template_name = "myadmin/common/create.html"
    title = None
    success_url = "/my"
    """
    Implementation of UserPassesTestMixin function.
    Required for making view accessable only for admin users
    """

    def get_context_data(self, *args, **kwargs):
        context = super(AdminCreateView, self).get_context_data(*args, **kwargs)
        context["title"] = self.title
        return context


class AdminUpdateView(IsAdminMixin, UpdateView):
    """
    Basic class for all update views in my/admin.
    Extends standard UpdateView
    """

    form_class = None
    model = None
    template_name = "myadmin/common/update.html"
    success_url = "/my"
    title = None

    def get_context_data(self, *args, **kwargs):
        context = super(AdminUpdateView, self).get_context_data(*args, **kwargs)
        context["title"] = self.title
        return context


class AdminDeleteView(IsAdminMixin, DeleteView):
    """
    Basic class for all update views in my/admin.
    Extends standard DeleteView, uses default confirmation mechanism.
    """

    template_name = "myadmin/common/delete.html"
    success_url = "/my"
    model = None
    title = None

    def get_context_data(self, *args, **kwargs):
        context = super(AdminDeleteView, self).get_context_data(*args, **kwargs)
        context["title"] = self.title
        return context


# endregion


# region Product type views
class ProductTypeMixin:
    table_class = ProductTypeTable
    model_class = model = ProductType
    index_title = update_title = create_title = "Типы изделий"
    form_class = ProductTypeForm
    suffix = "product_type"
    pass


class ProductTypeIndexView(ProductTypeMixin, AdminIndexView):
    pass


class CreateProductTypeView(ProductTypeMixin, AdminCreateView):
    pass


class UpdateProductTypeView(ProductTypeMixin, AdminUpdateView):
    pass


class DeleteProductTypeView(ProductTypeMixin, AdminDeleteView):
    pass


class ProductTypeCRUD:
    index_view = ProductTypeIndexView.as_view()
    create_view = CreateProductTypeView.as_view()
    update_view = UpdateProductTypeView.as_view()
    delete_view = DeleteProductTypeView.as_view()


# endregion


# region Part type views
class PartTypeMixin:
    table_class = PartTypeTable
    model_class = model = PartType
    index_title = update_title = create_title = "Типы деталей"
    form_class = PartTypeForm
    suffix = "part_type"
    pass


class PartTypeIndexView(PartTypeMixin, AdminIndexView):
    pass


class CreatePartTypeView(PartTypeMixin, AdminCreateView):
    pass


class UpdatePartTypeView(PartTypeMixin, AdminUpdateView):
    pass


class DeletePartTypeView(PartTypeMixin, AdminDeleteView):
    pass


class PartTypeCRUD:
    index_view = PartTypeIndexView.as_view()
    create_view = CreatePartTypeView.as_view()
    update_view = UpdatePartTypeView.as_view()
    delete_view = DeletePartTypeView.as_view()


# endregion


# region Material views
class MaterialMixin:
    table_class = MaterialTable
    model_class = model = Material
    index_title = update_title = create_title = "Типы деталей"
    form_class = MaterialForm
    suffix = "material"
    pass


class MaterialIndexView(MaterialMixin, AdminIndexView):
    pass


class CreateMaterialView(MaterialMixin, AdminCreateView):
    pass


class UpdateMaterialView(MaterialMixin, AdminUpdateView):
    pass


class DeleteMaterialView(MaterialMixin, AdminDeleteView):
    pass


class MaterialCRUD:
    index_view = MaterialIndexView.as_view()
    create_view = CreateMaterialView.as_view()
    update_view = UpdateMaterialView.as_view()
    delete_view = DeleteMaterialView.as_view()


# endregion


# region Parts views
class PartMixin:
    table_class = PartTable
    model_class = model = Part
    index_title = update_title = create_title = "Типы деталей"
    form_class = PartForm
    suffix = "part"
    success_url = "/my/parts"
    pass


class PartIndexView(PartMixin, AdminIndexView):
    pass


class CreatePartView(PartMixin, AdminCreateView):
    pass


class UpdatePartView(PartMixin, AdminUpdateView):
    pass


class DeletePartView(PartMixin, AdminDeleteView):
    pass


class PartCRUD:
    index_view = PartIndexView.as_view()
    create_view = CreatePartView.as_view()
    update_view = UpdatePartView.as_view()
    delete_view = DeletePartView.as_view()


# endregion


# region Jewelry views
class JewelryMixin:
    table_class = JewelryTable
    model_class = model = Jewelry
    index_title = update_title = create_title = "Изделия"
    form_class = JewelryForm
    suffix = "jewelry"
    pass


class JewelryIndexView(JewelryMixin, AdminIndexView):
    pass


class CreateJewelryView(JewelryMixin, AdminCreateView):
    pass


class UpdateJewelryView(JewelryMixin, AdminUpdateView):
    pass


class DeleteJewelryView(JewelryMixin, AdminDeleteView):
    pass


class JewelryCRUD:
    index_view = JewelryIndexView.as_view()
    create_view = CreateJewelryView.as_view()
    update_view = UpdateJewelryView.as_view()
    delete_view = DeleteJewelryView.as_view()


# endregion
