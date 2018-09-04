
import sys
import os
import time
import json
import swisscom
import paho.mqtt.client as mqtt
from configobj import ConfigObj
from library.loghandler import loghandler


class callMonitor(object):
    def __init__(self,configfile):
        self._configfile = configfile
        self._log = None

        self._ibox = None

    def readConfig(self):
        _cfg = ConfigObj(self._configfile)

        if bool(_cfg) is False:
            print('ERROR config file not found', self._configfile)
            sys.exit()

        self._cfg_log = _cfg.get('LOGGING', None)
        self._cfg_ibox = _cfg.get('INTERNET-BOX',None)
        self._cfg_file_dir = _cfg.get('FILE_DIR',None)
        self._mqttCfg = _cfg.get('BROKER', None)

        return True

    def startLogger(self):
        self._log = loghandler()
        # print(self._cfg_log)
        self._log.handle(self._cfg_log.get('LOGMODE'), self._cfg_log)
        #       self._log.handle()
        self._log.level(self._cfg_log.get('LOGLEVEL', 'DEBUG'))
        return True

    def connect(self):
        _host = self._cfg_ibox.get('HOST','192.168.1.1')
        _user = self._cfg_ibox.get('USER','admin')
        _password = self._cfg_ibox.get('PASSWORD',None)
       # print(_host,_user,_password)

        self._ibox = swisscom.Internetbox()
        self._ibox.connect(_host,_user,_password)

    def missedCalls(self):
        print('missed',self._ibox.missedCalls())
        for counter, item in  enumerate(self._ibox.missedCalls()):
            print('##########################')
            print('Call', counter)
            print('Caller Name', item.get('remoteName','No Name'))
            print('Caller ID', item.get('remoteNumber',None))
            print('Date', item.get('startTime',None))
            print(' ')

    def oldincommingCalls(self):
        print('received',self._ibox.incommingCalls())
        for counter, item in  enumerate(self._ibox.incommingCalls()):
            print('##########################')
            print('Call', counter)
            print('Caller Name', item.get('remoteName','No Name'))
            print('Caller ID', item.get('remoteNumber',None))
            print('Date', item.get('startTime',None))
            print('Duration', item.get('duration',0))
            print(' ')

    def incommingCalls(self):

        _templist = []
        for item in self._ibox.incommingCalls():
            _tempdict = {}
          #  print('item',item)
            _tempdict['DATE'] = item.get('startTime','')
            _name= item.get('remoteName','')
            if not _name:
                _tempdict['NAME']= 'Unknown'
            else:
                _tempdict['NAME']= _name

            _tempdict['DURATION'] = item.get('duration','')
            _tempdict['CALLER'] = item.get('remoteNumber','')
            _tempdict['TO'] = item.get('trunkLineNumber','')

            _templist.append(_tempdict)
         #   print('incommfing',_templist)

        return _templist[-5:]

    def outgoingCalls(self):
      #  print('OUTGOIGN',self._ibox.outgoingCalls())
        _templist = []
        for item in self._ibox.outgoingCalls():
            _tempdict = {}
           # print('outgoign',item)
            _tempdict['DATE'] = item.get('startTime','')
            _name= item.get('remoteName','')
            if not _name:
                _tempdict['NAME']= 'Unknown'
            else:
                _tempdict['NAME']= _name

            _tempdict['DURATION'] = item.get('duration','')
            _tempdict['CALLER'] = item.get('terminal','')
            _tempdict['TO'] = item.get('remoteNumber','')

            _templist.append(_tempdict)
         #   print('temp',_tempdict)
         #   print('outgoing',_templist)

        return _templist[-5:]

    def missedCalls(self):
      #  print('OUTGOIGN',self._ibox.outgoingCalls())
        _templist = []
        for item in self._ibox.missedCalls():
            _tempdict = {}
           # print('outgoign',item)
            _tempdict['DATE'] = item.get('startTime','')
            _name= item.get('remoteName','')
            if not _name:
                _tempdict['NAME']= 'Unknown'
            else:
                _tempdict['NAME']= _name

            _tempdict['DURATION'] = item.get('duration','')
            _tempdict['CALLER'] = item.get('remoteNumbe','')
            _tempdict['TO'] = item.get('terminal','')

            _templist.append(_tempdict)
         #   print('temp',_tempdict)
         #   print('outgoing',_templist)

        return _templist[-5:]

    def getCallerList(self):
        _temp = {}

        _temp['INCOMMING'] = self.incommingCalls()
        _temp['OUTGOING'] = self.outgoingCalls()
        _temp['MISSED'] = self.missedCalls()

        self._log.debug('getCallerList %s' % (_temp))

        return _temp


    def mqttPublish(self, topic, data):
        _host = str(self._mqttCfg.get('HOST', 'localhost'))
        _port = int(self._mqttCfg.get('PORT', 1883))
        _channel = str(self._mqttCfg.get('PUBLISH', 'OPENHAB'))
        _deviceId = str(self._mqttCfg.get('DEVICE', 'INTERNETBOX'))
        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

        #   try:
        self._mqttc.connect(_host, _port, 60)
        _topic = '/' + _channel + '/' + _deviceId + '/' + topic
        self._mqttc.publish(_topic, json.dumps(data))
        #    print(_topic, json.dumps(data))
        self._mqttc.loop(10)
        self._mqttc.disconnect()
        self._log.debug('message delivered to mqtt Server: %s; Topic: %s; Message: %s' % (_host, _topic, data))

        return True

if __name__ == "__main__":

    callmon = callMonitor('./internetboxCallMonitor2mqtt.cfg')
    callmon.readConfig()
    callmon.startLogger()
    callmon.connect()
    for key,item in callmon.getCallerList().items():
        callmon.mqttPublish(key,item)


