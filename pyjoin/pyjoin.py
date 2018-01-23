#!/usr/bin/env python3

import requests
import fire


class Join(object):
    
    def __init__(self, apikey=None):
        self.apikey = apikey
        self.send_url = "https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush"
        self.list_url = "https://joinjoaomgcd.appspot.com/_ah/api/registration/v1/listDevices"

    def get_devices(self):
        params = {"apikey": self.apikey}
        response = requests.get(self.list_url, params=params).json()
        if response.get('success') and not response.get('userAuthError'):
            for r in response['records']:
                print("{}: {}".format(r['deviceName'], r['deviceId']))
                return
        else:
            return False

    def send_notification(self, text, device_id=None, device_ids=None, device_names=None, title=None, icon=None,
                          smallicon=None, vibration=None):

        if device_id is None and device_ids is None and device_names is None:
            return False

        params = dict(apikey=self.apikey, text=text)

        if title:
            params['title'] = title
        if icon:
            params['icon'] = icon
        if smallicon:
            params['smallicon'] = + smallicon
        if vibration:
            params['vibration'] = vibration
        if device_id:
            params['deviceId'] = device_id
        if device_ids:
            params['deviceIds'] = device_ids
        if device_names:
            params['deviceNames'] = device_names

        requests.get(self.send_url, params=params)

    def ring_device(self, device_id=None, device_ids=None, device_names=None):
        if device_id is None and device_ids is None and device_names is None:
            return False
        req_url = self.send_url + self.apikey + "&find=true"
        if device_id:
            req_url += "&deviceId=" + device_id
        if device_ids:
            req_url += "&deviceIds=" + device_ids
        if device_names:
            req_url += "&deviceNames=" + device_names

        requests.get(req_url)

    def send_url(self, url, device_id=None, device_ids=None, device_names=None, title=None, text=None):
        if device_id is None and device_ids is None and device_names is None:
            return False

        req_url = self.send_url + self.apikey + "&url=" + url

        if title:
            req_url += "&title=" + title

        req_url += "&text=" + text if text else "&text="
        if device_id:
            req_url += "&deviceId=" + device_id
        if device_ids:
            req_url += "&deviceIds=" + device_ids
        if device_names:
            req_url += "&deviceNames=" + device_names

        requests.get(req_url)

    def set_wallpaper(self, url, device_id=None, device_ids=None, device_names=None):
        if device_id is None and device_ids is None and device_names is None:
            return False
        req_url = self.send_url + self.apikey + "&wallpaper=" + url
        if device_id:
            req_url += "&deviceId=" + device_id
        if device_ids:
            req_url += "&deviceIds=" + device_ids
        if device_names:
            req_url += "&deviceNames=" + device_names

        requests.get(req_url)

    def send_file(self, url, device_id=None, device_ids=None, device_names=None, title=None, text=None):
        if device_id is None and device_ids is None and device_names is None:
            return False
        req_url = self.send_url + self.apikey + "&file=" + url
        req_url += "&text=" + text if text else "&text="
        if title:
            req_url += "&title=" + title
        if device_id:
            req_url += "&deviceId=" + device_id
        if device_ids:
            req_url += "&deviceIds=" + device_ids
        if device_names:
            req_url += "&deviceNames=" + device_names

        requests.get(req_url)

    def send_sms(self, sms_number, sms_text, device_id=None, device_ids=None, device_names=None):
        if device_id is None and device_ids is None and device_names is None:
            return False
        req_url = self.send_url + self.apikey + "&smsnumber=" + sms_number + "&smstext=" + sms_text
        if device_id:
            req_url += "&deviceId=" + device_id
        if device_ids:
            req_url += "&deviceIds=" + device_ids
        if device_names:
            req_url += "&deviceNames=" + device_names
            
        requests.get(req_url)

if __name__ == '__main__':
    fire.Fire(Join)
