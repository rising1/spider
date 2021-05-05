import socket

for x in range(255):
 #   print(socket.gethostbyaddr("2a00:1450:4009:802::2004"))
 #   print(socket.gethostbyaddr("86.153.207." + str(x)))
    print(socket.gethostbyaddr("86."+ str(x)+ "." + str(x)+ "." + str(x)))