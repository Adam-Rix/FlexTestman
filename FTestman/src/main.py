import module_requests as mr

def main():
    # CREDS
    link_to_json = 'resources/api_links.json'
    header_path = 'resources/headers.txt'
    payload_path = 'resources/POST_payload_create.json'

    # OPTIONS
    server = 'test-2'
    function = 'booking-create'
    link_index = 0

    # LINK
    api_url = mr.get_link(server, function, link_index, link_to_json)

    if api_url:

        mr.send_request(api_url, payload_path, header_path)
    else:
        print("Link not found")


if __name__ == "__main__":
    main()