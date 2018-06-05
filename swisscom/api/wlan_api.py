import swisscom.base.ibox_base as ibox

class WLANApi(ibox.IboxBase):

    def __init__(self):
        print('WLANapi')

    def WlanIF_get(self):
        r = self._session.post(self._url + 'sysbus/sysbus/NeMo/Intf/lan:getMIBs',
                               headers=self._sah_headers,
                   #            data='{"parameters":{}}')
                               data='{"parameters":{"mibs":"wlanvap","flag":"","traverse":"down"}}')
        self._log.debug('WlanIF_get %s' % r.text)
        return r.json()['result']['status']

    def Wifi0_getSpectrumInfo(self):
        r = self._session.post(self._url + 'sysbus/sysbus/NeMo/Intf/wifi0_bcm:getSpectrumInfo',
                               headers=self._sah_headers,
                   #            data='{"parameters":{}}')
                               #data='{parameters: {update: 1}}')
                               data = '{"parameters":{"update":1}}')
        self._log.debug('WlanIF_getSpectrumInfo %s' % r.text)
        #print('sss',r.text)
        return r.json()['result']['status']

    def Wifi0_scan(self):
        r = self._session.post(self._url + 'sysbus/sysbus/NeMo/Intf/wifi0_bcm:scan',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
                        #       data='{parameters: {}}')
        self._log.debug('WlanIF_scan %s' % r.text)
      #  print(r.text)
        return r.json()['result']['status']

    def Wifi1_getSpectrumInfo(self):
        r = self._session.post(self._url + 'sysbus/sysbus/NeMo/Intf/wifi1_bcm:getSpectrumInfo',
                               headers=self._sah_headers,
                   #            data='{"parameters":{}}')
                               data='{parameters: {update: 1}}')
        self._log.debug('WlanIF_getSpectrumInfo %s' % r.text)
        return r.json()['result']['status']

    def Wifi1_scan(self):
        r = self._session.post(self._url + 'sysbus/sysbus/NeMo/Intf/wifi1_bcm:scan',
                               headers=self._sah_headers,
                   #            data='{"parameters":{}}')
                               data='{parameters: {}}')
        self._log.debug('WlanIF_scan %s' % r.text)
        return r.json()['result']


