from netesp import config, superGlobals, page
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
        request_lines = request.decode().splitlines()
        
        if request_lines[0].startswith('POST'):
            for line in request_lines:
                if line.startswith('Content-Length:'):
                    content_length = int(line.split(': ')[1])
                    break
            else:
                content_length = 0
            body = request[-content_length:] if content_length > 0 else b''
            print("Body:", body.decode())
            if content_length > 0:
                body_str = body.decode()
                parsed_body = parse_query_string(body_str)
                name_value = parsed_body.get('led', '')
                print("Led:", name_value)

        print("Request:", request)
        
        cl.send(page.send(page.homePage(request)))
        cl.close()
        