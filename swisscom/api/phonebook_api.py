import json
import swisscom.base.ibox_base as ibox

class PhonebookApi(ibox.IboxBase):

    def __init__(self):
        print('PhonebookApi')

    def Phonebook_getAllContacts(self):
        r = self._session.post(self._url + 'sysbus/Phonebook:getAllContacts',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('Phonebook_getAllContacts %s' % r.text)
        return r.json()['result']['status']

    def Phonebook_addContactAndGenUUID(self,data):
        #_jdata = json.load(data)
        r = self._session.post(self._url + 'sysbus/Phonebook:addContactAndGenUUID',
                               headers=self._sah_headers,
                               data='{"parameters":{"contact": %s}}'% data)
        self._log.debug('Phonebook_addContactAndGenUUID %s' % r.text)
        return r.json()['result']['status']

    def Phonebook_removeContactByUniqueID(self,uuid):
        print(uuid)
        r = self._session.post(self._url + 'sysbus/Phonebook:removeContactByUniqueID',
                               headers=self._sah_headers,
                               data='{"parameters":{"uniqueID": "%s"}}'% (uuid))
                            #   data={"parameters": {"uniqueID": "urn:uuid:1f858f37-8576-438f-b2d3-3454ca810910","contact": {"name": "N:famielyname;firstname", "formattedName": "famielyname firstname","telephoneNumbers": [{"name": "123567", "type": "HOME", "preferred": False},{"name": "5668", "type": "CELL", "preferred": False}]}}})
        self._log.debug('Phonebook_removeContactByUniqueID %s' % r.text)
        return r.json()['result']['status']

    def PhonebookBackup_get(self):
        r = self._session.post(self._url + 'sysbus/NMC/PhonebookBackup:get',
                               headers=self._sah_headers,
                               data='{"parameters":{}}')
        self._log.debug('PhonebookBackup_get %s' % r.text)
        return r.json()['result']['status']