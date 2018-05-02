import json
import swisscom.base.ibox_base as ibox

class VoiceServiceApi(ibox.IboxBase):

    def __init__(self):
        print('VoiceService API')

    def VoiceApplication_listTrunks(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:listTrunks',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('VoiceApplication_listTrunks %s' % r.text)
        return r.json()['result']['status']

    def VoiceApplication_listHandsets(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:listHandsets',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('VoiceApplication_listHandsets %s' % r.text)
        return r.json()['result']['status']

    def VoiceApplication_listGroups(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:listGroups',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('VoiceApplication_listGroups %s' % r.text)
        return r.json()['result']['status']

    def VoiceApplication_getSipExtensionsStatus(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:getSipExtensionsStatus',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('VoiceApplication_getSipExtensionsStatus %s' % r.text)
        return r.json()['result']['status']

    def VoiceApplication_getCallList(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:getCallList',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('VoiceApplication_getCallList %s' % r.text)
        return r.json()['result']['status']
