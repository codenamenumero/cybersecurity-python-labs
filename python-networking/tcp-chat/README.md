# Python TCP Chat Application

A beginner-friendly TCP client/server chat application built with Python sockets.

This project was created as part of my cybersecurity and Python networking journey.

---

# Features

- TCP socket communication
- Client/server architecture
- Message sending and receiving
- Exception handling
- Graceful disconnect support
- Error logging to terminal

---

# Technologies Used

- Python 3
- Socket Programming
- TCP Networking


---

# Problem Encountered

After sending a message from the client, the server terminated with a traceback error.
This happened because the application did not properly handle socket disconnections or unexpected errors during communication.


---

# Fix

The project was updated with exception handling using:
try:
...
except Exception as e: 

This prevents the server from crashing
 - the client disconnects unexpectedly
 - invalid data is received
 - network communication errors occur

The application now:
 - handles errors gracefully
 - prints useful error messages
 - closes sockets properly


---

# Project Structure

```bash
tcp_chat/
│-screenshots/
├── server.py
├── client.py
└── README.md