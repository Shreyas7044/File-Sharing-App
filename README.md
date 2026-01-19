# 📂 File Sharing App using Python

Computer Networks is an important topic, and understanding it requires practical implementation.  
This project demonstrates a **simple file-sharing application** using Python that allows you to share files from your PC to a mobile device using a browser and QR code.

---

## 🚀 Features
- Share files over local network
- No internet required
- QR code-based access
- Uses Python’s built-in HTTP server
- Works on any browser (mobile or desktop)

---

## 🛠 Modules Used

- **HTTPServer** – Creates and listens on an HTTP socket
- **socketserver** – Simplifies writing network servers
- **webbrowser** – Opens QR code automatically in browser
- **pyqrcode** – Generates QR codes
- **PyPNG** – Saves QR codes as PNG/SVG
- **os** – Interacts with the operating system

---

## 📱 How It Works
- The script starts a local HTTP server on port 8010.
- Your system IP address is detected automatically.
- A QR code is generated for the server URL.
- The QR code opens in your default browser.
- Scan the QR code using your mobile device.
- Access and download files from your PC browser.

---

## 📌 Output
- A QR code file (file_share_qr.svg) is generated.
- Terminal displays the local IP address.
- Files in your OneDrive/Desktop folder become accessible.

---

## ⚠️ Notes
- Both devices must be on the same Wi-Fi network.
- Change the directory path in main.py if needed.
- Use CTRL + C to stop the server.
