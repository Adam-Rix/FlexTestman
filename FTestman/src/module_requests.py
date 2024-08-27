import json
import requests

# load out json-APIs links
def load_data_api(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# return the link which u need
def get_link(server_name,
             function_name,
             link_index,
             link_to_json):

    data_api = load_data_api(link_to_json)

    server = data_api['servers'].get(server_name, {})
    functions = server.get('functions', {})
    links = functions.get(function_name, [])

    if 0 <= link_index < len(links):
        return links[link_index]
    else:
        return None

def load_data_payload(payload):
    return json.loads(payload) if payload else {}

def load_header(file_path):
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

# send the request ## params is smth add for url about ?key1=value1&key2=value2 or something similar
def send_request(api_url, payload=None,
                 headers_data=None,
                 request_type='POST',
                 retries=3):

    for attempt in range(retries):

        try:
            payload_data = load_data_payload(payload)

            headers = headers_data if headers_data else {}

            # print(f"Sending {request_type} request to {api_url}")
            # print(f"Payload Data: {payload_data}")
            # print(f"Headers: {headers}")

            # Определение типа запроса
            match request_type:
                case "GET":
                    response = requests.get(api_url,
                                            params=payload_data,
                                            headers=headers)
                case "POST":
                    response = requests.post(api_url,
                                             json=payload_data,
                                             headers=headers)
                case "PUT":
                     response = requests.put(api_url,
                                             json=payload_data,
                                             headers=headers)
                case "PATCH":
                     response = requests.patch(api_url,
                                               json=payload_data,
                                               headers=headers)

                case _:
                     raise ValueError(f"Unsupported request type: {request_type}")

            # Обработка ответа
            # response = requests.post(api_url,
            #                          json=payload_data,
            #                          headers=headers_data)

            match response.status_code:

                ## Status: 1xx
                case 100:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Continue: The initial part of the request has been received, and the client should continue with the request."
                case 101:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Switching Protocols: The server is switching protocols as requested by the client."
                case 102:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Processing: The request has been received, and processing is continuing."
                case 103:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Early Hints: The server is sending preliminary information about the final response."

                ## Status: 2xx
                case 200:
                    output = f"{response.status_code} {response.text}\nSuccess: {response.json()}"

                case 201:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Created: Resource was successfully created."
                case 202:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Accepted: Request has been accepted for processing, but the processing has not been completed."
                case 203:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Non-Authoritative Information: The returned information is not authoritative."
                case 204:
                    output = f"{response.status_code} - {response.text}\n" \
                          "No Content: The request was successful, but there is no content to return."
                case 205:
                    output = f"{response.status_code} - {response.text}\n" \
                          "Reset Content: The request was successful, and the client should reset the document view."

                ## Status: 3xx
                case 300:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Multiple Choices: There are multiple options for the resource."
                case 301:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Moved Permanently: The resource has been moved permanently to a new URL."
                case 302:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Found: The resource is temporarily available at a different URL."
                case 303:
                    output = f"{response.status_code} - {response.text}\n" \
                             "See Other: The response to the request can be found at a different URL."
                case 304:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Not Modified: The resource has not been modified since the last request."
                case 305:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Use Proxy: The resource must be accessed through the specified proxy."

                ## Status: 4xx
                case 400:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Bad Request: The request could not be understood or was missing required parameters."\
                                "U need check the server and if it's ok - U have a problem with creds/request!"
                case 401:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Unauthorized: Authentication is required or has failed."\
                                "U have a problem with creds!"
                case 402:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Payment Required: Reserved for future use."
                case 403:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Forbidden: The server understood the request, but refuses to authorize it."
                case 404:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Not Found: The requested resource could not be found."
                case 405:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Method Not Allowed: The request method is not supported for the resource."

                ## Status: 5xx
                case 500:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Internal Server Error: The server encountered an unexpected condition." \
                                " Ask backs or your Tech-lead"

                case 501:
                    output = f"{response.status_code} - {response.text}\n" \
                            "Not Implemented: The server does not support the functionality required to fulfill the request."\
                                "Ask backs or your Tech-lead"
                case 502:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Bad Gateway: The server received an invalid response from an upstream server."\
                                "Ask your Tech-lead"
                case 503:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Service Unavailable: The server is currently unable to handle the request due to temporary overloading or maintenance."\
                                "Ask your Tech-lead"
                case 504:
                    output = f"{response.status_code} - {response.text}\n" \
                             "Gateway Timeout: The server did not receive a timely response from an upstream server."\
                                "Ask your Tech-lead"
                case 505:
                    output = f"{response.status_code} - {response.text}\n" \
                             "HTTP Version Not Supported: The server does not support the HTTP protocol version used in the request."\
                             "Ask your Tech-lead"

                ### If no idea wtf is it
                case _:
                    output = f"Failed: {response.status_code} - {response.text}"

            return output

        except requests.RequestException as e:
            print(f"Request failed on attempt {attempt + 1}: {e}")

    return "Request failed after retries."




# # Status-check
# if response.status_code == 200:
#     # Успешно получены данные
#     data = response.json()  # Распаковка JSON-ответа
#     print('Полученные данные:', data)
# else:
#     # Обработка ошибок
#     print('Ошибка:', response.status_code, response.text)


# headers = {
#     'Content-Type': 'application/json',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'Accept': '*/*'
#     # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # if needed
# }