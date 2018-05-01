
import json
import swisscom.base.ibox_base as ibox

class DynDNSApi(ibox.IboxBase):

    def __init__(self):
        print('dyndns')

    def getDynDNS(self):
        r = self._session.post(self._url + 'sysbus/DynDNS:getServices',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDynDNS %s' % r.text)
        return r.json()['result']['status']

    def setDynDNSGlobalEnable(self):
        r = self._session.post(self._url + 'sysbus/DynDNS:setGlobalEnable',
                               headers=self._sah_headers,
                               data='{"parameters":{"enable":false}}')
        self._log.debug('DynDNS:setGlobalEnable %s' % r.text)
        return r.json()['result']['status']

    def getDynDNSGloablEnable(self):
        r = self._session.post(self._url + 'sysbus/DynDNS:getGlobalEnable',
                               headers=self._sah_headers,
                               data='{"parameters":{"enable":false}}')
        self._log.debug('DynDNS:getGlobalEnable %s' % r.text)
        return r.json()['result']['status']

    def DynDNSgetHosts(self):
        r = self._session.post(self._url + 'sysbus/DynDNS:getHosts',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('DynDNS:getHosts %s' % r.text)
        return r.json()['result']['status']


    def isNameTaken(self,name):
        r = self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data='{"service":"com.swisscom.apsm/dyndns.com.swisscom.apsm.dyndns","method":"IsNameTaken","parameters":{"name": "%s"}}'%(name))
        self._log.debug('isNameTaken %s' % r.text)
        return r.json()['result']['status']

    def isEnabled(self):
        r = self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data='{"service":"com.swisscom.apsm/dyndns.com.swisscom.apsm.dyndns","method":"IsEnabled","parameters":{}}')
        self._log.debug('isEnabled %s' % r.text)
        return r.json()['result']['status']

    def getName(self):
        r = self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data='{"service":"com.swisscom.apsm/dyndns.com.swisscom.apsm.dyndns","method":"GetName","parameters":{}}')
        self._log.debug('getName %s' % r.text)
        return r.json()['result']['status']

    def configure(self,enable,name):
        if enable:
            data = '{"service":"com.swisscom.apsm/dyndns.com.swisscom.apsm.dyndns","method":"Configure","parameters":{"enable":true,"name": "%s"}}' % (name)
        else:
            data = '{"service":"com.swisscom.apsm/dyndns.com.swisscom.apsm.dyndns","method":"Configure","parameters":{"enable":false,"name": "%s"}}' % (name)

        r = self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data= data)
        self._log.debug('Configure %s' % r.text)
        return r.json()['result']['status']


    def configDynDNS(self):
        r = self._session.post(self._url + 'ws',
                               headers=self._sah_headers,
                               data='{"service":"com.swisscom.apsm/dyndns.com.swisscom.apsm.dyndns","method":"IsNameTaken","parameters":{"name":"Swisscom12345678"}}')
        self._log.debug('configDynDNS %s' % r.text)
        return r.json()['result']['status']

    def setDynDNSName(self):
        print('globalEnabl',self.setDynDNSGlobalEnable())
        print('isNameTaken',self.isNameTaken('SWISSCOM1234567'))
        print('isEnabled',self.isEnabled())
        print('getName',self.getName())
        print('Configure',self.configure('SWISSCOM1234567'))
        print('isEnabled', self.isEnabled())
        print('getName',self.getName())

