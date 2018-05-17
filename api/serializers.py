from rest_framework import serializers
from device.models import Activity, Status, Monthly
from utility.models import Track, Monthly as UtilityMonthly, Daily


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = Activity.fields


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = Status.fields

    def create(self, validated_data):
        device = validated_data.get('device', None)

        try:
            item = Status.objects.get(device=device)
            self.update(item, validated_data)
            return item

        except Status.DoesNotExist:
            return super(StatusSerializer, self).create(validated_data)


class MonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monthly
        fields = Monthly.fields


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = Track.fields


class UtilityMonthlySerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilityMonthly
        fields = UtilityMonthly.fields

    def create(self, validated_data):
        home = validated_data.get('home', None)

        try:
            item = Status.objects.get(home=home)
            self.update(item, validated_data)
            return item

        except Status.DoesNotExist:
            return super(UtilityMonthlySerializer, self).create(validated_data)


class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = Daily.fields
