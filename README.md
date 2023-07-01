# Chat-Sample-App

This is a sample/starter code for some programming assignments in the Distributed Systems course taught by Prof. Fábio M. Costa at UFG in 2022. The app implements a simple client-server architecture where students can identify limitations, problems, and make enhancements at various levels, including architectural, non-functional aspects, and functional aspects.

## Architecture Overview

The Chat-Sample-App follows a basic client-server architecture. The server acts as a central point for message relaying between clients. Each client can send messages to other clients via the server.

![Chat Design - client-server](https://user-images.githubusercontent.com/13460193/173588387-89793ac9-17b9-4441-986b-53cac6ee40f4.png)

## Functionality

The Chat-Sample-App provides the following functionality:

1. User Registration: Users can register their names along with their IP addresses and port numbers in the `const.py` file.

2. Sending and Receiving Messages: Clients can send messages to other clients by specifying the destination username. The server relays the messages to the appropriate clients.

3. Dynamic User Addition: If a user attempts to connect with a name that doesn't exist in the `const.py` registry, the app prompts the user to provide the IP address and port number for the new user. The information is then added to the registry.

4. Concurrent Message Handling: The app utilizes threads to handle multiple client connections simultaneously. Each client connection is handled in a separate thread to allow concurrent message sending and receiving.

## Getting Started

To use the Chat-Sample-App, follow these steps:

1. Clone the repository: `git clone https://github.com/your_username/Chat-Sample-App.git`
2. Navigate to the project directory: `cd Chat-Sample-App`
3. Configure the `const.py` file: Update the `registry` dictionary with the desired usernames, IP addresses, and port numbers.
4. Start the server: Run the server code using `python3 server.py`.
5. Start a client: Run the client code using `python3 client.py <Username>`, where `<Username>` is the desired username for the client.
6. Interact with the client: Use the command-line interface to enter the destination username and message. Follow the prompts for further actions.

## Examples

Here are a few examples of how to use the Chat-Sample-App:

1. Registering a New User:
   - If the user attempts to connect with a username that doesn't exist in the `const.py` registry, they will be prompted to enter the IP address and port number for the new user.
   - The registry will be updated with the new user's information, allowing future connections using the new username.

2. Sending Messages:
   - When prompted, enter the destination username and message.
   - The message will be sent to the server and relayed to the appropriate client.

3. Exiting the App:
   - To exit the app, either enter "exit" as the destination username or when prompted to enter the destination username.

## Contributions

Contributions to the Chat-Sample-App are welcome. You can enhance the app by addressing limitations, improving non-functional aspects, or adding new functionality. Feel free to create pull requests with your enhancements.

## License

This project is licensed under the MIT License.

## Students

Antonio Emilio - 201905481
Melyssa Mariana - 201905503