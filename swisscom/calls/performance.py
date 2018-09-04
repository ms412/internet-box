import json
import swisscom.api.wlan_api as WLANApi
import swisscom.api.wan_api as WANApi
import swisscom.api.event_api as EventApi

class Perfromance(WLANApi.WLANApi,WANApi.WANApi):
 #   WLANApi.WLANApi,                  WANApi.WANApi):

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
        _result = {}
        value = self.WanIF_state()
        _result['TX_BYTE']=value['stats']['BytesSent']
        _result['RX_BYTE']=value['stats']['BytesReceived']
        _result['TX_PACKETS']=value['stats']['PacketsSent']
        _result['RX_PACKETS']=value['stats']['PacketsReceived']
        return _result

