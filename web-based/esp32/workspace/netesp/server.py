from netesp import config, superGlobals, page, requestResolver
import socket
import network
from time import sleep

def parse_query_string(query):
    """Parses a URL-encoded query string into a dictionary."""
    params = {}
    for pair in query.split('&'):
        if '=' in pair:
            key, value = pair.split('=', 1)
            params[key] = value
    return params

def run():
    addr_info = socket.getaddrinfo('0.0.0.0', config.webPort)
    addr = addr_info[0][4]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)

    while True:
        cl, addr = s.accept()
        clientIP, tmpPort = addr
        if (len(superGlobals.IP["entities"]) == 1): superGlobals.IP["entities"].append(clientIP)
        elif (clientIP != superGlobals.IP["entities"][1]):
            cl.close()
            continue
        
        print('Client connected from', addr)
        request = cl.recv(1024)
        requestResolver.handle(request, cl)