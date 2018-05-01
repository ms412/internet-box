
__app__ = "SwisscomInternetBox"
__VERSION__ = "0.1"
__DATE__ = "25.04.2018"
__author__ = "Markus Schiesser"
__contact__ = "M.Schiesser@gmail.com"

#https://www.heyrick.co.uk/blog/index.php?diary=20140804
#https://x0r.fr/blog/33
#https://github.com/home-assistant/home-assistant/blob/de9d19d6f44f3b4cd4a2425315e5d3b2d23f205f/homeassistant/components/device_tracker/swisscom.py
#https://github.com/rene-d/sysbus

import requests
import logging
#from library.loghandler import loghandler

#module_logger = logging.getLogger('internetboy')


class IboxBase(object):

    def __init__(self):
        print('Create Base')
     #   self._log = logging.getLogger('InternetBox.IboxBase')
        self._log.debug('Create boxmgr object')

        self._host = None

        self._user = None
        self._passwd = None

        self._url = None
        self._session = None
        self._cookie = None

        self._header = None

        self._sah_headers = None

    def connect(self,host,user,passwd):

        self._user = user
        self._passwd = passwd
        self._url = 'http://{}/'.format(host)

        self._session = requests.Session()

        _headers = {'Content-Type': 'application/x-sah-ws-1-call+json',
                       'Authorization': 'X-Sah-Login'}

        _data = '{"service":"sah.Device.Information","method":"createContext",' \
                '"parameters":{"applicationName":"so_sdkut","username":"%s","password":"%s"}}' % (self._user, self._passwd)

        r = self._session.post(self._url + 'ws', data=_data, headers=_headers)
        self._log.debug('Create session %s' % r.text)

        if not 'contextID' in r.json()['data']:
            print("auth error", str(r.text))
            self._log.error('Authentification Failure %s' % r.text)
            exit()

        self._cookie = r.json()['data']['contextID']
        print(self._cookie)
        self._log.debug('Cookie %s' % r.text)

        self._sah_headers = {'X-Context': self._cookie,
                       'X-Prototype-Version': '1.7',
                       'Content-Type': 'application/x-sah-ws-1-call+json; charset=UTF-8',
                       'Accept': 'text/javascript'}
        return True


    def getSystemDate(self):

        r = self._session.post(self._url + 'sysbus/Time:getTime', headers=self._sah_headers, data='{"parameters":{}}')

        self._log.debug('getSystemDate %s' % r.text)
        return r.json()['result']['data']['time']




