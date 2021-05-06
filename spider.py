import socket

f= open("C:/Users/phfro/PycharmProjects/spider/results.txt","w+")


for x in range(10,255):
    for y in range(10,255):
        for z in range(10,255):
            for k in range(10,255):
 #   print(socket.gethostbyaddr("2a00:1450:4009:802::2004"))
 #   print(socket.gethostbyaddr("86.153.207." + str(x)))
                print(socket.gethostbyaddr(str(x)+ "." + str(y)+ "." + str(z) + str(k)))
                f.write(str(x)+ "." + str(y)+ "." + str(z) + str(k) +"," +
                    socket.gethostbyaddr(str(x)+ "." + str(y)+ "." + str(z) + str(k)))
f.close()