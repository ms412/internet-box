import json
import swisscom.base.ibox_base as ibox

class EventApi(ibox.IboxBase):

    def __init__(self):
        print('event')

    def addEvent(self):
        r = self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data='{"service":"eventmanager","method":"get_events","parameters":{"channelid":0, "events":[{"service":"Devices","event":"changed"},{"service":"Devices","event":"add"}]}}' )
        self._log.debug('getDynDNS %s' % r.text)
        return r.json()['result']['status']
