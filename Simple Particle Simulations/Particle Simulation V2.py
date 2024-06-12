import pygame
import pymunk
import pymunk.pygame_util
import random

#Pygame positive values go down so flipped in pymunk so they match
pymunk.pygame_util.positive_y_is_up = False

#Initiates pygame and sets up screen size
pygame.init()
screen_width = 800
screen_height = 800

#Function forms dynamic pymunk particle with set elasticity and friction values of water
def create_particle(space,pos):
    body = pymunk.Body(1,1,body_type=pymunk.Body.DYNAMIC)
    body.position = (pos)
    shape = pymunk.Circle(body,8)
    space.add(body,shape)
    shape.elasticity = 0.4
    shape.friction = 0.51 
    return shape

#Function renders each pymunk particle in a particle array in blue
def draw_particle(particles):
    for particle in particles:
        x = int(particle.body.position.x)
        y = int(particle.body.position.y)
        color = (35,137,218)
        pygame.draw.circle(screen,color,(x,y),8)

#Function forms static pymunk object based on set position
def create_static_object(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,100)
    space.add(body,shape)
    return shape

#Function renders each pymunk static object in an object array, they are invisible
def draw_static_object(objects):
    for object in objects:
        x = int(object.body.position.x)
        y = int(object.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(x,y),50)

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

#Creates pymunk space for particles to interact in and sets it's gravity at 9.81m/s
space = pymunk.Space()
space.gravity = (0,981)

#Creating pymunk space to match screen boundaries
floor = pymunk.Segment(space.static_body,(0,screen_height),(screen_width,screen_height),8)
left = pymunk.Segment(space.static_body,(0,0),(0,screen_height),8)
right = pymunk.Segment(space.static_body,(screen_width,0),(screen_width,screen_height),8)
top = pymunk.Segment(space.static_body,(0,0),(screen_width,0),8)
space.add(floor,right,left,top)

#Initialize particle and obstruction object arrays
particles = []
obstructions=[]

run = True
while run:
	
    screen.fill((0,0,0))
    draw_particle(particles)
    #Particle updates match 60fps framerat
    space.step(1/60)
    clock.tick(60)
    #If the framerate does not go below 60fps it will continue to add particles into the simulation
    if clock.get_fps()>59:
        x=random.randint(0,800)
        y=random.randint(0,800)
        particles.append(create_particle(space,(x,y)))

    #Press space to create invisible obstruction for particles to interact with
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        x,y=pygame.mouse.get_pos()
        obstructions.append(create_static_object(space,(x,y)))
        draw_static_object(obstructions)

    #Press up arrow key to remove formed obstructions so particles do not interact with them
    if key[pygame.K_UP] == True:
        for obstruction in obstructions:
            space.remove(obstruction,obstruction.body)
            obstructions.remove(obstruction)

    #Print how many particles are being rendered on screen        
    print(len(particles))
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        run = False

    pygame.display.update()

pygame.quit()