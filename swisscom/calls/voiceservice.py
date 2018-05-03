import json
import swisscom.api.VoiceService_api as VoiceServiceApi


class VoiceService(VoiceServiceApi.VoiceServiceApi):

    def __init__(self):
        print('Caller')

    def missedCalls(self):
        _missedCallList = []
        for item in self.VoiceApplication_getCallList():
            if 'missed' in item['callType']:
                print(item)
                _missedCallList.append(item)

        return _missedCallList

    def receivedCalls(self):
        _receivedCallList = []
        for item in self.VoiceApplication_getCallList():
            if 'missed' in item['callType']:
                print(item)
                _receivedCallList.append(item)

        return _receivedCallList
