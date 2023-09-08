# CodeCollab - Real-time Collaborative Code Editor

**Project Title:** CodeCollab

**Project Description:** CodeCollab is a real-time collaborative code editor that allows multiple users to code together simultaneously. It's a web-based platform where developers can create and join coding rooms, write, edit, and execute code in various programming languages, and see real-time updates from their collaborators. CodeCollab is designed to streamline remote pair programming, facilitate coding interviews, and enhance collaborative coding experiences.

---

## Features

- **Real-time Collaboration:** Multiple users can edit the same code file simultaneously and see each other's changes in real-time.
- **Syntax Highlighting:** Code is highlighted for various programming languages, making it easy to read and write.
- **Code Execution:** Execute code within the editor and view the output.
- **User Authentication:** Users can create accounts, log in, and access their private coding rooms.
- **Room Management:** Create and manage coding rooms, join rooms with room codes, and invite collaborators.
- **WebSockets:** Utilizes WebSocket technology for instant updates and chat functionality.
- **Secure:** User data and code are protected with authentication and authorization.
- **Responsive:** Works on various devices, including desktop and mobile.

---

## Tech Stack

### Frontend:

- **HTML/CSS:** For structuring and styling the web pages.
- **JavaScript:** For handling client-side logic and user interactions.
- **CodeMirror:** An open-source code editor that provides syntax highlighting and code editing features.
- **WebSocket:** For real-time communication between clients and the server.

### Backend:

- **Django:** A high-level Python web framework for building the backend of the web application.
- **Django Channels:** Extends Django to handle WebSockets, enabling real-time functionality.
- **Python:** The primary programming language for server-side logic.
- **Django ORM (Object-Relational Mapping):** For interacting with the database.
- **SQLite:** The database management system for storing user data and code.

### Version Control:

- **Git:** For version control and collaboration among developers.
- **GitHub:** A platform for hosting the Git repositories and managing the project.

### Other Tools and Libraries:

- **Redis:** In-memory data store for managing WebSocket connections and Celery task queues.

This tech stack combines frontend and backend technologies, ensuring a robust and responsive collaborative code editing experience for users.

---

## Installation

To install and run CodeCollab locally, follow these steps:

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/code-collab.git

2. Navigate to the project directory: 

```bash
  cd code-collab
```

3. Set up a virtual environment (optional but recommended):

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the Python dependencies:
```bash
  pip install -r requirements.txt
```

5. Run database migrations:
```bash
  python manage.py migrate
```
6. Start the Django development server:
```bash
  python manage.py runserver
``` 
Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

---

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://vivekdevkar123.github.io/Portfolio/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vivekdevkar123/)
[![twitter](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)](https://github.com/vivekdevkar123)

---

## Authors

- [@Vivek Devkar](https://www.github.com/vivekdevkar123)

---

## Feedback

If you have any feedback, please reach out to us at mrvivekdevkar123@gmail.com

---
