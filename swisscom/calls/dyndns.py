import json
import swisscom.api.dyndns_api as dyndnsApi
import swisscom.api.NMC_api as NMCApi
#from swisscom.calls.phonebook import phonebook

class DynDNS(dyndnsApi.DynDNSApi,
             NMCApi.NMCApi):

    def __init__(self):
        print('Calls DynDNS')

    def setDynDNSName(self,name):
     #   print('getDynDNS',self.isEnabled())
        print('getDynDNSGloabl',self.getDynDNSGloablEnable())
        _j= json.loads(self.isEnabled())
        if _j['result']:
            self._log.error('DynDNS already enabled')
            return False

        else:
            if self.setDynDNSGlobalEnable():

                _j = json.loads(self.isNameTaken(name))
                if not _j['result']:
                    self.configure(True,name)
                    self.isEnabled()
                    self.getName()
                    self.DynDNSgetHosts()
                    self._log.info('DynDNS name: %s, IP Address: %s)'%(name, self.NMC_getWANStatus()['IPAddress']))

                else:
                    self._log.error('Name: %s is in use'%(name))
                    return False
            else:
                self._log.error('Failed to enable DynDNS')
                return False

        return True

    def delDynDNSservice(self):

        self.DynDNSgetHosts()
        self.setDynDNSGlobalEnable()
        self.configure(False,'')
        self.isEnabled()
        self.getDynDNSGloablEnable()
        self.DynDNSgetHosts()

