# Chat Room Application

This is a simple chat room application built with Flask and SocketIO. It allows users to create chat rooms with unique codes and join existing rooms to chat in real-time.

### Technologies Used

- Flask: Web framework for Python.

- Flask-SocketIO: Extension for Flask to handle WebSockets.

- HTML/CSS/JavaScript: For the front-end interface.

Setup

1. Clone the repository:

   git clone <repository-url>

2. Navigate to the project directory:

   cd <project-directory>

3. Install the required dependencies:

   pip install -r requirements.txt

   Note: Ensure you have Python and pip installed on your system.

4. Run the application:

   python app.py

   The application will be available at http://localhost:5000.

Usage

1. Open the application in your web browser at http://localhost:5000.

2. On the home page, enter your name.

3. To create a new room, click the "Create a Room" button. A unique room code will be generated.

4. To join an existing room, enter the room code and click "Join a Room".

5. Once in a room, you can send messages by typing in the input box and clicking "Send" or pressing Enter.

6. Messages will be displayed in real-time to all users in the same room.

Notes

- Authentication: This application does not include user authentication or any security measures. I am not focusing on authentication, so it is intended for demonstration purposes only and should not be used in production without proper security implementations.

- Front-end: I am not focusing on the front-end, so it is minimal and uses basic HTML and JavaScript. It is not styled extensively and is intended to demonstrate the functionality rather than provide a polished user interface.

Contributing

If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository. Alternatively, you can fork the repository and submit a pull request with your changes.

