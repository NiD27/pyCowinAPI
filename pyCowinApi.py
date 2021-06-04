import requests
import pprint as pp

class cowinAPI():

    API_BASE_URI = "https://cdn-api.co-vin.in/api"
    HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    # TEST_HEADER = {'User-Agent': 'cowinalertstestappv1'}
    BASE_PAYLOAD = {
            "Accept-Language": "en_IN"
        }

    def __init__(self):
        pass

#? USER AUTHENTICATION APIs
    def generateOTP(self, phone_number):
        URL = self.API_BASE_URI+"/v2/auth/public/generateOTP"
        params = {
            "mobile": phone_number
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    
    def generateOTP(self, otp, txnId):
        URL = self.API_BASE_URI+"/v2/auth/public/generateOTP"
        params = {
            "otp" : otp,
            "txnId": txnId
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
#? METADATA APIs
    def getStates(self):
        URL = self.API_BASE_URI+"/v2/admin/location/states"
        params = {
            "Accept-Language": "en_IN"
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result

    def getDistricts(self, state_id):
        URL = self.API_BASE_URI+"/v2/admin/location/districts/"
        params = {
            "Accept-Language": "en_IN",
            "state_id" : state_id
        }
        # payload.update(self.BASE_PAYLOAD)
        URL += params["state_id"]
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result

#? APPOINTMENT AVAILABILITY APIs
    def findByPin(self, pincode, date):
        URL = self.API_BASE_URI+"/v2/appointment/sessions/public/calendarByPin"
        params = {
            "Accept-Language": "en_IN",
            "pincode" : pincode,
            "date" : date
        }
        result = requests.get(URL, headers=self.HEADER, params = params)

        return result

    #!200 BUT NO DATA or {'errorCode': 'USRRES0001', 'error': 'Input parameter missing'}
    def findByDistrict(self, district_id, date):
        URL = self.API_BASE_URI+"/v2/appointment/sessions/public/findByPin"
        params = {
            "Accept-Language": "en_IN",
            "district_id" : district_id,
            "date" : date
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    
    #!401
    #* API WEBSITE STATES THAT THIS IS A DRAFT SPECIFICATION
    def findByLatLong(self, lat, long):
        URL = self.API_BASE_URI+"/v2/appointment/centers/public/findByLatLong"
        params = {
            "Accept-Language": "en_IN",
            "lat" : lat,
            "long" : long
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    
    def calendarByPin(self, pincode, date):
        URL = self.API_BASE_URI+"/v2/appointment/sessions/public/calendarByPin"
        params = {
            "Accept-Language": "en_IN",
            "pincode" : pincode,
            "date" : date
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    
    def calendarByDistrict(self, district_id, date):
        URL = self.API_BASE_URI+"/v2/appointment/sessions/public/calendarByDistrict"
        params = {
            "Accept-Language": "en_IN",
            "district_id" : district_id,
            "date" : date
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    
    def calenderByCenter(self, center_id, date):
        URL = self.API_BASE_URI+"/v2/appointment/sessions/public/calendarByDistrict"
        params = {
            "Accept-Language": "en_IN",
            "center_id" : center_id,
            "date" : date
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    
    #************************************************************************#
#? CERTIFICATE APIs
    #? fetches binary data of the pdf
    def downloadCertificate(self, beneficiary_reference_id):
        URL = self.API_BASE_URI+"/v2/registration/certificate/public/download"
        params = {
            "beneficiary_reference_id" : beneficiary_reference_id
        }
        result = requests.get(URL, headers=self.HEADER, params = params)
        return result
    #************************************************************************#