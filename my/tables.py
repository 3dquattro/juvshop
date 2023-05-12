import django_tables2 as tables
from core.models import ProductType, PartType, Material, Part, Jewelry
from django.utils.html import format_html
from my.models import Address


# 'Django_tables2'-table for ProductType admin index view
class ProductTypeTable(tables.Table):
    delete = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = ProductType
        fields = ("id", "name", "volumeCoefficient", "update_time", "status")
        attrs = {"class": "table table-striped table-bordered"}

    def render_name(self, value, record):
        return format_html(
            '<a href="/my/edit_product_type/{}">{}</a>', record.id, value
        )

    def render_delete(self, record):
        return format_html(
            '<a href="/my/delete_product_type/{}">Удалить</a>', record.id
        )


# 'Django_tables2'-table for PartType admin index view
class PartTypeTable(tables.Table):
    delete = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = PartType
        fields = ("id", "productType", "status", "name", "update_time")
        attrs = {"class": "table table-striped table-bordered"}

    def render_name(self, value, record):
        return format_html('<a href="/my/edit_part_type/{}">{}</a>', record.id, value)

    def render_delete(self, record):
        return format_html('<a href="/my/delete_part_type/{}">Удалить</a>', record.id)


# 'Django_tables2'-table for Material admin index view
class MaterialTable(tables.Table):
    id = tables.Column(verbose_name="ID")
    name = tables.Column(verbose_name="Название")
    price = tables.Column(verbose_name="Стоимость, руб/грамм")
    density = tables.Column(verbose_name="Плотность, кг/м^3")
    update_time = tables.Column(verbose_name="Время обновления")
    status = tables.Column(verbose_name="Статус")
    delete = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = Material
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "price", "density", "update_time", "status")
        attrs = {"class": "table table-striped table-bordered"}

    def render_name(self, value, record):
        return format_html('<a href="/my/edit_material/{}">{}</a>', record.id, value)

    def render_delete(self, record):
        return format_html('<a href="/my/delete_material/{}">Удалить</a>', record.id)


# 'Django_tables2'-table for Part admin index view
class PartTable(tables.Table):
    id = tables.Column(verbose_name="ID")
    name = tables.Column(verbose_name="Название")
    volume = tables.Column(verbose_name="Объем")
    preview = tables.Column(verbose_name="Превью")
    category = tables.Column(verbose_name="Категория")
    ModelFile = tables.Column(verbose_name="Модель")
    update_time = tables.Column(verbose_name="Время обновления")
    status = tables.Column(verbose_name="Статус")
    delete = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = Part
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "id",
            "name",
            "volume",
            "preview",
            "category",
            "ModelFile",
            "update_time",
            "status",
        )
        attrs = {"class": "table table-striped table-bordered"}

    def render_name(self, value, record):
        return format_html('<a href="/my/edit_part/{}">{}</a>', record.id, value)

    def render_delete(self, record):
        return format_html('<a href="/my/delete_part/{}">Удалить</a>', record.id)


class JewelryTable(tables.Table):
    name = tables.Column()
    parts = tables.Column()
    ispublic = tables.BooleanColumn()
    type = tables.Column()
    material = tables.Column()
    user = tables.Column()
    preview = tables.Column()
    update_time = tables.DateTimeColumn()
    status = tables.Column()
    weight = tables.Column()
    cost = tables.Column()
    is_editable = tables.BooleanColumn()
    delete = tables.Column(verbose_name="", empty_values=())

    class Meta:
        model = Jewelry
        attrs = {"class": "table table-striped table-bordered"}

    def render_name(self, value, record):
        return format_html('<a href="/my/edit_jewelry/{}">{}</a>', record.id, value)

    def render_delete(self, record):
        return format_html('<a href="/my/delete_jewelry/{}">Удалить</a>', record.id)


class AddressTable(tables.Table):
    address = tables.Column(verbose_name="Адрес")
    actions = tables.Column(verbose_name="Действия", empty_values=())

    class Meta:
        model = Address
        exclude = ["profile", "id"]
        attrs = {"class": "table table-striped table-bordered"}

    def render_actions(self, record):
        return format_html(
            '<a href="/my/profile/addresses/edit/{}">Редактировать</a>'
            ' <a href="/my/profile/addresses/delete/{}">Удалить</a>',
            record.id,
            record.id,
        )
