from django import forms
from project.models import Project, DeviceType, Home, Hardware
from device.models import Device, Status as DeviceStatus, Activity, Monthly as DeviceMonthly
from utility.models import Track as UtilityTrack, Daily as UtilityDaily, Monthly as UtilityMonthly


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = Project.fields


class DeviceTypeForm(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = DeviceType.fields


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = Home.fields


class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = Hardware.fields


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = Device.fields


class DeviceStatusForm(forms.ModelForm):
    class Meta:
        model = DeviceStatus
        fields = DeviceStatus.fields


class DeviceMonthlyForm(forms.ModelForm):
    class Meta:
        model = DeviceMonthly
        fields = DeviceMonthly.fields


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = Activity.fields


class UtilityTrackForm(forms.ModelForm):
    class Meta:
        model = UtilityTrack
        fields = UtilityTrack.fields


class UtilityDailyForm(forms.ModelForm):
    class Meta:
        model = UtilityDaily
        fields = UtilityDaily.fields


class UtilityMonthlyForm(forms.ModelForm):
    class Meta:
        model = UtilityMonthly
        fields = UtilityMonthly.fields
