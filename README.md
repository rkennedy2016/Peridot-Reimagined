**Peridot Local Revival**

*A self-hosted mock server and open-source preservation toolkit for keeping Peridot running locally after official server shutdowns. This repository provides the backend infrastructure to handle authentication handshakes and keep your virtual companions alive on your own network.*
Prerequisites

Python 3.8 or higher installed on your host machine (Windows, Linux, or Raspberry Pi).
Your own locally obtained client files or APK (not included in this repository due to copyright preservation guidelines).

Project Structure

peridot-local-revival/
├── mock_server.py     # Python-based mock OAuth and token server
└── README.md          # Setup and configuration guide

Quickstart Guide
1. Clone or Download the Repository

Clone this repository or download mock_server.py to your local machine or server device.
2. Configure Your Environment

Ensure your server device has a static or reliable local IP address.
3. Run the Mock Server

Open a terminal in the directory containing the script and run it using Python:

python3 mock_server.py

The server will bind to port 8000 by default and listen for incoming game authentication and token requests:
Plaintext

Mock auth server running on port 8000...

Technical Details

Authentication Mocking: The server handles incoming /ap/oa OAuth handshakes and returns valid token payloads to satisfy the client initialization sequence.

Cross-Platform Compatibility: Runs natively on any environment supporting Python's standard http.server module, making it ideal for Linux servers, Raspberry Pis, or Windows test environments.
