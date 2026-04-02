# Simple Python Socket Chat (Server & Client)

This project demonstrates a basic socket-based server and client communication in Python using TCP. The server can handle multiple clients concurrently using threading.

## Features

- **Multi-client support:** Each client connection is handled in a separate thread.
- **Custom protocol:** Messages are sent with a fixed-length header indicating the message size.
- **Graceful disconnect:** Clients can disconnect by sending a special message.

## Files

- `server.py` — The server script. Listens for incoming connections and prints received messages.
- `client.py` — The client script. Connects to the server and sends messages.

## How It Works

1. **Server:**
   - Binds to a local IP and port.
   - Waits for client connections.
   - For each client, starts a new thread to handle communication.
   - Receives messages with a fixed-size header indicating the message length.

2. **Client:**
   - Connects to the server.
   - Sends messages prefixed with a header specifying the message length.

## Usage

### 1. Start the Server

Open a terminal and run:

```bash
python server.py
```

### 2. Start the Client

In another terminal, run:

```bash
python client.py
```

You can modify `client.py` to send different messages.

## Protocol

- **Header:** 64 bytes, contains the length of the message.
- **Encoding:** UTF-8.

## Disconnect

To disconnect a client, send the message `"Disconnect me"`.

## Requirements

- Python 3.x

No