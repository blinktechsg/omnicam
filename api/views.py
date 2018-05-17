from rest_framework.generics import CreateAPIView

import serializers


class CreateActivityView(CreateAPIView):
    serializer_class = serializers.ActivitySerializer


class CreateTrackView(CreateAPIView):
    serializer_class = serializers.TrackSerializer


class CreateStatusView(CreateAPIView):
    serializer_class = serializers.StatusSerializer


class CreateMonthlyView(CreateAPIView):
    serializer_class = serializers.MonthlySerializer


class CreateUtilityMonthlyView(CreateAPIView):
    serializer_class = serializers.UtilityMonthlySerializer


class CreateDailyView(CreateAPIView):
    serializer_class = serializers.DailySerializer
