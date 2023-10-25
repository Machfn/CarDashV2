import eel

def close_callback(route, websockets):
    if not websockets:
        print('Bye!')
        exit()

eel.init("web", allowed_extensions=['.js', '.html'])

@eel.expose
def startf():
    print("received")
    return "Starting..."



#  Start the index.html file
eel.start("index.html", size=(800, 400))