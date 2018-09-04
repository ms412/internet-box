
import os
import sys
import time
import json
import swisscom
#import threading
import paho.mqtt.client as mqtt

from configobj import ConfigObj

from library.loghandler import loghandler


class Performance(object):
    def __init__(self,configfile):

        self._configfile = configfile
        self._log = None

        self._ibox = None

    def readConfig(self):
        print('READCONFIG',self._configfile)
        _cfg = ConfigObj(self._configfile)

        if bool(_cfg) is False:
            print('ERROR config file not found', self._configfile)
            sys.exit()

        self._cfg_log = _cfg.get('LOGGING', None)
        self._cfg_ibox = _cfg.get('INTERNET-BOX',None)
        self._cfg_devices = _cfg.get('DEVICES',None)
        self._mqttCfg = _cfg.get('MQTT', None)
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

        self._ibox = swisscom.Internetbox()
        self._ibox.connect(_host,_user,_password)

        return True

    def mqttPublish(self, topic, data):
        _host = str(self._mqttCfg.get('HOST', 'localhost'))
        _port = int(self._mqttCfg.get('PORT', 1883))
        _channel = str(self._mqttCfg.get('PUBLISH', 'OPENHAB'))
        _deviceId = str(self._mqttCfg.get('DEVICE','FRITZBOX'))
        self._mqttc = mqtt.Client(str(os.getpid()), clean_session=True)

     #   try:
        self._mqttc.connect(_host, _port, 60)
        _topic = '/' + _channel + '/' + _deviceId + '/' + topic
        self._mqttc.publish(_topic, json.dumps(data))
        self._mqttc.loop(10)
        self._mqttc.disconnect()
        self._log.debug('message delivered to mqtt Server: %s; Topic: %s; Message: %s'%(_host,_topic,data))
      #  except:
       #     self._log.error('Cannot deliver message to mqtt Server')

        return True

    def WLAN(self):
        print("--- WLAN 5 G ---")
        for item in self._ibox.PM_Wlan_5G():
            print('MAC Address', item['MACAddress'])
            print('SignalNoiseRation', item['SignalNoiseRatio'])
            print('RxPacketCount', item['RxPacketCount'])
            print('TxPacketCount', item['TxPacketCount'])
            print('DownlinkRate', item ['LastDataDownlinkRate'])
            print('UplinkRate', item['LastDataUplinkRate'])

        print("--- WLAN 2.4 G ---")
        for item in self._ibox.PM_Wlan_24G():
            print('MAC Address', item['MACAddress'])
            print('SignalNoiseRation', item['SignalNoiseRatio'])
            print('RxPacketCount', item['RxPacketCount'])
            print('TxPacketCount', item['TxPacketCount'])
            print('DownlinkRate', item ['LastDataDownlinkRate'])
            print('UplinkRate', item['LastDataUplinkRate'])

    def WAN(self):
       # print ("--- WAN ---")
        return self._ibox.PM_Wan()

    def Calls(self):
        print('tt',self._ibox.missedCalls())
        print('xx',self._ibox.receivedCalls())


    def run(self):
        self.readConfig()
        self.startLogger()
        self.connect()
        #self.WLAN()
        self.Calls()
        self.mqttPublish('PM',self.WAN())


if __name__ == "__main__":
    PM = Performance('./Performance.cfg')
    PM.run()

