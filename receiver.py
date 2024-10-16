import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox
#modify this 

def receive_file(save_as, host='127.0.0.1', port=12345):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = sock.accept()
    print(f"Connected by {addr}")

    # Open the file to write the received data
    with open(save_as, 'wb') as fo:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            fo.write(data)

    print(f"File received and saved as '{save_as}'.")
    conn.close()
    sock.close()


if __name__ == "__main__":
    
    def select_folder():
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        folder_selected = filedialog.askdirectory()
        return folder_selected

    def main():
        print("Select the folder where the file will be saved.")
        folder = select_folder()
        if not folder:
            messagebox.showerror("Error", "No folder selected. Exiting.")
            return
        filename = input("Enter the filename to be saved: ")
        save_path = os.path.join(folder, filename)
        receive_file(save_path)

    if __name__ == "__main__":
        main()
