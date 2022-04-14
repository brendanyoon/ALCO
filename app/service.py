#from rest_framework import requests

#File to store all the API calls to external applications
str: blackboard_base_url = 'https://blackboard.umbc.edu'
str: blackboard_oauth_API = '/learn/api/public/v1/oauth/authorizationcode'
str: dummy_param = {
    "redirect_uri": "http://localhost:8000/prof-dashboard/",
    "response_type" : "code",
    "client_id": "7f96fb30-e5ba-495d-a962-ed5f1ad0c52e",
    "scope" : "read write",
    "state" : 
    
    }
   
#def blackboard_auth():
#    str: oauth_request_url = blackboard_base_url + blackboard_oauth_API
#    request_to_blackboard = requests.get(url, params=dummy_params)
#    final_request_format = request_to_blackboard.json()
