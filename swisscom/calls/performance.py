import json
import swisscom.api.wlan_api as WLANApi
import swisscom.api.wan_api as WANApi


class Perfromance(WLANApi.WLANApi,
                  WANApi.WANApi):

    def __init__(self):
        print('Performance')

    def PM_Wlan_5G(self):
        _counterList = []
        value = self.WlanIF_get()['wlanvap']['wl0']['AssociatedDevice']

        for key, item in value.items():
            if item['Active']:
                _counterList.append(item)

        return _counterList

    def PM_Wlan_24G(self):
        _counterList = []
        value = self.WlanIF_get()['wlanvap']['wl1']['AssociatedDevice']

        for key, item in value.items():
            if item['Active']:
                _counterList.append(item)

        return _counterList

    def PM_Wan(self):
        print(self.getEvent_get())
        channel = self.getEvent_get()['channelid']
        print('channel',channel)
        print(self.WanIF_get(32))

