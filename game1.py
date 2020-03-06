import pygame
import pygame_camera
import pygame_ai
from time import *
from pygame.locals import *
import random as r
pygame.init()
run =True
win=pygame.display.set_mode((400,373))
pygame.display.set_caption("Game for Youtube")

Bg=[pygame.image.load('image.png').convert(),pygame.image.load('image.png').convert()]
Clock=pygame.time.Clock()
FPS=120
bg=pygame.image.load('image.png').convert()
x_c=[]

rock=[pygame.image.load('blocks.png').convert()]

def move_coordinates(x_c,y_c):

    pygame.draw.rect(win,(255,0,100),(x_c,y_c, 50,50),0)

obstacles=[]

class object:
    def __init__(self,y,obj_vel):
        self.obj_vel=obj_vel
        self.x=0
        self.y=y
        self.vel=1
        self.x1=800
        self.right=0
        self.jump=False
        self.counter=10
        self.count=0
        self.i=0
        self.hit=False

    def scroll(self):
        win.blit(bg, (self.x, 0))
        win.blit(Bg[0], (self.x1, 0))
        self.x -= 1
        self.x1 -= 1
        if self.x == Bg[0].get_width() * -1:
            self.x = 800
        if self.x1 == Bg[0].get_width() * -1:
            self.x1 = 800


    def move_obj(self):
        #move_coordinates(self.obj_vel,self.y)
        self.hitbox = (self.obj_vel, self.y, 50, 50)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.obj_vel+=1



    def stay_obj(self):
        #move_coordinates(self.obj_vel,self.y)
        self.hitbox = (self.obj_vel, self.y, 50, 50)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.obj_vel-=0.5
        if self.obj_vel < 0:
            move_coordinates(0,self.y)

    def hit(self):

        if self.y <= 150 and x_c[self.i]+10 <= self.x < x_c[self.i]+90:
            self.count+=1
            print(self.count)

        self.i+=1

class rock_obj:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.count=0


    def draw_obj(self):
        self.hitbox=(self.x,self.y,100,50)
        pygame.draw.rect(win,(255,0,255),self.hitbox,0)
        win.blit(pygame.transform.scale(rock[0],(100,50)),(self.x,self.y))

    def collide(self, rect):
        if  rect[1] < self.hitbox[1] and self.hitbox[0] < rect[0] <self.hitbox[0]+self.hitbox[2] :
            object_run.hit=True
        else:
            object_run.hit=False

object_run=object(300,20)

def rungame():

    object_run.scroll()
    if object_run.right==1:
        object_run.move_obj()
    if object_run.right==0:
        object_run.stay_obj()

    for obstacle in obstacles:
        obstacle.draw_obj()

    pygame.display.update()


pygame.time.set_timer(USEREVENT+1,r.randrange(3000,6000))
i=0
count=0
while run:

    for objects in obstacles:
        objects.collide(object_run.hitbox)
        objects.x-=2
        font = pygame.font.SysFont('comicsans', 20, True)
        win.blit(font.render("Score: " + str(count), 1, (255, 0, 0)), (10, 10))
        pygame.display.update()


    if object_run.hit==True:
        count+=1
        print(count)
        object_run.hit=False


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==USEREVENT+1:

            obstacles.append(rock_obj(r.randrange(500,800),100))
            pygame.display.update()



    keys=pygame.key.get_pressed()

    if not object_run.jump:

        if keys[pygame.K_RIGHT]:
            object_run.right=1

        else:
            object_run.right=0

        if keys[pygame.K_SPACE]:
            object_run.jump=True

    else:

        if object_run.counter >=-10:

            object_run.y-=(object_run.counter * abs(object_run.counter))*0.55
            object_run.counter-=1

        else:
            object_run.jump=False
            object_run.counter=10

    Clock.tick(FPS)
    rungame()
    pygame.display.update()