import json
import requests

from .utils import func_args_processor

class cowinAPI:
    __API_BASE_URL = "https://cdn-api.co-vin.in/api"
    __BASE_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"}
    __BASE_PARAMS = {"Accept-Language": "en_IN"}

    def __init__(self, api_base_url = __API_BASE_URL, base_headers = __BASE_HEADERS, base_params = __BASE_PARAMS):
        self.api_base_url = api_base_url
        self.base_headers = base_headers
        self.base_params = base_params
        self.request_timeout = 120

    def __request_get(self, url, headers, params):
        try:
            response = requests.get(url, headers = headers, params = params)
        except requests.exceptions.RequestException:
            raise

        try:
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            # Check if JSON (with error messages) is returned
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise valueError(content)
            # If no JSON
            except json.decoder.JSONDecodeError:
                pass

            raise
    
    #? START METADATA API's

    @func_args_processor 
    def get_states(self):
        # api_url = f"{self.api_base_url}/v2/admin/location/states"
        api_url = f"{self.api_base_url}/v2/admin/location/states"
        return self.__request_get(api_url, self.base_headers, self.base_params)
    
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
        return self.__request_get(api_url, self.base_headers, params)

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
        return self.__request_get(api_url, self.base_headers, params)

    @func_args_processor
    def calendar_by_district(self, district_id, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/public/calendarByDistrict"
        params = self.base_params
        params["district_id"] = district_id
        params["date"] = date
        return self.__request_get(api_url, self.base_headers, params)

    @func_args_processor
    def calendar_by_center(self, center_id, date):
        api_url = f"{self.api_base_url}/v2/appointment/sessions/public/calendarByCenter"
        params = self.base_params
        params["center_id"] = center_id
        params["date"] = date
        return self.__request_get(api_url, self.base_headers, params)

    #? END APPOINTMENT API's