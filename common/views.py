from rest_framework import generics
from common.models import ContactUs
from common.serializers import ContactUsSerializer
# Create your views here.

class ContactUsSerializerView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer