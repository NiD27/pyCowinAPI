### Python wrapper for the COWIN API.
<ul>
<li>Please refer the official website - https://apisetu.gov.in/public/api/cowin/cowin-public-v2 for API rules, limitations, official documentation and schemas.</li>
<li>Sandbox api-key provided by the official website is used by default, refer official website to obtain your own api-key.</li>
<li>This library is under development and certain features may be unstable, stay updated with the latest version.</li>
</ul>

### Classes
The official documentation of the api has been categorized into:
<ul>
<li>Co-WIN Public APIs</li>
<li>Co-WIN Protected APIs</li>
<li>Co-WIN Vaccinator APIs</li>
</ul>

### USAGE
- Requirements
```python
pip install -r requirements.txt
```
- Co-WIN Public APIs
```python
from cowinApi import cowinPublicApi
obj = cowinPublicApi()
#FOR PRODUCTION URL AND API-KEY
from cowinApi import cowinPublicApi
obj = cowinPublicApi(production = True, api_key_production = "INSERT_API_KEY_HERE")
```
- Co-WIN Protected APIs
```python
#FOR SANDBOX URL AND API-KEY
from cowinApi import cowinProtectedApi
obj = cowinProtectedApi()
#FOR PRODUCTION URL AND API-KEY
from cowinApi import cowinProtectedApi
obj = cowinProtectedApi(production = True, api_key_production = "INSERT_API_KEY_HERE")
```
- Co-WIN Vaccinator APIs
```python
#FOR SANDBOX URL AND API-KEY
from cowinApi import cowinVaccinatorApi
obj = cowinVaccinatorApi()
#FOR PRODUCTION URL AND API-KEY
from cowinApi import cowinVaccinatorApi
obj = cowinVaccinatorApi(production = True, api_key_production = "INSERT_API_KEY_HERE")
```

### ROADMAP
<ul>
<li>Fake User Agent implementation.</li>
<li>Rate limiting/monitoring.</li>
<li>Request timeouts.</li>
<li>Testing and stabalization of unstable functions.</li>
<li>ASYNCIO version.</li>
</ul>

### DISCLAIMER
<ul>
<li>I am in no way affiliated with COWIN API.</li>
<li>Use this library at your own risk, I or any contributors to this library are not responsible for any damages caused.</li>
</ul>