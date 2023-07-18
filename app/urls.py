# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    
    path("", views.Index.as_view(), name="index"),
    path("form/", views.Form.as_view(), name="form"),
    path("icon/", views.Icon.as_view(), name="icon"),
    path("buttons/", views.Button.as_view(), name="buttons"),
    path("typography/", views.Typography.as_view(), name="typography"),
    path("charts/", views.Chart.as_view(), name="charts"),
    path("tables/", views.Table.as_view(), name="tables"),
    path("error/", views.Error.as_view(), name="error"),
    
    path("book_create/", views.BookCreate.as_view(), name="book_create"),
    path("book_list/", views.BookList.as_view(), name="book_list"),
    path("book_detail/<str:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("book_update/<str:pk>/", views.BookUpdate.as_view(), name="book_update"),
    path("book_delete/<str:pk>/", views.BookDelete.as_view(), name="book_delete"),

]

