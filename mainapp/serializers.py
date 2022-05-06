from asyncore import write
from turtle import write_docstringdict
from rest_framework import serializers, exceptions
from mainapp.models import Worker, TradePoint, Visit


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            "id",
            "name",
            "phone_number",
        )


class TradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePoint
        fields = (
            "id",
            "name",
            "worker",
        )

        extra_kwargs = {
            "worker": {"write_only": True},
        }


class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class TradePointReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePoint
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("name",)


class VisitSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = Visit
        fields = (
            "id",
            "visit_time",
            "trade_point",
            "latitude",
            "longitude",
            "phone_number",
        )
        read_only_fields = (
            "id",
            "visit_time",
        )

        extra_kwargs = {
            "trade_point": {"write_only": True},
            "latitude": {"write_only": True},
            "longitude": {"write_only": True},
        }

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        worker_phone_number = attrs.get("trade_point").worker.phone_number
        if worker_phone_number == phone_number:
            return attrs
        else:
            raise exceptions.ValidationError({"error": "phone number is not valid"})

    def create(self, validated_data):
        visit = Visit.objects.create(
            trade_point=validated_data.get("trade_point"),
            latitude=validated_data.get("latitude"),
            longitude=validated_data.get("longitude"),
        )
        return visit
