# EX01 Developing a Simple Webserver
## Date: 13-09-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
<title>TCP/IP Protocols</title>
<style>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid black;
    padding: 8px;
    text-align: left;
  }
  th {
    background-color: #f2f2f2;
  }
</style>
</head>
<body>

<h2>TCP/IP Protocol Suite Overview</h2>

<table>
  <thead>
    <tr>
      <th>TCP/IP Layer</th>
      <th>Equivalent OSI Layers</th>
      <th>Key Protocols</th>
      <th>Function</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Application Layer</td>
      <td>Application, Presentation, Session</td>
      <td>HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, SNMP, SSH, Telnet</td>
      <td>Provides network services directly to end-user applications (e.g., web browsing, email, file transfer, name resolution, remote access, network management).</td>
    </tr>
    <tr>
      <td>Transport Layer</td>
      <td>Transport</td>
      <td>TCP, UDP</td>
      <td>Manages end-to-end communication between applications, including reliability (TCP) and speed (UDP).</td>
    </tr>
    <tr>
      <td>Internet Layer</td>
      <td>Network</td>
      <td>IP, ICMP, ARP, RARP</td>
      <td>Handles logical addressing and routing of packets across interconnected networks.</td>
    </tr>
    <tr>
      <td>Network Access Layer</td>
      <td>Data Link, Physical</td>
      <td>Ethernet, Wi-Fi (802.11), PPP, Frame Relay</td>
      <td>Manages physical transmission of data frames over a local network medium and handles hardware addressing.</td>
    </tr>
  </tbody>
</table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

~~~

## successfully. OUTPUT:
![alt text](<Screenshot 2025-09-13 153443.png>)
![alt text](<Screenshot 2025-09-13 153532.png>)


## RESULT:
The program for implementing simple webserver is executed

