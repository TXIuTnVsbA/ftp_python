import socket,threading,re
def connect(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip,port))
    print sock.recv(1024)
    sock.close()

def print_sock(sock):
    while True:
        str = sock.recv(1024)
        print str
        tmp = str.split()
        if (tmp[0] == '221'):
            break
        if (tmp[0] == '227'):
            try:
                req = re.findall(r'\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3},\d{1,3}', str)[0].split(',')
                if (req):
                    new_ip = req[0] + '.' + req[1] + '.' + req[2] + '.' + req[3]
                    new_port = int(int(req[4]) * 256 + int(req[5]))
                    threading.Thread(target=connect, args=(new_ip, new_port)).start()
            except:
                pass
    sock.close()
    exit(0)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        str = raw_input().split(',')
        if (str[0].lower() == 'exit' or str[0].lower() == 'quit'):
            s.send('quit\r\n')
            exit(0)
        if (str[0].lower() == 'connect'):
            try:
                s.connect((str[1], int(str[2])))
                threading.Thread(target=print_sock, args=(s,)).start()
            except:
                pass
        if (str[0].lower() == 'login'):
            s.send('user ' + str[1] + '\r\n')
            s.send('pass ' + str[2] + '\r\n')
        if (str[0].lower() == 'ls' or str[0].lower() == 'dir'):
            s.send('pasv\r\n')
            s.send('list\r\n')
        if(str[0].lower()=='send'):
            if(str[1].lower()=='quit' or str[1].lower()=='exit' ):
                s.send('quit\r\n')
                exit(0)
            else:
                s.send(str[1]+'\r\n')
