from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from visitor_app.models import Visitor
from visitor_app.serializers import VisitorSerializer
# Create your views here.


class Visitor(generics.GenericAPIView,
              generics.mixins.CreateModelMixin,
              generics.mixins.ListModelMixin):

    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)