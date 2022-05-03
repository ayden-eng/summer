def setup():
    global Background
    size(2000,640)
    Background = loadImage("pen.PNG")
            
    
timer = True
def draw():
    global Background
    
    image(Background,0,0)
