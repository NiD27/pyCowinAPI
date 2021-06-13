from .requestsHandler import __requests_handler
from .utils import func_args_processor, generate_sha256

class cowinProtectedApi(__requests_handler):

    API_KEY_SANDBOX = "3sjOr2rmM52GzhpMHjDEE1kpQeRxwFDr4YcBEimi"
    API_BASE_SANDBOX_URL = "https://cdndemo-api.co-vin.in/api"
    API_BASE_PRODUCTION_URL = "https://cdn-api.co-vin.in/api"
    BASE_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36", "Content-Type": "application/json"
    }
    BASE_PARAMS = {"Accept-Language": "en_IN"}

    """
    production = False by default this enables sandbox mode,
    if you need production mode please turn production = True and also set api_key_production
    """
    def __init__(self, api_key_sandbox = API_KEY_SANDBOX, api_base_sandbox_url = API_BASE_SANDBOX_URL, api_base_production_url = API_BASE_PRODUCTION_URL,
                 base_headers = BASE_HEADERS, base_params = BASE_PARAMS, production = False, api_key_production = None):
        self.api_key = api_key_sandbox
        self.api_base_url = api_base_sandbox_url
        if production and api_key_production:
            self.api_key = api_key_production
            self.api_base_url = api_base_production_url
        self.base_headers = base_headers
        self.base_headers["x-api-key"] = self.api_key
        self.base_params = base_params
        self.request_timeout = 120

    #? START USER AUTHENTICATION API's

    """generate_OTP - requires a 10 digit mobile number (without the country code) and posts a OTP request  and the response contains a txnId"""
    @func_args_processor
    def generate_OTP(self, mobile):
        api_url = f"{self.api_base_url}/v2/auth/generateOTP"
        params = self.base_params
        params["mobile"] = mobile
        return self.request_post(api_url, self.base_headers, params)
    
    """
    confirm_OTP - requires a txnId which is returned by the generate_OTP functions and also requires a SHA-256 hash of the received OTP. Hash function provided in utils.py.
    If success the response is a token
    """
    @func_args_processor
    def confirm_OTP(self, txnId, otp):
        api_url = f"{self.api_base_url}/v2/auth/confirmOTP"
        params = self.base_params
        params["txnId"] = txnId
        params["otp"] = generate_sha256(otp)
        return self.request_post(api_url, self.base_headers, params)

    #? END USER AUTHENTICATION API's
    #------------------------------------------------------------------#
    #? START METADATA API's
    """
    Returns the list of beneficiary id types
    """
    @func_args_processor
    def get_beneficiary_id_types(self):
        api_url = f"{self.api_base_url}/v2/registration/beneficiary/idTypes"
        return self.request_get(api_url, self.base_headers, self.base_params)

    """
    Returns the list of beneficiary genders
    """
    @func_args_processor
    def get_beneficiary_gender(self):
        api_url = f"{self.api_base_url}/v2/registration/beneficiary/genders"
        return self.request_get(api_url, self.base_headers, self.base_params)

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

    """
    Returns centers by lattitude and longitude
    """
    @func_args_processor
    def get_centers_by_lat_long(self):
        api_url = f"{self.api_base_url}/v2/registration/beneficiary/genders"
        return self.request_get(api_url, self.base_headers, self.base_params)

    #? END METADATA API's
    #------------------------------------------------------------------#
    #? START BENEFICIARY REGISTRATION API's
    
    """
    Requires [name, birth_year, gender_id, photo_id_type, photo_id_number, comorbidity_ind, consent_version]
    Returns a 'benediciary_reference_id'
    """
    @func_args_processor
    def beneficiary_new(self, **kwargs):
        api_url = f"{self.api_base_url}/v2/registration/beneficiary/new"
        params = self.base_params
        params.update(kwargs)
        return self.request_post(api_url, self.base_headers, params)
    
    """
    Requires [beneficiary_reference_id]
    response - 204 the beneficiary was deleted successfully
    """
    @func_args_processor
    def beneficiaty_delete(self, beneficiary_reference_id):
        api_url = f"{self.api_base_url}​/v2​/registration​/beneficiary​/delete"
        params = self.base_params
        params["beneficiary_reference_id"] = beneficiary_reference_id
        return self.request_post(api_url, self.base_headers, params)

    #? END BENEFICIARY REGISTRATION API's
    #------------------------------------------------------------------#
    #? START VACCINATION APPOINTMENT API's

    """
    findByPin, findByDistrict are currently under debugging process seems that official documentation may be inaccurate please use calendar_by_xyz instead
    """
    #TODO: OPTIONAL VACCINE PARAM
    @func_args_processor
    def calendar_by_pin(self, pincode, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/calendarByPin"
        params = self.base_params
        params["pincode"] = pincode
        params["date"] = date
        return self.request_get(api_url, self.base_headers, params)
    #TODO: OPTIONAL VACCINE PARAM
    @func_args_processor
    def calendar_by_district(self, district_id, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/calendarByDistrict"
        params = self.base_params
        params["district_id"] = district_id
        params["date"] = date
        return self.request_get(api_url, self.base_headers, params)
    
    @func_args_processor
    def get_beneficiaries(self):
        api_url = f"{self.api_base_url}/v2/appointment/beneficiaries"
        params = self.base_params
        return self.request_get(api_url, self.base_headers, params)
    
    @func_args_processor
    def appointment_schedule(self, dose, session_id, slot, beneficiaries = []):
        api_url = f"{self.api_base_url}/v2/appointment/schedule"
        params = self.base_params
        params["dose"] = dose
        params["session_id"] = session_id
        params["slot"] = slot
        params["benediciaries"] = beneficiaries
        return self.request_post(api_url, self.base_headers, params)
    
    @func_args_processor
    def appointment_reschedule(self, appointment_id, session_id, slot):
        api_url = f"{self.api_base_url}/v2/appointment/reschedule"
        params = self.base_params
        params["appointment_id"] = appointment_id
        params["session_id"] = session_id
        params["slot"] = slot
        return self.request_post(api_url, self.base_headers, params)

    @func_args_processor
    def appointment_cancel(self, appointment_id, beneficiariesToCancel = []):
        api_url = f"{self.api_base_url}/v2/appointment/cancel"
        params = self.base_params
        params["appointment_id"] = appointment_id
        params["benediciariesToCancel"] = beneficiariesToCancel
        return self.request_post(api_url, self.base_headers, params)

    #? END VACCINATION APPOINTMENT API's
    #------------------------------------------------------------------#
    #? START CERTIFICATE API's

    """
    ALERT - This function returns the binary content of PDF file write your own code to create a .pdf
    """
    def certificate_download(self, beneficiary_reference_id):
        api_url = f"{self.api_base_url}/v2/registration/certificate/download"
        params = self.base_params
        params["beneficiary_reference_id"] = beneficiary_reference_id
        return self.request_get(api_url, self.base_headers, params)

    """
    ALERT - This function returns the binary content of PDF file write your own code to create a .pdf
    """
    def appointment_slip_download(self, appointment_id):
        api_url = f"{self.api_base_url}​/v2​/appointment​/appointmentslip​/download"
        params = self.base_params
        params["appointment_id"] = appointment_id
        return self.request_get(api_url, self.base_headers, params)

    #? END CERTIFICATE API's