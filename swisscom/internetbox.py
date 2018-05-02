
import logging

from swisscom.calls.dyndns import DynDNS
from swisscom.calls.phonebook import Phonebook
from swisscom.calls.devicelist import Devicelist
from swisscom.calls.voiceservice import VoiceService



class Internetbox(DynDNS,
                  Phonebook,
                  Devicelist,
                  VoiceService):

    def __init__(self):
        print('Create')
        self._log = logging.getLogger('internet-box')
        self._log.debug('Create boxmgr object')


    pass