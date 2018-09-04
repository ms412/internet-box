
import logging

from swisscom.calls.dyndns import DynDNS
from swisscom.calls.phonebook import Phonebook
from swisscom.calls.devicelist import Devicelist
from swisscom.calls.voiceservice import VoiceService
from swisscom.calls.performance import Perfromance
from swisscom.calls.wifi import Wifi
from swisscom.calls.usermanagement import UserManagement



class Internetbox(DynDNS,
                  Phonebook,
                  Devicelist,
                  VoiceService,
                  Perfromance,
                  Wifi,
                  UserManagement):

    def __init__(self):
    #    print('Create')
        self._log = logging.getLogger('internet-box')
        self._log.debug('Create boxmgr object')


    pass