# FlexTestman

FlexTestman is a tool for API testing that combines the functionalities of Postman and JMeter. The project allows you to manage API requests, configure parameters, save request history, and perform load testing.

## Key Features

- **Create and Execute API Requests:** Supports all major HTTP request types (GET, POST, PUT, DELETE, etc.).
- **Load and Performance Testing:** Capabilities for conducting load testing with JMeter.
- **Flexibility and Customization:** Supports creating request templates and flexible configuration of headers and parameters.
- **Intuitive Interface:** Graphical interface based on Tkinter for ease of use and management.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/FlexTestman.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd FlexTestman/src
    ```

3. **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Running the Application:**
   Navigate to the `src` directory and run the command:
   ```bash
   python main.py
   ```
## Creating an API Request

1. **In the graphical interface, select the request type.**
2. **Enter the URL, headers, and request parameters.**
3. **Click "Send" to execute the request.**

## Conducting Load Testing

1. **Switch to the `Load Testing` tab.**
2. **Specify the scenario and the number of concurrent users.**
3. **Click "Start Test".**

## Debugging and Logging

If errors occur, you can use debugging messages to identify the issue. Enable debugging mode in the application settings or add `print` statements in the code to output necessary information.

## Contributing

If you want to contribute to the project:

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature/NewFeature
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -am 'Add new feature'
    ```
4. **Push your changes to your branch:**
    ```bash
    git push origin feature/NewFeature
    ```
5. **Create a Pull Request.**

## Contact
For more information, you can refer to [Adam Rix's GitHub profile](https://github.com/Adam-Rix).
