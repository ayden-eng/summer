def setup():
    global Background
    size(2000,640)
    Background = loadImage("pen.PNG")


    
timer,m,x,X = False,0,0,0
def draw():
    global Background ,m,timer,x,X
    background(0,0,0)
    tint(255)
    if timer == True:
        for i in range (1,220):
            m += 0.001
            if m >= 220:
                m = 0
                timer = False

    if timer == False:
        x -= 1
        copy(loadImage("pen.PNG"),x,0,2000,640,0,0,2000,640)
        if x == 2000:
            timer =True
            x = -2000
    
    
