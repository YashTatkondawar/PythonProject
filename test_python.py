import subprocess
import httplib
import json
import pytest

def install_foglamp():

	subprocess.call(['./install.sh'])


def test_foglamp():
	print ("Validating if FogLAMP is up ....")

	#init_val = {'uptime': 17762, 'safeMode': False, 'dataSent': 0, 'hostName': 'localhost.localdomain', 'dataRead': 0, 'serviceName': 'FogLAMP', 'health': 'green', 'ipAddresses': ['192.168.1.140'], 'dataPurged': 0, 'authenticationOptional': True }

	key = ["safeMode","dataSent","hostName","dataRead","serviceName","health","dataPurged","authenticationOptional"]
	value = [False,0,'localhost.localdomain',0,'FogLAMP','green',0,True]

	con=httplib.HTTPConnection("192.168.1.140:8081")
	con.request("GET", "/foglamp/ping")
	resp=con.getresponse()
	strdata=resp.read().decode()
	data=json.loads(strdata)
	
	for i in range(len(key)):	   
	   assert data[key[i]] == value[i]
	
def main():	
	install_foglamp()
	test_foglamp()
	print ("FogLAMP installation and validation complete")

	
if __name__ == "__main__":
	main()
