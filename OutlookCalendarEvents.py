from msal import PublicClientApplication
import requests
import uuid
import json

client_id = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX'  # Or App Id from Portal Azure 
client_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
directory_id = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX'  # Also known as: tenant
authority = 'https://login.microsoftonline.com/' + directory_id
username = 'your_email_id@someDomain.com'   # Office365/Outlook Email account
result = None
graph_endpoint = 'https://graph.microsoft.com/v1.0{0}'

app = PublicClientApplication(client_id, client_credential=None, authority=authority)

# We now check the cache to see
# whether we already have some accounts that the end user already used to sign in before.
accounts = app.get_accounts()
if accounts:
    result = app.acquire_token_silent(config["scope"], account=username)

if not result:
    # So no suitable token exists in cache. Let's get a new one from AAD.
    flow = app.initiate_device_flow(scopes=["User.Read", "Calendars.Read"])
    print(flow)
    result = app.acquire_token_by_device_flow(flow)

if "access_token" in result:
    print(result["access_token"])  # Yay!
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))  # You may need this when reporting a bug


# Generic API Sending
def make_api_call(method, url, token, payload=None, parameters=None):
    # Send these headers with all API calls
    headers = {'User-Agent': 'python_tutorial/1.0',
               'Authorization': 'Bearer {0}'.format(token),
               'Accept': 'application/json'}

    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id': request_id,
                       'return-client-request-id': 'true'}
    headers.update(instrumentation)
    response = None
    if (method.upper() == 'GET'):
        response = requests.get(url, headers=headers, params=parameters)
    elif (method.upper() == 'DELETE'):
        response = requests.delete(url, headers=headers, params=parameters)
    elif (method.upper() == 'PATCH'):
        headers.update({'Content-Type': 'application/json'})
        response = requests.patch(url, headers=headers, data=json.dumps(payload), params=parameters)
    elif (method.upper() == 'POST'):
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url, headers=headers, data=json.dumps(payload), params=parameters)
    return response


def get_my_events(access_token):
    get_events_url = graph_endpoint.format('/me/events')

    # Use OData query parameters to control the results
    #  - Only first 10 results returned
    #  - Only return the Subject, Start, and End fields
    #  - Sort the results by the Start field in ascending order
    query_parameters = {'$top': '10',
                        '$select': 'subject,start,end',
                        '$orderby': 'start/dateTime ASC'}

    r = make_api_call('GET', get_events_url, access_token, parameters=query_parameters)

    if (r.status_code == requests.codes.ok):
        return r.json()
    else:
        return "{0}: {1}".format(r.status_code, r.text)

print("--------------------------------------------------------------")
events = get_my_events(result["access_token"])
print(events)
