
import logging
from swisscom.calls.dyndns import DynDNS
from swisscom.calls.phonebook import Phonebook


class Internetbox(DynDNS,
                  Phonebook):

    def __init__(self):
        print('Create')
        self._log = logging.getLogger('internet-box')
        self._log.debug('Create boxmgr object')


    pass