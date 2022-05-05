add_library('minim')
def setup():
    global Background,Night,Sun,Moon,summer
    size(1270,640)
    minim=Minim(this)
    summer=minim.loadFile("summer.mp3")
    Background = loadImage("pen.PNG")
    Night = loadImage("pennight.PNG")
    Sun = loadImage("sun.png")
    Moon = loadImage("moon.png")

    
timer,m,x,X,XX,timer2,n,nn,mm,sun,timer3, = True,0,0,1270,1270,None,0,0,False,1000,True
one,y,p,k,song=(255, 0, 0),0,"p",0,key
def draw():
    global Background ,m,timer,x,X,XX,Night,timer2,n,nn,mm,Sun,sun,Moon,summer,timer3,song
    global one,y,p,k
    background(0,0,0)
    tint(255)
#________________________________________________________This is a timer for 30s and then i turns the timer off
    if timer == True:
        for i in range (1,220):
            m += 0.001
            if m >= 220:
                m = 0
                timer = False
                mm = False
#________________________________________________________This chages the day to night and then starts the second timer
    if timer == False:
        x -= 10
        X -= 10
        sun += 10
        copy(loadImage("pen.PNG"),x,0,2000,640,0,0,2000,640)
        fill(244, 247, 32)
        ellipse(sun+30,100,100,100)
        image(Sun,sun,50) 
        copy(loadImage("pennight.PNG"),X,0,2000,640,0,0,2000,640)
        fill(255,255,255)
        ellipse(sun-1230,85,100,100)
        image(Moon,sun-1270,40)
        if X <= 0:
            timer = None
            image(Night,0,0)
            timer2= True
            x = 0
            sun = -370
#__________________________________________________________This turns on and prints the night background and starts a second timer
    if timer2 == True:
        image(Night,0,0)
        ellipse(sun+1395,85,100,100)
        image(Moon,1000,40)

        for i in range (1,230):
            k += 0.001
            if k >= 220:
                k = 0
                timer2 = False
                X = 0
                sun = -370
#___________________________________________________________When the second timer is done this turns on and turn it from night to day
    if timer2 == False:
        XX -= 10
        X -= 10
        sun += 10

        copy(loadImage("pennight.PNG"),X,0,2000,640,0,0,2000,640)
        fill(255,255,255)
        ellipse(sun+1462,85,100,100)

        image(Moon,sun+1420,40)
        copy(loadImage("pen.PNG"),XX,0,2000,640,0,0,2000,640)
        fill(244, 247, 32)
        ellipse(sun+30,85,100,100)
        image(Sun,sun,40) 
        if XX <= 0:
            timer2 = None
            timer = True
            XX = 1270
            X = 1270
            mm =True
            sun = 1000
#__________________________________________________________once it is day it turns of the 30s timer
#__________________________________________________________ this function prints the day time when timer one is true  
    def Day(timer, sun,Sun,mm):
        if timer == True:
            image(Background,0,0)
            fill(244, 247, 32)
            ellipse(sun+30,100,100,100)
            image(Sun,1000,50)
            if mm == True:
                text("Summertime is always the best time",500,400)
                textSize(40)
    Day(timer=timer ,sun=sun,Sun=Sun,mm=mm)
#___________________________________________________________________ this is a thrid timer for 
    if timer3 == True:
        for i in range (1,100):
            n += 0.001
            if n >= 0 and n <= 20:
                one=[255,0,0]
            if n >=21 and n <=40:
                one=[0, 39, 255]
            if n >= 40:
                n = 0
#___________________________________________________________________This make Confetti 
    if timer == True:
        if y <=500:
            y+=1
        if y >=500:
            if n >=39:
                y=0
        fill(one[0],one[1],one[2])
        rect(200,y+100,10,20)
        rect(340,y+100,20,10)
        rect(400,y+20,20,10)
        rect(100,y+100,20,10)
        rect(600,y+100,10,20)
        rect(800,y+120,20,10)
        rect(1200,y+80,20,10)
        rect(900,y+20,20,10)
#_________________________________________________________________This makes clouds when timer one is true
    def Cloud(timer):
        if timer == True:
            fill(255,255,255)
            ellipse(100,100,50,40)
            ellipse(120,80,40,40)
            ellipse(140,100,60,50)
            #______________________
            ellipse(510,90,90,60)
            ellipse(560,60,60,60)
            ellipse(580,90,100,70)
            #______________________
        
            ellipse(860,60,60,60)
            ellipse(880,60,60,60)
            ellipse(820,60,60,60)
            ellipse(880,90,100,70)
            ellipse(810,90,90,60)
            #______________________
            ellipse(360,100,100,30)
            ellipse(320,100,100,30)
            ellipse(380,120,150,40)
            ellipse(310,120,120,30)
            #______________________
            ellipse(660,200,60,30)
            ellipse(640,200,60,30)
            ellipse(680,220,70,40)
            ellipse(630,220,70,30)
            #----------------------
            ellipse(180,300,40,30)
            ellipse(140,320,50,30)
            ellipse(180,320,50,40)
            #----------------------
            ellipse(1080,300,40,50)
            ellipse(1040,320,50,50)
            ellipse(1080,320,50,60)
    Cloud(timer=timer)
#_______________________________________________________This makes the song play
    def Song (song):
        if  key != "p":
            summer.play()
        if key == "s":
            summer.pause()
            summer.rewind()
    Song(song=song)



#_____________________________________________________Moves the clouds
    if timer == False:
            fill(255,255,255)
            ellipse(-1*x+100,100,50,40)
            ellipse(-1*x+120,80,40,40)
            ellipse(-1*x+140,100,60,50)
            #______________________
            ellipse(-1*x+510,90,90,60)
            ellipse(-1*x+560,60,60,60)
            ellipse(-1*x+580,90,100,70)
            #______________________
        
            ellipse(-1*x+860,60,60,60)
            ellipse(-1*x+880,60,60,60)
            ellipse(-1*x+820,60,60,60)
            ellipse(-1*x+880,90,100,70)
            ellipse(-1*x+810,90,90,60)
            #______________________
            ellipse(-1*x+360,100,100,30)
            ellipse(-1*x+320,100,100,30)
            ellipse(-1*x+380,120,150,40)
            ellipse(-1*x+310,120,120,30)
            #______________________
            ellipse(-1*x+660,200,60,30)
            ellipse(-1*x+640,200,60,30)
            ellipse(-1*x+680,220,70,40)
            ellipse(-1*x+630,220,70,30)
            #----------------------
            ellipse(-1*x+180,300,40,30)
            ellipse(-1*x+140,320,50,30)
            ellipse(-1*x+180,320,50,40)
            #----------------------
            ellipse(-1*x+1080,300,40,50)
            ellipse(-1*x+1040,320,50,50)
            ellipse(-1*x+1080,320,50,60)

        
