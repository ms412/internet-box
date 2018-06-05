
import logging

from swisscom.calls.dyndns import DynDNS
from swisscom.calls.phonebook import Phonebook
from swisscom.calls.devicelist import Devicelist
from swisscom.calls.voiceservice import VoiceService
from swisscom.calls.performance import Perfromance
from swisscom.calls.wifi import Wifi



class Internetbox(DynDNS,
                  Phonebook,
                  Devicelist,
                  VoiceService,
                  Perfromance,
                  Wifi):

    def __init__(self):
        print('Create')
        self._log = logging.getLogger('internet-box')
        self._log.debug('Create boxmgr object')


    pass