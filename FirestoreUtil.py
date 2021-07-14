import requests

BASEURL = "http://192.168.1.60:8081/v1/projects/emulator-222e3/databases/(default)/documents"

class FirestoreUtil(object):

	@staticmethod
	def getDocument(path, id):
		reqRes = requests.get(url = BASEURL + path, headers = {"Authorization": f"Bearer {id}"})
		res = reqRes.json()
		if ("error" in res):
			# TODO: Give some indication to user.
			return
		
		return res

	@staticmethod
	def writeDocument(path, data, id, docId = None):
		reqRes = requests.post(url = BASEURL + path, json = data, params = {"documentId": docId}, headers = {"Authorization": f"Bearer {id}"})
		res = reqRes.json()
		if ("error" in res):
			# TODO: Give some indication to user.
			return
		
		return res

	@staticmethod
	def formatData(data):
		formattedData = {"fields": {}}
		for key in data.keys():
			formattedData["fields"][key] = {}
			formattedData["fields"][key]["stringValue"] = data[key]
		return formattedData