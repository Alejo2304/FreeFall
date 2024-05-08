import sys, pygame, time
from menu import *
from menu import height_

#Function.
def getFreeFall(height, t):#calculate speed and height on a determinate second. 
    
    #calculates height per each second. 
    h = (GRAVITY*(t**2))/2
    h = round(h,2)
     #calculate the final velocity when touch the ground.
    if h > height:
        h = height #reassign height
        #calculates final speed based on the height.
        vf = ((2*GRAVITY*h)**(1/2))
        #calculates the time at the final height. 
        t = (h / (vf/2))
    else:
      #calculates speed per each second. 
        vf = GRAVITY*t 

    #round t and vf to only 2 decimals.     
    t = round(t, 2)
    vf = round(vf, 2)
    result = [vf, h, t]
    return result
def meterToPx(meter,screen,escale):#it uses 3 rule to convert the meter provided into px position. 
    posX = screen[0] // 2
    posY = (meter//(escale[1] / screen[1])) #posY traduce the amount in meter to Px
    posY = int(screen[1] - posY) #Provide us with the coordinate in the plane for Y. 
    return [posX,posY]

#Pygame
pygame.init()
size = width, height = 800, 600 # this is our plane.
escale = [200,150] # 200 meters per 150 meters. this is our scale
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif") #Load images ball.gif so it can be use inside the program7
ballrect = ball.get_rect() #It obtains the rectangle of the ball.gif after its convertion.
 


#-----GLOBAL VARIABLES-----
FONT_ARIAL = pygame.font.SysFont("Arial", 40)
GRAVITY = 9.806
#-----VARIABLES----- 
h = t = i = 0 #initializes the variables.
freeFall = []  # initializes array.
#-----Dictionary-----
#RGB Colors save in a dictionary. 
colors = {
    "BLACK" : (0  ,0  ,0  ),
    "WHITE" : (255,255,255),
    "RED"   : (255,0  ,0  ),
    "GREEN" : (0  ,255,0  ),
    "BLUE"  : (0  ,0  ,255),
    }
 
hmax = height_.get() #request for height

while h < hmax:
    freeFall.append(getFreeFall(hmax,t)) #add the result from the function into our array 
    h = freeFall[i][1]  #update the value of height for each interaction
    t += 0.1
    i += 1
 
i = 0 #restart value if iterator to 0.

#while True: 
for data in reversed(freeFall):

    #-----Text to show in screen ------/
    strV = "Velocidad: "+str(freeFall[i][0])+" m/s2." #Save an string with the message
    txtV = FONT_ARIAL.render(strV, True, colors["GREEN"]) #Render the message with the font and color. 
    strH = "Altura:    "+str(data[1])+" meter."
    txtH = FONT_ARIAL.render(strH, True, colors["WHITE"])
    strT = "Tiempo:    "+str(freeFall[i][2]) +" seconds."
    txtT = FONT_ARIAL.render(strT, True, colors["RED"])
    i+=1 #Increase value of iterator. 
    #-----Text to show in screen ------

    mtr = meterToPx(data[1],size,escale)  #Position in screen for ball. 

    #-----ZONA DE DIBUJO-----
    screen.fill(colors["BLACK"])
    screen.blit(ball, (mtr[0],mtr[1]-ballrect.height))

    screen.blit(txtH, (0,20))
    screen.blit(txtV, (0,60))
    screen.blit(txtT, (0,100))
    #-----ZONA DE DIBUJO-----
    pygame.display.flip()
    time.sleep(0.1)
    
    