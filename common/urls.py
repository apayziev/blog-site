from common.views import ContactUsSerializerView
from django.urls import path


app_name = "common"


urlpatterns = [
    path("create/", ContactUsSerializerView.as_view(), name="contact-us"),
]
