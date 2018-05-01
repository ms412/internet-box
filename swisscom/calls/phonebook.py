
import json
import swisscom.api.phonebook_api as phonebookApi

class Phonebook(phonebookApi.PhonebookApi):

    def __init__(self):
        print('Phonebook')

    def getPhonebook(self):
        print(self.Phonebook_getAllContacts())

        return True

    def addPhonebookEntry(self,contact):

        _r = self.Phonebook_addContactAndGenUUID(json.dumps(contact))
        uuid = _r.split(':')

        return uuid[2]

    def delPhonebookEntry(self,uuid):
        _uuid = 'urn:uuid:' + str(uuid)
        print('call',_uuid)
        print(self.Phonebook_removeContactByUniqueID(_uuid))
        return True


