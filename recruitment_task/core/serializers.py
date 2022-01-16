from rest_framework import serializers

from core.models import Project, Investor

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_field = ["funded", "funded_by"]


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = "__all__"
        read_only_fields = ["remaining_amount"]


class ProjectDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'amount', 'delivery_date', 'funded', 'funded_by', 'matching_investor_ids')
        read_only_fields = ["funded", "funded_by"]


class InvestorDetailsSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Investor
        fields = ('id', 'name', 'remaining_amount', 'total_amount', 'individual_amount', 'project_delivery_deadline', 'matching_project_ids')
        read_only_fields = ["remaining_amount"]

