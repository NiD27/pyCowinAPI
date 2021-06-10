# import json
# import requests

# from requests.exceptions import RequestException
# from json.decoder import JSONDecodeError

from .requestsHandler import __requests_handler
from .utils import func_args_processor, generate_sha256

class cowinPublicAPI(__requests_handler):
    API_BASE_URL = "https://cdn-api.co-vin.in/api"
    BASE_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36", "Content-Type": "application/json"}
    BASE_PARAMS = {"Accept-Language": "en_IN"}

    def __init__(self, api_base_url = API_BASE_URL, base_headers = BASE_HEADERS, base_params = BASE_PARAMS):
        self.api_base_url = api_base_url
        self.base_headers = base_headers
        self.base_params = base_params
        self.request_timeout = 120

    #? START USER AUTHENTICATION API's

    """generate_OTP - requires a 10 digit mobile number (without the country code) and posts a OTP request  and the response contains a txnId"""
    @func_args_processor
    def generate_OTP(self, mobile):
        api_url = f"{self.api_base_url}/v2/auth/public/generateOTP"
        params = self.base_params
        params["mobile"] = mobile
        return self.request_post(api_url, self.base_headers, params)
    
    """
    confirm_OTP - requires a txnId which is returned by the generate_OTP functions and also requires a SHA-256 hash of the received OTP. Hash function provided in utils.py.
    If success the response is a token
    """
    @func_args_processor
    def confirm_OTP(self, txnId, otp):
        api_url = f"{self.api_base_url}/v2/auth/public/confirmOTP"
        params = self.base_params
        params["txnId"] = txnId
        params["otp"] = generate_sha256(otp)
        return self.request_post(api_url, self.base_headers, params)

    #? END USER AUTHENTICATION API's


    #? START METADATA API's
    """
    Returns the id's of all states and the id's of districts in a specified state
    """
    @func_args_processor 
    def get_states(self):
        # api_url = f"{self.api_base_url}/v2/admin/location/states"
        api_url = f"{self.api_base_url}/v2/admin/location/states"
        return self.request_get(api_url, self.base_headers, self.base_params)
    
    """
    The state_id needs to be appended to the url as well as sent as a parameter, when sent only as a parameter it returns 403 - Unauthorized URL
    """
    @func_args_processor
    def get_districts(self, state_id):
        api_url = f"{self.api_base_url}/v2/admin/location/districts/"
        params = self.base_params
        params["state_id"] = state_id
        # payload.update(self.BASE_PAYLOAD)
        api_url += params["state_id"]
        return self.request_get(api_url, self.base_headers, params)

    #? END METADATA API's
    #------------------------------------------------------------------#
    #? START APPOINTMENT API's
    """
    findByPin, findByDistrict, findByLatLong are current under debugging process seems that official documentation may be inaccurate please use calendar_by_xyz instead
    """
    @func_args_processor
    def calendar_by_pin(self, pincode, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/public/calendarByPin"
        params = self.base_params
        params["pincode"] = pincode
        params["date"] = date
        return self.request_get(api_url, self.base_headers, params)

    @func_args_processor
    def calendar_by_district(self, district_id, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/public/calendarByDistrict"
        params = self.base_params
        params["district_id"] = district_id
        params["date"] = date
        return self.request_get(api_url, self.base_headers, params)

    @func_args_processor
    def calendar_by_center(self, center_id, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/public/calendarByCenter"
        params = self.base_params
        params["center_id"] = center_id
        params["date"] = date
        return self.request_get(api_url, self.base_headers, params)

    #? END APPOINTMENT API's
    #------------------------------------------------------------------#
    #? START CERTIFICATE API's
    """
    ALERT - This function returns the binary content of PDF file write your own code to create a .pdf
    """
    def certificate_download(self, beneficiary_reference_id):
        api_url = f"{self.api_base_url}/v2/registration/certificate/public/download"
        params = self.base_params
        params["beneficiary_reference_id"] = beneficiary_reference_id
        return self.request_get(api_url, self.base_headers, params)

    #? END CERTIFICATE API's