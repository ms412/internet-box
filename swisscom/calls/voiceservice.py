import json
import swisscom.api.VoiceService_api as VoiceServiceApi


class VoiceService(VoiceServiceApi.VoiceServiceApi):

    def __init__(self):
        print('Caller')

    def getmissedCalls(self):
        _missedCallList = []
        for item in self.VoiceApplication_getCallList():
            if 'missed' in item['callType']:
                print(item)
                _missedCallList.append(item)

        return _missedCallList
