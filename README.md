
# Peridot Local Revival Toolkit

A complete open-source toolkit containing a Python-based automation script to build a modified universal APK and a local mock server to keep Peridot running on your local network.

---

## Repository Structure

peridot-local-revival/
├── mock_server.py     # Local mock OAuth and token handler
├── builder.py         # Automated split-APK merger and signer script
└── README.md          # Full setup instructions





## Prerequisites

* **Python 3.8+** installed on your system.
* **Java Runtime Environment (JRE/JDK)** installed (required for APKEditor and `jarsigner` / `keytool`).
* Your own legally backed-up Peridot split APK files (place them in a local folder).



## Step-by-Step Guide

### Step 1: Clone or Download the Toolkit

Download or clone this repository onto your computer or server host.

### Step 2: Run the Automated APK Builder

Place your exported game split APKs in a folder, open your terminal in the repository directory, and run the builder script:

python3 builder.py



The script will automatically:

1. Download APKEditor if it isn't present.
2. Merge your split APKs into a single *peridot_universal.apk*.
3. Create and inject an *api_key.txt* asset containing your chosen server IP.
4. Generate a local debug keystore and sign the package automatically.

### Step 3: Start the Mock Server

On your server host (or local machine), configure your environment variable or run the mock server script:

python3 mock_server.py



### Step 4: Install and Play

Transfer the newly generated *peridot_universal.apk* to your Android device, install it, and launch it to connect directly to your local backend.
The server will bind to port 8000 by default and listen for incoming game authentication and token requests:
Plaintext

Mock auth server running on port 8000...

Technical Details

Authentication Mocking: The server handles incoming /ap/oa OAuth handshakes and returns valid token payloads to satisfy the client initialization sequence.

Cross-Platform Compatibility: Runs natively on any environment supporting Python's standard http.server module, making it ideal for Linux servers, Raspberry Pis, or Windows test environments.
