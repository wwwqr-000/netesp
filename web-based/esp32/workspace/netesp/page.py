def send(pageRes):
    header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\n\r\n".format(len(pageRes))
    return header + pageRes

def homePage(data):
    return f"""<!DOCTYPE html>
    <html>
    <head>
        <title>netesp - home</title>
    </head>
    <body>
    { data }
    </body>
    </html>
    """