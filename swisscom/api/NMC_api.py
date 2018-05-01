

import json
import swisscom.base.ibox_base as ibox

class NMCApi(ibox.IboxBase):
    def __init__(self):
        print('NMCApi')

    def deviceReboot(self):

        r = self._session.post(self._url + 'sysbus/NMC:reboot', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('deviceReboot %s' % r.text)
        return r.json()['result']['status']

    def NMC_getWANStatus(self):

        r = self._session.post(self._url+ 'sysbus/NMC:getWANStatus', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getWANStatus %s' % r.text)
        return r.json()['result']['data']

    def AgetWANStatus(self):
        r = self._session.post(self._url + 'sysbus/NMC%3AgetWANStatus', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('AgetWANStatus %s' % r.text)
        return r.json()['result']['data']
