from .requestsHandler import __requests_handler
from .utils import func_args_processor, generate_sha256
from .cowinApi import cowinApi

class cowinVaccinatorApi(__requests_handler, cowinApi):

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

    #? START BENEFICIARY API's
    
    """
    Requires [name, birth_year, gender_id, photo_id_type, photo_id_number, comorbidity_ind, consent_version]
    Returns a 'benediciary_reference_id'
    """
    @func_args_processor
    def beneficiary_new(self, **kwargs):
        api_url = f"{self.api_base_url}/v2/vaccinator/beneficiaries/new"
        params = self.base_params
        params.update(kwargs)
        return self.request_post(api_url, self.base_headers, params)
    
    @func_args_processor
    def find_by_reference_id(self, beneficiary_reference_id):
            api_url = f"{self.api_base_url}​/v2/vaccinator/beneficiaries/findByReferenceId"
            params = self.base_params
            params["beneficiary_reference_id"] = beneficiary_reference_id
            return self.request_get(api_url, self.base_headers, params)

    @func_args_processor
    def find_by_mobile(self, mobile_number):
            api_url = f"{self.api_base_url}​​/v2​/vaccinator​/beneficiaries​/findByMobile"
            params = self.base_params
            params["mobile_number"] = mobile_number
            return self.request_get(api_url, self.base_headers, params)

    #? END BENEFICIARY API's
    #------------------------------------------------------------------#
    #? START VACCINATION API's

    """
    Create an appointment for onspot vaccination session.
    Requires : ["beneficiary_reference_id","center_id","vaccine","vaccine_batch","dose","dose1_date","dose2_date","vaccinator_name"]
    """
    @func_args_processor
    def appointment_schedule(self, **kwargs):
        api_url = f"{self.api_base_url}/v2/vaccinator/onspots/schedule"
        params = self.base_params
        params.update(kwargs)
        return self.request_post(api_url, self.base_headers, params)
    
    """
    Update beneficiary record with vaccination details.
    """
    @func_args_processor
    def beneficiaries_vaccinate(self, dose, session_id, slot, beneficiaries = []):
        api_url = f"{self.api_base_url}/v2/vaccinator/onspots/schedule"
        params = self.base_params
        params["dose"] = dose
        params["session_id"] = session_id
        params["slot"] = slot
        params["benediciaries"] = beneficiaries
        return self.request_post(api_url, self.base_headers, params)

    #? END VACCINATION API's
    #------------------------------------------------------------------#
    #? START CERTIFICATE API's

    """
    ALERT - This function returns the binary content of PDF file write your own code to create a .pdf
    """
    @func_args_processor
    def certificate_download(self, beneficiary_reference_id):
        api_url = f"{self.api_base_url}​/v2​/vaccinator​/certificate​/download"
        params = self.base_params
        params["beneficiary_reference_id"] = beneficiary_reference_id
        return self.request_get(api_url, self.base_headers, params)

    #? END CERTIFICATE API's