import subprocess
import httplib
import json
import pytest
from collections import Counter

class TestClass:
    def setup_method(self,method):
        print ("*******Setting up***************\n")
        subprocess.call(['./install.sh'])

    def test_foglamp(self):
        print ("Validating if FogLAMP is up ....")

        #init_val = {'uptime': 17762, 'safeMode': False, 'dataSent': 0, 'hostName': 'localhost.localdomain', 'dataRead': 0, 'serviceName': 'FogLAMP', 'health': 'green', 'ipAddresses': ['192.168.1.140'], 'dataPurged': 0, 'authenticationOptional': True }

        key = ["uptime","safeMode","dataSent","hostName","dataRead","serviceName","health","ipAddresses","dataPurged","authenticationOptional"]
        value = [1,False,0,'localhost.localdomain',0,'FogLAMP','green',['192.168.1.140'],0,True]

        con=httplib.HTTPConnection("192.168.1.140:8081")
        con.request("GET", "/foglamp/ping")
        resp=con.getresponse()
        strdata=resp.read().decode()
        data=json.loads(strdata)

        assert Counter(data.keys()) == Counter(key)

        for i in range(len(key)):
            assert data[key[i]] >= value[i]

    def teardown_method(self,method):
        print ("\n********Tearing down********")
        subprocess.call(['./uninstall.sh'])
