from .requestsHandler import __requests_handler
from .utils import func_args_processor, generate_sha256
from .cowinApi import cowinApi

class cowinPublicApi(__requests_handler, cowinApi):

    """
    production = False by default this enables sandbox mode,
    if you need production mode please turn production = True and also set api_key_production
    """
    def __init__(self, api_key_sandbox = cowinApi.API_KEY_SANDBOX, api_base_sandbox_url = cowinApi.API_BASE_SANDBOX_URL, api_base_production_url = cowinApi.API_BASE_PRODUCTION_URL,
                 base_headers = cowinApi.BASE_HEADERS, base_params = cowinApi.BASE_PARAMS, production = False, api_key_production = None, vaccines = cowinApi.VACCINES):
        self.api_key = api_key_sandbox
        self.api_base_url = api_base_sandbox_url
        if production and api_key_production:
            self.api_key = api_key_production
            self.api_base_url = api_base_production_url
        self.base_headers = base_headers
        self.base_headers["x-api-key"] = self.api_key
        self.base_params = base_params
        self.vaccines = vaccines
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
    #------------------------------------------------------------------#
    #? START METADATA API's
    """
    Returns the id's of all states and the id's of districts in a specified state
    """
    @func_args_processor 
    def get_states(self):
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
        api_url += params["state_id"]
        return self.request_get(api_url, self.base_headers, params)

    #? END METADATA API's
    #------------------------------------------------------------------#
    #? START APPOINTMENT API's
    """
    findByPin, findByDistrict, findByLatLong are currently under debugging process seems that official documentation may be inaccurate please use calendar_by_xyz instead
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