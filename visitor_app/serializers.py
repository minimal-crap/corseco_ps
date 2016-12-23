from rest_framework import serializers
from visitor_app.models import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ("name", "email", "phone", "whom_to_meet", "company_name", "photo")