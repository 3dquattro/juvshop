from django.urls import path
from my.views import (
    MyIndexView,
    MyOrdersView,
    cart_view,
    confirm_view,
    order_view,
    add_to_cart,
    make_order,
    messages_for_order,
    dialogues_list,
    signup_view,
    login_view,
    logout_view,
    PartTypeCRUD,
    PartCRUD,
    MaterialCRUD,
    ProductTypeCRUD,
    JewelryCRUD,
    ProfileViews,
)


urlpatterns = [
    # Main urls for 'my' app
    path("", MyIndexView.as_view()),
    path("orders", MyOrdersView.as_view()),
    # Urls for cart-order part
    path("cart", cart_view),
    path("addtocart", add_to_cart),
    path("cart/makeorder", make_order),
    path("order/<int:id>/confirm", confirm_view),
    path("order/<int:id>", order_view),
    # urls for authentification
    path("login/", login_view),
    path("logout", logout_view),
    path("register/", signup_view),
    # urls for inner messanger
    path("messages/<int:id>", messages_for_order),
    path("messages", dialogues_list),
    #
    path("product_types", ProductTypeCRUD.index_view),
    path("create_product_type", ProductTypeCRUD.create_view),
    path("edit_product_type/<int:pk>", ProductTypeCRUD.update_view),
    path("delete_product_type/<int:pk>", ProductTypeCRUD.delete_view),
    #
    path("part_types", PartTypeCRUD.index_view),
    path("create_part_type", PartTypeCRUD.create_view),
    path("edit_part_type/<int:pk>", PartTypeCRUD.update_view),
    path("delete_part_type/<int:pk>", PartTypeCRUD.delete_view),
    #
    path("parts", PartCRUD.index_view),
    path("create_part", PartCRUD.create_view),
    path("edit_part/<int:pk>", PartCRUD.update_view),
    path("delete_part/<int:pk>", PartCRUD.delete_view),
    #
    path("materials", MaterialCRUD.index_view),
    path("create_material", MaterialCRUD.create_view),
    path("edit_material/<int:pk>", MaterialCRUD.update_view),
    path("delete_material/<int:pk>", MaterialCRUD.delete_view),
    #
    path("jewelries", JewelryCRUD.index_view),
    path("create_jewelry", JewelryCRUD.create_view),
    path("edit_jewelry/<int:pk>", JewelryCRUD.update_view),
    path("delete_jewelry/<int:pk>", JewelryCRUD.delete_view),
    path("profile", ProfileViews.index_view),
    path("profile/addresses", ProfileViews.addresses_index),
    path("profile/addresses/edit/<int:pk>", ProfileViews.AddressEdit.as_view()),
    path("profile/addresses/delete/<int:pk>", ProfileViews.AddressDelete.as_view()),
    path("profile/addresses/create", ProfileViews.AddressCreate.as_view()),
]
