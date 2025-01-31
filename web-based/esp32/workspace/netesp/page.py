from netesp import superGlobals
import os, json

def send(pageRes):
    header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {}\r\n\r\n".format(len(pageRes))
    return header + pageRes

def homePage():
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>netesp</title>
            <style>
                * {{
                    box-sizing: border-box;
                    overflow: hidden;
                    margin: 0vw;
                }}
                #screen {{
                    aspect-ratio: auto;
                    width: 100vw;
                    height: 100vh;
                }}
            </style>
            <script>
                setTimeout(() => {{
                    let scrn = document.getElementById("screen");
                    let ctx = scrn.getContext("2d");

                    const grd = ctx.createLinearGradient(0, 0, scrn.width, scrn.height);
                    grd.addColorStop(0, "purple");
                    grd.addColorStop(1, "blue");
                    ctx.fillStyle = grd;
                    ctx.fillRect(0, 0, scrn.width, scrn.height);

                }}, 50);
            </script>
        </head>
        <body>
            <canvas id="screen" width="4000" height="2000"></canvas>
        </body>
        </html>
    """

def pullApi():
    return "testPull"

def pushApi():
    return "testPush"

def pullDesktop():
    res = [f for f in os.listdir("/netesp/drive/desktop/")]
    return json.dumps(res)