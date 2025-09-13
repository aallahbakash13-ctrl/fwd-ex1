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