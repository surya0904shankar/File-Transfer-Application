import socket
import tkinter as tk
from tkinter import filedialog

def send_file(filename, host='127.0.0.1', port=12345):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        # Open the file to be sent
        with open(filename, 'rb') as fi:
            data = fi.read(1024)
            while data:
                sock.send(data)
                data = fi.read(1024)

        print(f"File '{filename}' sent successfully.")
    except IOError:
        print('You entered an invalid filename! Please enter a valid name.')
    finally:
        sock.close()

if __name__ == "__main__":
    '''filename = input("Enter the filename to send: ")
    send_file(filename)'''
    def select_file_and_send():
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename()  # Open file dialog to select file
        if file_path:
            send_file(file_path)

    # Create a simple GUI
    root = tk.Tk() 
    root.title("File Sender")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    select_button = tk.Button(frame, text="Select File and Send", command=select_file_and_send)
    select_button.pack()

    root.mainloop()