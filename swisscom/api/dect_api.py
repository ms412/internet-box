import json
import swisscom.base.ibox_base as ibox

class DECTapi(ibox.IboxBase):

    def __init__(self):
        print('DECTapi')

    def DECT_getPin(self):
        r = self._session.post(self._url + 'sysbus/sysbus/DECT:getPIN',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('DECT_getPin %s' % r.text)
        return r.json()['result']['status']

    def DECT_getBaseState(self):
        r = self._session.post(self._url + 'sysbus/sysbus/DECT:getBaseState',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('DECT_getBaseState %s' % r.text)
        return r.json()['result']['status']

    def DECT_getNEMoState(self):
        r = self._session.post(self._url + 'sysbus/sysbus/DECT:getNEMoState',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('DECT_getNEMoState %s' % r.text)
        return r.json()['result']['status']

    def DECT_getVersion(self):
        r = self._session.post(self._url + 'sysbus/sysbus/DECT:getVersion',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('DECT_getVersion %s' % r.text)
        return r.json()['result']['status']

    def DECT_getRFPI(self):
        r = self._session.post(self._url + 'sysbus/sysbus/DECT:getRFPI',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('DECT_getRFPI %s' % r.text)
        return r.json()['result']['status']