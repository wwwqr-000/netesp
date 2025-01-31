from netesp import page

def handle(request, cl):
    request = request.decode("utf-8")
    pathStartIndex = request.find("/")
    pathEndIndex = request.find(" ", 4)
    path = request[pathStartIndex:pathEndIndex]

    if (path == "/"): cl.send(page.send(page.homePage()))
    elif (path == "/pull"): cl.send(page.send(page.pullApi()))
    elif (path == "/push"): cl.send(page.send(page.pushApi()))
    elif (path == "/pullDesktop"): cl.send(page.send(page.pullDesktop()))

    cl.close()