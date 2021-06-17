class cowinApi:

    API_KEY_SANDBOX = "3sjOr2rmM52GzhpMHjDEE1kpQeRxwFDr4YcBEimi"
    API_BASE_SANDBOX_URL = "https://cdndemo-api.co-vin.in/api"
    API_BASE_PRODUCTION_URL = "https://cdn-api.co-vin.in/api"
    #? The below url is provided in the home page when none of the 3 categories are selected
    # API_BASE_PRODUCTION_URL = "https://api.sit.co-vin.in/api"
    BASE_HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36", "Content-Type": "application/json"
    }
    BASE_PARAMS = {"Accept-Language": "en_IN"}
    VACCINES = {
                "COVAXIN" : "COVAXIN",
                "COVISHIELD" : "COVISHIELD",
                "SPUTNIK_V" : "SPUTNIK V"
            }