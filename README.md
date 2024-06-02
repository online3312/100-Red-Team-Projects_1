# Network Tools and Utilities in Python

This repository contains a single Python script that includes various network tools and utilities. The tools include TCP and UDP chat servers, file transfer servers, Caesar Cipher and ROT13 encryption, remote command execution, and a Netcat-like tool.

## Prerequisites

- Python 3.x

## Table of Contents

1. [Usage](#usage)
2. [TCP Chat Server](#tcp-chat-server)
3. [UDP Chat Server](#udp-chat-server)
4. [Multithreaded TCP Chat Server](#multithreaded-tcp-chat-server)
5. [File Transfer Server](#file-transfer-server)
6. [Caesar Cipher Tool](#caesar-cipher-tool)
7. [TCP Chat Server with Caesar Cipher](#tcp-chat-server-with-caesar-cipher)
8. [ROT13 Encryption Tool](#rot13-encryption-tool)
9. [UDP Chat Server with ROT13 Encryption](#udp-chat-server-with-rot13-encryption)
10. [Remote Command Execution](#remote-command-execution)
11. [Netcat-like Tool](#netcat-like-tool)

## Usage

Run the script with the desired function name as an argument. For example:


python network_tools.py <function_name>
Replace  with one of the following: , , , , , , , , , .<function_name>tcp_chat_serverudp_chat_servermultithreaded_tcp_chat_serverfile_transfer_servercaesar_cipher_tooltcp_chat_server_with_caesar_cipherrot13_tooludp_chat_server_with_rot13remote_command_executionnetcat_tool

TCP Chat Server
Starts a basic TCP chat server that allows multiple clients to connect and send messages to each other.

Usage
python network_tools.py tcp_chat_server
UDP Chat Server
Starts a basic UDP chat server that allows multiple clients to send messages to each other.

Usage
python network_tools.py udp_chat_server
Multithreaded TCP Chat Server
Starts a multithreaded TCP chat server that handles multiple clients using threading.

Usage
python network_tools.py multithreaded_tcp_chat_server
File Transfer Server
Starts a TCP server that allows clients to upload files to the server.

Usage
python network_tools.py file_transfer_server
Caesar Cipher Tool
Provides a command-line tool to encrypt text using the Caesar Cipher.

Usage
python network_tools.py caesar_cipher_tool
TCP Chat Server with Caesar Cipher
Starts a TCP chat server where messages are encrypted using the Caesar Cipher before being sent to other clients.

Usage
python network_tools.py tcp_chat_server_with_caesar_cipher
ROT13 Encryption Tool
Provides a command-line tool to encode text using the ROT13 algorithm.

Usage
python network_tools.py rot13_tool
UDP Chat Server with ROT13 Encryption
Starts a UDP chat server where messages are encoded using the ROT13 algorithm before being sent to other clients.

Usage
python network_tools.py udp_chat_server_with_rot13
Remote Command Execution
Starts a TCP server that allows clients to execute commands on the server remotely.

Usage
python network_tools.py remote_command_execution
Netcat-like Tool
Implements a simple Netcat-like tool that can either listen for incoming connections or connect to a server.

Usage
To listen for incoming connections:
python network_tools.py netcat_tool listen <host> <port>
To connect to a server:

python network_tools.py netcat_tool connect <host> <port>
Replace  and  with the appropriate values.<host><port>

License
This project is licensed under the MIT License. See the LICENSE file for details.
