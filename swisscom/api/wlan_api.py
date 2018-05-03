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