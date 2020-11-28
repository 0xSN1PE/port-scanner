import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

print(
	'''
  _____   ____  _____ _______    _____  _____          _   _ _   _ ______ _____  
 |  __ \ / __ \|  __ |__   __|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | |__) | |  | | |__) | | |    | (___ | |       /  \  |  \| |  \| | |__  | |__) |
 |  ___/| |  | |  _  /  | |     \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
 | |    | |__| | | \ \  | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_|     \____/|_|  \_\ |_|    |_____/ \_____/_/    \_|_| \_|_| \_|______|_|  \_\
 	'''
	)


def portScanner(ip, port):
	if s.connect_ex((ip, port)):
		print("The port is closed.")
	else:
		print("The port is open.")

def help_msg():
    print('''
Usage: python3 port_scanner.py [IP Address to scan] [Port]

Example:

python3 port_scanner.py 172.217.161.4 1337

''')
    quit()

if "help" in sys.argv:
    help_msg()
else:
    try:
        print(sys.argv[1])
        print(sys.argv[2])
        try:
            portScanner(sys.argv[1],int(sys.argv[2]))
        except Exception as e:
            print('An error occured.')
            print(e)
    except:
        print('WRONG USAGE.')
        help_msg()
