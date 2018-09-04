

import json
import swisscom.api.UserManagement_api as UserManagementApi

class UserManagement(UserManagementApi.UserManagementApi):

    def __init__(self):
        print('UserManagement')

    def getUserLog(self):

        return self.UserManagement_getUserLog()

    def test123(self):
        return self.Test_test()

    def test1234(self):
        return self.Test_test1()


