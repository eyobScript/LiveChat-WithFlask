### Chat Room Application  

Creating a simple chat room application using Flask and SocketIO. This app will allow users to start chats with unique codes and also chat on existing rooms in real-time.  

---

### Technologies Used  

- **Flask**: Web framework for Python.  
- **Flask-SocketIO**: Extension for Flask to handle WebSockets.  
- **HTML/CSS/JavaScript**: For the front-end interface.  

---

### Setup  

1. Clone the repository:  
   ```bash
   git clone <repository-url>
   ```  
2. Navigate to the project directory:  
   ```bash
   cd <project-directory>
   ```  
3. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
   **Note**: Make sure you have Python and pip installed on your system.  
4. Run the application:  
   ```bash
   python main.py
   ```  
   The application will be available at **http://localhost:5000**.  

---

### Usage  

1. Open the application in your web browser at **http://localhost:5000**.  
2. On the home page, enter your name.  
3. To create a new room, click the **"Create a Room"** button. A unique room code will be generated.  
4. To join an existing room, enter the room code and click **"Join a Room"**.  
5. Once in a room, you can send messages by typing in the input box and clicking **"Send"** or pressing **Enter**.  
6. Messages will be displayed in real-time to all users in the same room.  

---

### Notes  

- **Authentication**: This app lacks the functionality of user authentication or any security features. I do not concentrate on authentication and, therefore, it is meant to be for the purposes of demonstration, and to use it in production, there should be security developments implemented.  
- **Front-end**: The front-end of the site barely was programmed. It is a very simple HTML/JavaScript application which is intended not to be visually attractive but to demonstrate its functionality and provide a simple user interface.  

---

### Contributing  

Issues should be reported and by the way, feel free to suggest improvements, opening an issue on the GitHub repository. Instead, you can fork the repository or add, edit and impart your changes via a pull request to the project.

