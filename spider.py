import socket

f= open("C:/Users/phfro/PycharmProjects/spider/results.txt","w+")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#target = input('What website to scan?: ')

def pscan(port):
    try:
        con = s.connect((target[0],port))
        return True
    except:
        return False


for x in range(86,255):
    for y in range(153,255):
        for z in range(207,255):
            for k in range(10,255):
 #   print(socket.gethostbyaddr("2a00:1450:4009:802::2004"))
 #   print(socket.gethostbyaddr("86.153.207." + str(x)))
                try:
                    target = socket.gethostbyaddr(str(x) + "." + str(y) + "." + str(z) + "." + str(k))
                    result = " placeholder "
                    #for x in range(80, 80):
                    #    if pscan(x):
                    #        result = ('Port', x, 'is open')
                    #    else:
                    #        result = ('Port', x, 'is closed')
                    print(target[0] + " " + result)
                    f.write(target[0] + " " + result +  "\n")
                except Exception as e:
                    print(str(e) + " " + str(x) + "." + str(y) + "." + str(z) + "." + str(k))
f.close()