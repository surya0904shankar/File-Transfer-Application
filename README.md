# File-Transfer-Application
This project implements a simple and efficient file transfer system using Python. It allows users to transfer files over a network using TCP/IP socket programming. The application consists of two scripts: the sender and the receiver, ensuring that files can be transferred between devices connected over a network (LAN or Internet).

The goal of this project is to provide an easy-to-use solution for file sharing without the need for complex setups or third-party services. With future enhancements like encryption and GUI, this application aims to be a more secure and user-friendly tool.

Features
Socket Programming: Implements the TCP/IP protocol to ensure reliable data transmission.
Dynamic Buffer Management: The application handles large file transfers by breaking the data into manageable chunks.
Simple CLI: Easy command-line interface for initiating file transfers.
Support for All File Types: Send any kind of file (e.g., documents, images, videos, etc.).

Prerequisites
Python 3.x installed on both sender and receiver devices.
Both devices must be connected to the same network (or be able to communicate over the internet).

Installation
Clone the repository to both the sender and receiver devices:

bash
Copy code
git clone https://github.com/surya0904shankar/File-Transfer-Application.git
cd File-Transfer-Application
Install dependencies (if any are listed in requirements.txt):

bash
Copy code
pip install -r requirements.txt
How It Works
The sender script reads a file from the local filesystem and sends it over a socket connection to the receiver, which saves the file on the destination device.

File Transfer Process
Sender:

Runs sender.py, which takes the destination IP address (receiver's address) and the file path as input.
The file is read and sent in chunks to avoid overwhelming the network.
The sender waits for confirmation of successful file receipt from the receiver.
Receiver:

Runs receiver.py, which opens a socket to listen for incoming files.
Receives the file and saves it to the specified directory on the device.
Sends an acknowledgment to the sender once the file is successfully saved.
