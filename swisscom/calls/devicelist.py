import json
import swisscom.api.ToD_api as ToDApi


class Devicelist(ToDApi.ToDApi):

    def __init__(self):
        print('DeviceList')

    def getMACAddresses(self):
      #  print(self.ToD_listMST())
        return self.ToD_listMST()

    def getDeviceList(self):
        _macList = []
        _detailList = self.ToD_listDetails()
        for item in self.getMACAddresses():
           # print(item)
            _mac = ':'.join(format(s, '02x') for s in bytes.fromhex(item))
            _mac = _mac.upper()
            print(_mac)
            for item in _detailList:

                if _mac in item['Key']:
                    print(item['Name'],item['Active'],item['IPAddress'])

    def stateDevice(self,mac):

        _detailList = self.ToD_listDetails()

        for item in self.ToD_listDetails():
            if mac in item['Key']:
                return item['Active'],item['Name'],item['IPAddress']

        return None


