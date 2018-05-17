import requests
import json


class Request(object):
    def __init__(self, endpoint, password=None):
        self._endpoint = endpoint
        self._password = password

    def get(self, request_url, params={}):
        url = self.get_url(request_url)

        return requests.get(url, params=params, headers=self.get_headers())

    def post(self, request_url, params={}):
        url = self.get_url(request_url)

        return requests.post(url, json=params, headers=self.get_headers())

    def get_headers(self):
        if self._password:
            return {'Authorization': 'Basic %s' % self._password}
        return {}

    def get_url(self, request_url):
        return self._endpoint + request_url

    def response(self, request):
        resp = json.loads(request.text)
        return resp


class OmnicamAPI(Request):
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        version = "api/v1" if endpoint.endswith('/') else "/api/v1"
        endpoint = endpoint + version
        super(OmnicamAPI, self).__init__(endpoint, password=None)

    def add_activity(self, device_id, on_time, off_time, real_power_w, energy_wh):
        """
        Add Device Activity to DB
        :param device_id: ID of the device
        :param on_time: On timing of the device
        :param off_time: Off timing of the device
        :param real_power_w: Real Power
        :param energy_wh: Energy
        :return: 0 if added successfully
        """
        request_url = '/add/device/activity/'

        params = {
            'device': device_id,
            'on_time': on_time,
            'off_time': off_time,
            'real_power_w': real_power_w,
            'energy_wh': energy_wh,
        }

        resp = self.response(self.post(request_url, params))
        return resp

    def add_device_status(self, device_id, on_time, off_time, real_power_w, energy_wh):
        """
        Add Device Activity to DB
        :param device_id: ID of the device
        :param on_time: On timing of the device
        :param off_time: Off timing of the device
        :param real_power_w: Real Power
        :param energy_wh: Energy
        :return: 0 if added successfully
        """
        request_url = '/add/device/status/'

        params = {
            'device': device_id,
            'on_time': on_time,
            'off_time': off_time,
            'real_power_w': real_power_w,
            'energy_wh': energy_wh,
        }

        resp = self.response(self.post(request_url, params))
        return resp

    def add_device_monthly(self, device_id, on_time, off_time, real_power_w, energy_wh):
        """
        Add Device Activity to DB
        :param device_id: ID of the device
        :param on_time: On timing of the device
        :param off_time: Off timing of the device
        :param real_power_w: Real Power
        :param energy_wh: Energy
        :return: 0 if added successfully
        """
        request_url = '/add/device/monthly/'

        params = {
            'device': device_id,
            'on_time': on_time,
            'off_time': off_time,
            'real_power_w': real_power_w,
            'energy_wh': energy_wh,
        }

        resp = self.response(self.post(request_url, params))
        return resp

    def add_utility_track(self, home_id, bill_acc_cost, energy_main_acc_wh, power_main_w,
                    energy_bg_acc_wh, power_bg_w, voltage_v, current_a, peak_curr_acc_a, datetime_peak_acc):
        """
        :param home_id: ID of the home
        :param bill_acc_cost: Bill
        :param energy_main_acc_wh: Energy Main
        :param power_main_w: Power Main
        :param energy_bg_acc_wh: Energy Background
        :param power_bg_w: Power Background
        :param voltage_v: Voltage
        :param current_a: Current
        :param peak_curr_acc_a: Peak Current
        :param datetime_peak_acc: Timing of Peak
        :return:
        """
        request_url = '/add/utility/track/'

        params = {
            'home': home_id,
            'bill_acc_cost': bill_acc_cost,
            'energy_main_acc_wh': energy_main_acc_wh,
            'power_main_w': power_main_w,
            'energy_bg_acc_wh': energy_bg_acc_wh,
            'power_bg_w': power_bg_w,
            'voltage_v': voltage_v,
            'current_a': current_a,
            'peak_curr_acc_a': peak_curr_acc_a,
            'datetime_peak_acc': datetime_peak_acc,
        }

        resp = self.response(self.post(request_url, params))
        return resp

    def add_utility_daily(self, home_id, bill_acc_cost, energy_main_acc_wh, power_main_w,
                    energy_bg_acc_wh, power_bg_w, voltage_v, current_a, peak_curr_acc_a, datetime_peak_acc):
        """
        :param home_id: ID of the home
        :param bill_acc_cost: Bill
        :param energy_main_acc_wh: Energy Main
        :param power_main_w: Power Main
        :param energy_bg_acc_wh: Energy Background
        :param power_bg_w: Power Background
        :param voltage_v: Voltage
        :param current_a: Current
        :param peak_curr_acc_a: Peak Current
        :param datetime_peak_acc: Timing of Peak
        :return:
        """
        request_url = '/add/utility/daily/'

        params = {
            'home': home_id,
            'bill_acc_cost': bill_acc_cost,
            'energy_main_acc_wh': energy_main_acc_wh,
            'power_main_w': power_main_w,
            'energy_bg_acc_wh': energy_bg_acc_wh,
            'power_bg_w': power_bg_w,
            'voltage_v': voltage_v,
            'current_a': current_a,
            'peak_curr_acc_a': peak_curr_acc_a,
            'datetime_peak_acc': datetime_peak_acc,
        }

        resp = self.response(self.post(request_url, params))
        return resp

    def add_utility_monthly(self, home_id, bill_acc_cost, energy_main_acc_wh, power_main_w,
                    energy_bg_acc_wh, power_bg_w, voltage_v, current_a, peak_curr_acc_a, datetime_peak_acc):
        """
        :param home_id: ID of the home
        :param bill_acc_cost: Bill
        :param energy_main_acc_wh: Energy Main
        :param power_main_w: Power Main
        :param energy_bg_acc_wh: Energy Background
        :param power_bg_w: Power Background
        :param voltage_v: Voltage
        :param current_a: Current
        :param peak_curr_acc_a: Peak Current
        :param datetime_peak_acc: Timing of Peak
        :return:
        """
        request_url = '/add/utility/monthly/'

        params = {
            'home': home_id,
            'bill_acc_cost': bill_acc_cost,
            'energy_main_acc_wh': energy_main_acc_wh,
            'power_main_w': power_main_w,
            'energy_bg_acc_wh': energy_bg_acc_wh,
            'power_bg_w': power_bg_w,
            'voltage_v': voltage_v,
            'current_a': current_a,
            'peak_curr_acc_a': peak_curr_acc_a,
            'datetime_peak_acc': datetime_peak_acc,
        }

        resp = self.response(self.post(request_url, params))
        return resp
