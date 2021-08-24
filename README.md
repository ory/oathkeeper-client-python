# ory-oathkeeper-client
ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.0.0-alpha.57
- Package version: v0.0.0-alpha.57
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.ory.am](https://www.ory.am)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ory/sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ory/sdk.git`)

Then import the package:
```python
import ory_oathkeeper_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ory_oathkeeper_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ory_oathkeeper_client
from pprint import pprint
from ory_oathkeeper_client.api import api_api
from ory_oathkeeper_client.model.health_not_ready_status import HealthNotReadyStatus
from ory_oathkeeper_client.model.health_status import HealthStatus
from ory_oathkeeper_client.model.inline_response500 import InlineResponse500
from ory_oathkeeper_client.model.json_web_key_set import JsonWebKeySet
from ory_oathkeeper_client.model.rule import Rule
from ory_oathkeeper_client.model.version import Version
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_oathkeeper_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with ory_oathkeeper_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_api.ApiApi(api_client)
    
    try:
        # Access Control Decision API
        api_instance.decisions()
    except ory_oathkeeper_client.ApiException as e:
        print("Exception when calling ApiApi->decisions: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**decisions**](docs/ApiApi.md#decisions) | **GET** /decisions | Access Control Decision API
*ApiApi* | [**get_rule**](docs/ApiApi.md#get_rule) | **GET** /rules/{id} | Retrieve a rule
*ApiApi* | [**get_version**](docs/ApiApi.md#get_version) | **GET** /version | Get service version
*ApiApi* | [**get_well_known_json_web_keys**](docs/ApiApi.md#get_well_known_json_web_keys) | **GET** /.well-known/jwks.json | Lists cryptographic keys
*ApiApi* | [**is_instance_alive**](docs/ApiApi.md#is_instance_alive) | **GET** /health/alive | Check alive status
*ApiApi* | [**is_instance_ready**](docs/ApiApi.md#is_instance_ready) | **GET** /health/ready | Check readiness status
*ApiApi* | [**list_rules**](docs/ApiApi.md#list_rules) | **GET** /rules | List all rules


## Documentation For Models

 - [CreateRuleCreated](docs/CreateRuleCreated.md)
 - [CreateRuleForbidden](docs/CreateRuleForbidden.md)
 - [CreateRuleForbiddenBody](docs/CreateRuleForbiddenBody.md)
 - [CreateRuleInternalServerError](docs/CreateRuleInternalServerError.md)
 - [CreateRuleInternalServerErrorBody](docs/CreateRuleInternalServerErrorBody.md)
 - [CreateRuleUnauthorized](docs/CreateRuleUnauthorized.md)
 - [CreateRuleUnauthorizedBody](docs/CreateRuleUnauthorizedBody.md)
 - [DecisionsForbidden](docs/DecisionsForbidden.md)
 - [DecisionsForbiddenBody](docs/DecisionsForbiddenBody.md)
 - [DecisionsInternalServerError](docs/DecisionsInternalServerError.md)
 - [DecisionsInternalServerErrorBody](docs/DecisionsInternalServerErrorBody.md)
 - [DecisionsNotFound](docs/DecisionsNotFound.md)
 - [DecisionsNotFoundBody](docs/DecisionsNotFoundBody.md)
 - [DecisionsUnauthorized](docs/DecisionsUnauthorized.md)
 - [DecisionsUnauthorizedBody](docs/DecisionsUnauthorizedBody.md)
 - [DeleteRuleForbidden](docs/DeleteRuleForbidden.md)
 - [DeleteRuleForbiddenBody](docs/DeleteRuleForbiddenBody.md)
 - [DeleteRuleInternalServerError](docs/DeleteRuleInternalServerError.md)
 - [DeleteRuleInternalServerErrorBody](docs/DeleteRuleInternalServerErrorBody.md)
 - [DeleteRuleNotFound](docs/DeleteRuleNotFound.md)
 - [DeleteRuleNotFoundBody](docs/DeleteRuleNotFoundBody.md)
 - [DeleteRuleUnauthorized](docs/DeleteRuleUnauthorized.md)
 - [DeleteRuleUnauthorizedBody](docs/DeleteRuleUnauthorizedBody.md)
 - [GetRuleForbidden](docs/GetRuleForbidden.md)
 - [GetRuleForbiddenBody](docs/GetRuleForbiddenBody.md)
 - [GetRuleInternalServerError](docs/GetRuleInternalServerError.md)
 - [GetRuleInternalServerErrorBody](docs/GetRuleInternalServerErrorBody.md)
 - [GetRuleNotFound](docs/GetRuleNotFound.md)
 - [GetRuleNotFoundBody](docs/GetRuleNotFoundBody.md)
 - [GetRuleOK](docs/GetRuleOK.md)
 - [GetRuleUnauthorized](docs/GetRuleUnauthorized.md)
 - [GetRuleUnauthorizedBody](docs/GetRuleUnauthorizedBody.md)
 - [GetWellKnownForbidden](docs/GetWellKnownForbidden.md)
 - [GetWellKnownForbiddenBody](docs/GetWellKnownForbiddenBody.md)
 - [GetWellKnownJSONWebKeysInternalServerError](docs/GetWellKnownJSONWebKeysInternalServerError.md)
 - [GetWellKnownJSONWebKeysInternalServerErrorBody](docs/GetWellKnownJSONWebKeysInternalServerErrorBody.md)
 - [GetWellKnownJSONWebKeysOK](docs/GetWellKnownJSONWebKeysOK.md)
 - [GetWellKnownOK](docs/GetWellKnownOK.md)
 - [GetWellKnownUnauthorized](docs/GetWellKnownUnauthorized.md)
 - [GetWellKnownUnauthorizedBody](docs/GetWellKnownUnauthorizedBody.md)
 - [HealthNotReadyStatus](docs/HealthNotReadyStatus.md)
 - [HealthStatus](docs/HealthStatus.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [IsInstanceAliveInternalServerError](docs/IsInstanceAliveInternalServerError.md)
 - [IsInstanceAliveInternalServerErrorBody](docs/IsInstanceAliveInternalServerErrorBody.md)
 - [IsInstanceAliveOK](docs/IsInstanceAliveOK.md)
 - [JsonWebKey](docs/JsonWebKey.md)
 - [JsonWebKeySet](docs/JsonWebKeySet.md)
 - [JudgeForbidden](docs/JudgeForbidden.md)
 - [JudgeForbiddenBody](docs/JudgeForbiddenBody.md)
 - [JudgeInternalServerError](docs/JudgeInternalServerError.md)
 - [JudgeInternalServerErrorBody](docs/JudgeInternalServerErrorBody.md)
 - [JudgeNotFound](docs/JudgeNotFound.md)
 - [JudgeNotFoundBody](docs/JudgeNotFoundBody.md)
 - [JudgeUnauthorized](docs/JudgeUnauthorized.md)
 - [JudgeUnauthorizedBody](docs/JudgeUnauthorizedBody.md)
 - [ListRulesForbidden](docs/ListRulesForbidden.md)
 - [ListRulesForbiddenBody](docs/ListRulesForbiddenBody.md)
 - [ListRulesInternalServerError](docs/ListRulesInternalServerError.md)
 - [ListRulesInternalServerErrorBody](docs/ListRulesInternalServerErrorBody.md)
 - [ListRulesOK](docs/ListRulesOK.md)
 - [ListRulesUnauthorized](docs/ListRulesUnauthorized.md)
 - [ListRulesUnauthorizedBody](docs/ListRulesUnauthorizedBody.md)
 - [RawMessage](docs/RawMessage.md)
 - [Rule](docs/Rule.md)
 - [RuleHandler](docs/RuleHandler.md)
 - [RuleMatch](docs/RuleMatch.md)
 - [SwaggerCreateRuleParameters](docs/SwaggerCreateRuleParameters.md)
 - [SwaggerGetRuleParameters](docs/SwaggerGetRuleParameters.md)
 - [SwaggerHealthStatus](docs/SwaggerHealthStatus.md)
 - [SwaggerJSONWebKey](docs/SwaggerJSONWebKey.md)
 - [SwaggerJSONWebKeySet](docs/SwaggerJSONWebKeySet.md)
 - [SwaggerListRulesParameters](docs/SwaggerListRulesParameters.md)
 - [SwaggerNotReadyStatus](docs/SwaggerNotReadyStatus.md)
 - [SwaggerRule](docs/SwaggerRule.md)
 - [SwaggerRuleHandler](docs/SwaggerRuleHandler.md)
 - [SwaggerRuleMatch](docs/SwaggerRuleMatch.md)
 - [SwaggerRuleResponse](docs/SwaggerRuleResponse.md)
 - [SwaggerRulesResponse](docs/SwaggerRulesResponse.md)
 - [SwaggerUpdateRuleParameters](docs/SwaggerUpdateRuleParameters.md)
 - [SwaggerVersion](docs/SwaggerVersion.md)
 - [UpdateRuleForbidden](docs/UpdateRuleForbidden.md)
 - [UpdateRuleForbiddenBody](docs/UpdateRuleForbiddenBody.md)
 - [UpdateRuleInternalServerError](docs/UpdateRuleInternalServerError.md)
 - [UpdateRuleInternalServerErrorBody](docs/UpdateRuleInternalServerErrorBody.md)
 - [UpdateRuleNotFound](docs/UpdateRuleNotFound.md)
 - [UpdateRuleNotFoundBody](docs/UpdateRuleNotFoundBody.md)
 - [UpdateRuleOK](docs/UpdateRuleOK.md)
 - [UpdateRuleUnauthorized](docs/UpdateRuleUnauthorized.md)
 - [UpdateRuleUnauthorizedBody](docs/UpdateRuleUnauthorizedBody.md)
 - [Upstream](docs/Upstream.md)
 - [Version](docs/Version.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

hi@ory.am


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ory_oathkeeper_client.apis and ory_oathkeeper_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ory_oathkeeper_client.api.default_api import DefaultApi`
- `from ory_oathkeeper_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ory_oathkeeper_client
from ory_oathkeeper_client.apis import *
from ory_oathkeeper_client.models import *
```

