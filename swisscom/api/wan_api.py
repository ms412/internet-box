import swisscom.base.ibox_base as ibox

class WANApi(ibox.IboxBase):

    def __init__(self):
        print('WANApi')

    def WanIF_get(self,channelid):
        r = self._session.post(self._url + 'sysbus/ws',
                               headers=self._sah_headers,
                          #     data='{"service":"eventmanager","method":"get_events","parameters":{"channelid":99}}')
                               data='{"parameters":{"channelid":%s}}'%(channelid))
        self._log.debug('WanIF_get %s' % r.text)
        return r.json()['result']['status']


    def getEvent_get(self):
        r = self._session.post(self._url + 'sysbus/ws',
                               headers=self._sah_headers,
                              # data='{"parameters": {"events": [{"service": "Devices.Device", "event": "network"}, {"handler": "NeMo.Intf.wwan"}],"channelid": 0}}')
                               data='{"parameters": {"events": [{"service": "Devices.Device", "event": "network"}, {"handler": "NeMo.Intf.wwan"}],"channelid": 0}, "service": "eventmanager", "method": "get_events"}')
        self._log.debug('getEvent_get %s' % r.text)
        return r.json()['result']['status']
