import module_requests as mr
from ui.gui import ApiTester

def main():

    # CREDS
    link_to_json = 'resources/api_links.json'
    header_path = 'resources/headers.txt'

    # SEND_TO_GUI
    app = ApiTester(link_to_json=link_to_json,
                    header_path=header_path)
    app.mainloop()

if __name__ == "__main__":
    main()