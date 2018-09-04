import json
import swisscom.api.VoiceService_api as VoiceServiceApi


class VoiceService(VoiceServiceApi.VoiceServiceApi):

    def __init__(self):
        print('Caller')

    def allCalls(self):
        _allCallList = []
        for item in self.VoiceApplication_getCallList():
            _allCallList.append(item)

        return _allCallList

    def missedCalls(self):
        _missedCallList = []
        for item in self.VoiceApplication_getCallList():
            if 'missed' in item['callType']:
                print(item)
                _missedCallList.append(item)

        return _missedCallList

    def incommingCalls(self):
        _incommingCallList = []
        for item in self.VoiceApplication_getCallList():
            if  'succeeded' in item['callType'] and 'local' in item['callDestination']:
             #   print(item)
                _incommingCallList.append(item)

        return _incommingCallList

    def outgoingCalls(self):
        _outgoingCallList = []
        for item in self.VoiceApplication_getCallList():
            if 'succeeded' in item['callType'] and 'SIP' in item['callDestination']:
              #  print(item)
                _outgoingCallList.append(item)

        return _outgoingCallList

    def receivedCalls(self):
        _receivedCallList = []
        for item in self.VoiceApplication_getCallList():
            if 'succeeded' in item['callType']:
                print(item)
                _receivedCallList.append(item)

        return _receivedCallList
