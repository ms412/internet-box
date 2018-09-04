import json
import swisscom.base.ibox_base as ibox

class UserManagementApi(ibox.IboxBase):

    def __init__(self):
        print('User Management API')


    def UserManagement_getUserLog(self):
        r = self._session.post(self._url + 'sysbus/UserManagement:getUserLog',
       # r=self._session.post(self._url + 'voice/v1/voip/events/subscriptions',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('UserManagement_getUserLog %s' % r.text)
        return r.json()['result']

    def Test_test(self):
        #r = self._session.post(self._url + 'sysbus/Devices:get',
        r=self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data='{"service":"eventmanager","method":"get_events","parameters":{"channelid":0, "events":[{"service":"Devices","event":"changed"},{"service":"Devices","event":"add"}]}}')
                          #     data='{"parameters":{"expression":".Active==false","traverse":"down","flags":""}}')
        self._log.debug('UserManagement_getUserLog %s' % r.text)
        print('TEST',r.text)
      #  return r.json()['result']

    def Test_test1(self):
        #r = self._session.post(self._url + 'sysbus/Devices:get',
        r=self._session.post(self._url + 'sysbus/NMC:get',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
                              # data='{"service":"eventmanager","method":"get_events","parameters":{"channelid":0, "events":[{"service":"Devices","event":"changed"},{"service":"Devices","event":"add"}]}}')
                          #     data='{"parameters":{"expression":".Active==false","traverse":"down","flags":""}}')
        self._log.debug('UserManagement_getUserLog %s' % r.text)
        print('TEST',r.text)
      #  return r.json()['result']


