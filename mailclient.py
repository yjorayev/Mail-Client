from socket import *
import base64
import time
import ssl

msg = "\r\n Oh wow. It finally works!!!!!!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587) #Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end
recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO Microsoft\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

tls = "STARTTLS\r\n"
clientSocket.send(tls.encode())
recv = clientSocket.recv(1024)
print("TLS: "+recv.decode())
clientSocket = ssl.wrap_socket(clientSocket)

clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)

#Info for username and password
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
base64_str = ("\x00"+username+"\x00"+password).encode()
base64_str = base64.b64encode(base64_str)
base64_str = base64_str.strip("\n".encode())
#auth = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print("After auth: "+recv_auth.decode())


# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM:<YOUR_EMAIL_ADDRESS>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO:<TARGET_EMAIL_ADDRESS>\r\n"
clientSocket.send(rcptTo.encode())
rcptTo = "RCPT TO:<TARGET_EMAIL_ADDRESS>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)
# Fill in end
# Send message data.
# Fill in start
subject = "Subject: testing my client\r\n\r\n" 
clientSocket.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
clientSocket.send(date.encode())
clientSocket.send(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
# Fill in end
clientSocket.close()