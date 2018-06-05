
import json
import swisscom.api.wlan_api as Wifi


class Wifi(Wifi.WLANApi):

    def __init__(self):
        print('Wlan')

    def scan2G(self):
        print(self.Wifi0_getSpectrumInfo())
        print(self.Wifi0_scan())