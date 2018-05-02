import json
import swisscom.base.ibox_base as ibox

class ToDApi(ibox.IboxBase):

    def __init__(self):
        print('VoiceService API')

    def ToD_listMST(self):
        r = self._session.post(self._url + 'sysbus/ToD:listMST',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('ToD_listMST %s' % r.text)
        return  r.json()['result']['data']['ids']

    def ToD_getMST(self,id):
        r = self._session.post(self._url + 'sysbus/ToD:getMST',
                               headers=self._sah_headers,
                               data='{"parameters":{"id": "%s"}}'%(id))
        self._log.debug('ToD_getMST %s' % r.text)
        return r.json()['result']['data']

    def ToD_statsMST(self,id):
        r = self._session.post(self._url + 'sysbus/ToD:statsMST',
                               headers=self._sah_headers,
                               data='{"parameters":{"id": "%s"}}'%(id))
        self._log.debug('ToD_statsMST %s' % r.text)
        return r.json()['result']['data']

    def ToD_listDetails(self):
        r = self._session.post(self._url + 'sysbus/ws',
                               headers=self._sah_headers,
                               data='{"service":"Devices","method":"get","parameters":{"expression":"lan and not self and not interface","flags":"no_actions"}}')
        self._log.debug('ToD_statsMST %s' % r.text)
        return r.json()['result']['status']