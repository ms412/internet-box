
import sys
import time
import swisscom
import threading

from configobj import ConfigObj

from library.loghandler import loghandler


class monitorDevice(threading.Thread):
    def __init__(self,configfile):
        threading.Thread.__init__(self)

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

    def run(self):
        self.readConfig()
        self.startLogger()
        self.connect()

        while True:
            self.monitor()
            time.sleep(5)

    def monitor(self):
        print(self._cfg_devices)
        _macList = []
        for key, item in self._cfg_devices.items():
            _macList.append(item.upper())

        while True:
            for item in _macList:
                print(self._ibox.stateDevice(item),item)

if __name__ == "__main__":
    mon = monitorDevice('./example/monitorDevice.cfg')
    mon.start()


