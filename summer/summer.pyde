def setup():
    global Background,Night,Sun,Moon
    size(1270,640)
    Background = loadImage("pen.PNG")
    Night = loadImage("pennight.PNG")
    Sun = loadImage("sun.png")
    Moon = loadImage("moon.png")

    
timer,m,x,X,XX,timer2,n,nn,mm,sun, = True,0,0,1270,1270,None,0,0,False,1000,
def draw():
    global Background ,m,timer,x,X,XX,Night,timer2,n,nn,mm,Sun,sun,Moon
    background(0,0,0)
    tint(255)
    if timer == True:
        for i in range (1,220):
            m += 0.001
            if m >= 220:
                m = 0
                timer = False
                mm = False

    if timer == False:
        x -= 10
        X -= 10
        sun += 10
        copy(loadImage("pen.PNG"),x,0,2000,640,0,0,2000,640)
        image(Sun,sun,40) 
        copy(loadImage("pennight.PNG"),X,0,2000,640,0,0,2000,640)
        image(Moon,sun-1270,40)
        if X <= 0:
            timer = None
            image(Night,0,0)
            timer2= True
            x = 0
            sun = -370
    if timer2 == True:
        image(Night,0,0)
        image(Moon,1000,40)
        for i in range (1,230):
            n += 0.001
            if n >= 220:
                n = 0
                timer2 = False
                X = 0
    if timer2 == False:
        XX -= 10
        X -= 10
        sun += 10

        copy(loadImage("pennight.PNG"),X,0,2000,640,0,0,2000,640)
        image(Moon,sun+1420,40)
        copy(loadImage("pen.PNG"),XX,0,2000,640,0,0,2000,640)
        image(Sun,sun,40) 
        if XX <= 0:
            timer2 = None
            timer = True
            XX = 1270
            X = 1270
            mm =True
            sun = 900

    if timer == True:
        image(Background,0,0)
        
        image(Sun,1000,50)
        if mm == True:
            text("Summertime is always the best time",150,40)
            textSize(40)
    
    