class internetbox_old(object):

    def __init__(self,host):
        self._log = logging.getLogger('InternetBox.boxmgr')
        self._log.debug('Create boxmgr object')

        self._host = host

        self._user = None
        self._passwd = None

        self._url = 'http://{}/'.format(host)
        self._session = None
        self._cookies = None

        self._header = None

        self._sah_headers = None

    def connect(self,user,passwd):

        self._user = user
        self._passwd = passwd

        self._session = requests.Session()

        _headers = {'Content-Type': 'application/x-sah-ws-1-call+json',
                       'Authorization': 'X-Sah-Login'}

        _data = '{"service":"sah.Device.Information","method":"createContext",' \
                '"parameters":{"applicationName":"so_sdkut","username":"%s","password":"%s"}}' % (self._user, self._passwd)

        r = self._session.post(self._url + 'ws', data=_data, headers=_headers)
        self._log.debug('Create session %s' % r.text)

        if not 'contextID' in r.json()['data']:
            print("auth error", str(r.text))
            self._log.error('Authentification Failure %s' % r.text)
            exit()

        self._cookies = r.json()['data']['contextID']
        self._log.debug('Cookies %s' % r.text)

        self._sah_headers = {'X-Context': self._cookies,
                       'X-Prototype-Version': '1.7',
                       'Content-Type': 'application/x-sah-ws-1-call+json; charset=UTF-8',
                       'Accept': 'text/javascript'}
        return True

    def getSystemDate(self):

        r = self._session.post(self._url + 'sysbus/Time:getTime', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getSystemDate %s' % r.text)
        return r.json()['result']['data']['time']

    def getDeviceInfo(self):

        r = self._session.post(self._url + 'sysbus/DeviceInfo:get', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getDeviceInfo %s' % r.text)
        return r.json()['result']['status']

    def getDevices(self):

        r = self._session.post(self._url + 'sysbus/Devices:get', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getDevices %s' % r.text)
        return r.json()['result']['status']

    def deviceReboot(self):

        r = self._session.post(self._url + 'sysbus/NMC:reboot', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('deviceReboot %s' % r.text)
        return r.json()['result']['status']

    def getWANStatus(self):

        r = self._session.post(self._url+ 'sysbus/NMC:getWANStatus', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getWANStatus %s' % r.text)
        return r.json()['result']['data']

    def AgetWANStatus(self):
        r = self._session.post(self._url + 'sysbus/NMC%3AgetWANStatus', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('AgetWANStatus %s' % r.text)
        return r.json()['result']['data']

    def getInterface(self):

        r = self._session.post(self._url + 'sysbus/NeMo/Intf/data:getMIBs', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getInterface %s' % r.text)
        return r.json()['result']['status']

    def getLANInterface(self):

        r = self._session.post(self._url + 'sysbus/NeMo/Intf/lan:getMIBs', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getLANInterface %s' % r.text)
        return r.json()['result']['status']

    def getLANIP(self):

        r = self._session.post(self._url + 'sysbus/NMC:getLANIP', headers=self._sah_headers, data='{"parameters":{}}')
        self._log.debug('getLANIP %s' % r.text)
        return r.json()['result']['status']

    def getDECT(self):
        r = self._session.post(self._url + 'sysbus/DECT:get', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDECT %s' % r.text)
        return r.json()['result']['status']

    def getDECTVersion(self):
        r = self._session.post(self._url + 'sysbus/DECT:getVersion', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDECTVersion %s' % r.text)
        return r.json()['result']['status']

    def getDECTRFPI(self):
        r = self._session.post(self._url + 'sysbus/DECT:getRFPI', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDECTRFPI %s' % r.text)
        return r.json()['result']['status']

    def getDECTPin(self):
        r = self._session.post(self._url + 'sysbus/DECT:getPIN', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDECTPin %s' % r.text)
        return r.json()['result']['status']

    def getDECTBaseState(self):
        r = self._session.post(self._url + 'sysbus/DECT:getBaseState', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDECTBaseState %s' % r.text)
        return r.json()['result']['status']

    def getDECTNEMoState(self):
        r = self._session.post(self._url + 'sysbus/DECT:getNEMoState', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getNEMoState %s' % r.text)
        return r.json()['result']['status']

    def getDECTStatus(self):
        r = self._session.post(self._url + 'sysbus/DECT%3AgetBaseState', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDECTStatus %s' % r.text)
        return r.json()['result']['status']

    def getVoiceTrunkList(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:listTrunks', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getVoiceTrunkList %s' % r.text)
        return r.json()['result']['status']

    def getVoiceSipExtensionsStatus(self):

        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:getSipExtensionsStatus', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getVoiceSipExtensionsStatus %s' % r.text)
        return r.json()['result']['status']

    def getVoiceCallList(self):

        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:getCallList', headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getVoiceCallList %s' % r.text)
        return r.json()['result']['status']

    def getVoicelistGroups(self):
        r = self._session.post(self._url + 'sysbus/VoiceService/VoiceApplication:listGroups',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getVoicelistGroups %s' % r.text)
        return r.json()['result']['status']

    def getPhonebookAllContacts(self):
        r = self._session.post(self._url + 'sysbus/Phonebook:getAllContacts',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getPhonebookAllContacts %s' % r.text)
        return r.json()['result']['status']

    def getUsers(self):
        r = self._session.post(self._url + 'sysbus/UserManagement:getUsers',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getUsers %s' % r.text)
        return r.json()['result']['status']

    def getPowerManagement(self):
        r = self._session.post(self._url + 'sysbus/APController/PowerManagement%3AgetMode',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getPowerManagement %s' % r.text)
        return r.json()['result']['status']

    def getWifi(self):
        r = self._session.post(self._url + 'sysbus/NMC/Wifi:get',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getWifi %s' % r.text)
        return r.json()['result']['status']



    def getVPN(self):
        r = self._session.post(self._url + 'sysbus/VPN:getServersConfig',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getVPN %s' % r.text)
        return r.json()['result']['status']

    def getDNS(self):
        r = self._session.post(self._url + 'sysbus/DNS:get',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getDNS %s' % r.text)
        return r.json()['result']['status']

    def getLAN(self):
        r = self._session.post(self._url + 'sysbus/APController/LAN:get',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('getLAN %s' % r.text)
        return r.json()['result']['status']










