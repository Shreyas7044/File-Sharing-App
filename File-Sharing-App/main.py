# import necessary modules

# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to display a Web-based documents to users
import webbrowser

# to generate qrcode
import pyqrcode
from pyqrcode import QRCode

# convert into png format
import png

# to access operating system control
import os


# assigning the appropriate port value
PORT = 8010

# this finds the name of the computer user
user_profile = os.environ['USERPROFILE']

# changing the directory to access the files desktop/OneDrive
desktop = os.path.join(user_profile, 'OneDrive')
os.chdir(desktop)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler

# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)

# converting the IP address into a QR code
url = pyqrcode.create(IP)
url.svg("file_share_qr.svg", scale=8)

# opens the QR code in the web browser
webbrowser.open("file_share_qr.svg")

# starting the HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving files at port:", PORT)
    print("Access using browser:", IP)
    print("Or scan the QR Code")
    httpd.serve_forever()
