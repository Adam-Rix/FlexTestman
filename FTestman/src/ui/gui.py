import json
import tkinter as tk
from tkinter\
    import ttk
from FlexTestman.FTestman.src import\
    module_requests as mr


class ApiTester(tk.Tk):
    def __init__(self, link_to_json, header_path):
        super().__init__()
        self.title('FlexTestman')
        self.geometry('980x1024')

        self.selected_server = tk.StringVar()
        self.selected_function = tk.StringVar()
        self.selected_request_type = tk.StringVar()
        self.custom_payload = tk.StringVar()

        self.header_path = header_path
        self.headers_data = mr.load_header(self.header_path)

        self.link_to_json = link_to_json
        self.servers_data = self.load_servers(self.link_to_json)

        self.create_widgets()

    def load_servers(self, json_path):
        try:
            with open(json_path, 'r') as file:
                data = json.load(file)
            return data.get('servers', {})
        except Exception as e:
            print('''Can't load the data, status - 500; Check json file.''')
            return {}

    def create_widgets(self):
        # SERVER_UI_ZONE
        server_label = ttk.Label(self,
                                 text='Choose a server: ')
        server_label.pack(pady=5)

        server_combobox = ttk.Combobox(self,
                                       textvariable=self.selected_server,
                                       values=list(self.servers_data.keys()))
        server_combobox.pack(pady=5)

        # FUNCTION_UI_ZONE
        function_label = ttk.Label(self,
                                   text='Choose a function: ')
        function_label.pack(pady=5)

        self.function_combobox = ttk.Combobox(self,
                                              textvariable=self.selected_function,
                                              values=[])
        self.function_combobox.pack(pady=5)

        # REQUEST_UI_ZONE
        request_type_label = ttk.Label(self,
                                       text='Choose a type of the request: ')
        request_type_label.pack(pady=5)

        request_type_combobox = ttk.Combobox(self,
                                             textvariable=self.selected_request_type,
                                             values=["GET",
                                                     "POST",
                                                     "PUT",
                                                     "PATCH"])
        request_type_combobox.pack(pady=5)

        # PAYLOAD_UI_ZONE
        payload_label = ttk.Label(self,
                                  text='Payload')
        payload_label.pack(pady=5)

        self.payload_text = tk.Text(self,
                                    height=10, width=50)
        self.payload_text.pack(pady=5,
                               fill=tk.BOTH,
                               expand=True)

        # RESPONSE_UI_ZONE
        response_label = ttk.Label(self,
                                   text='Response')
        response_label.pack(pady=5)

        self.response_text = tk.Text(self,
                                     height=10,
                                     width=50)
        self.response_text.pack(pady=5,
                                fill=tk.BOTH,
                                expand=True)

        # BUTTON
        send_button = ttk.Button(self,
                                 text='Send Request',
                                 command=self.send_request)
        send_button.pack(pady=10)

        # Update function combobox values when server is selected
        server_combobox.bind("<<ComboboxSelected>>", self.update_functions)

    def update_functions(self, event):
        server = self.selected_server.get()
        if server in self.servers_data:
            functions = list(self.servers_data[server].get('functions', {}).keys())
            self.function_combobox['values'] = functions

    def send_request(self):
        server = self.selected_server.get()
        function = self.selected_function.get()
        request_type = self.selected_request_type.get()
        payload = self.payload_text.get("1.0", tk.END).strip()

        # Determine the API URL based on server and function
        link_index = 0
        api_url = mr.get_link(server,
                              function,
                              link_index,
                              self.link_to_json)

        if not api_url:
            self.response_text.delete("1.0", tk.END)
            self.response_text.insert(tk.END, "Link not found")
            return

        # Debug output for the API URL and request parameters
        # print(f"API URL: {api_url}")
        # print(f"Request Type: {request_type}")
        # print(f"Payload: {payload}")
        # print(f"Headers: {self.headers_data}")

        # Handle the request based on the type
        response = mr.send_request(api_url, payload=payload,
                                   headers_data=self.headers_data,
                                   request_type=request_type)

        self.response_text.delete("1.0", tk.END)
        self.response_text.insert(tk.END, response)
