
import sys
import time
import swisscom
from configobj import ConfigObj
from library.loghandler import loghandler


class phonebook(object):
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
        print(self._ibox.getmissedCalls())



if __name__ == "__main__":

    phonebook = phonebook('./phonebook.cfg')
    phonebook.readConfig()
    phonebook.startLogger()
    phonebook.connect()
    phonebook.getPhonebook()
    uuid = phonebook.addPhonebookEntry('firstname','famielyname',[{'type':'HOME','name':'123567'},{'type':'CELL','name':'5668'}])
    time.sleep(5)
    phonebook.delPhonebookEntry(uuid)

