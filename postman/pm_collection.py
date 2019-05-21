import re

def collection_header():
    co_header =  '''
{
	"info": {
		"name": "test",
		"_postman_id": "e61529df-a10b-69e0-7e49-56647667624a",
		"description": "",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
        	{
			"name": "login",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\\"aaaUser\\" : { \\"attributes\\": {\\"name\\":\\"admin\\",\\"pwd\\":\\"C1sco12345\\" } } } "
				},
				"url": {
					"raw": "https://198.18.133.200/api/aaaLogin.json",
					"protocol": "https",
					"host": [
						"198",
						"18",
						"133",
						"200"
					],
					"path": [
						"api",
						"aaaLogin.json"
					]
				},
				"description": "login"
			},
			"response": []
		},
    '''
    return co_header

def rest_header(n):
    reg_name = "req_" + str(n)
    re_header =  '''
		{
			"name": "%s",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/xml"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "
    ''' % reg_name

    return re_header

def rest_tail():
    re_tail  =  '''"
				},
				"url": {
					"raw": "https://198.18.133.200/api/mo/uni.json",
					"protocol": "https",
					"host": [
						"198",
						"18",
						"133",
						"200"
					],
					"path": [
						"api",
						"mo",
						"uni.json"
					]
				},
				"description": ""
			},
			"response": []
		}
    '''
    return re_tail


def aci_json_correction(*args):
    data = ""
    for file_name in args:
        fl = open(file_name, "r")
        data = data + rest_header(file_name) + fl.read() + "}}}"
        fl.close()
    
    collction = collection_header() + data + rest_tail()
    

    return collction

print aci_json_correction ("/home/nihole/python_test/test1", "/home/nihole/python_test/test2")
