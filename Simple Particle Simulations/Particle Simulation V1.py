import pygame
import random

#Sets up pygame screen for rendering
pygame.init()
screen_width = 1200
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))

#object class for particle objects with each having own x,y and velocities
class particle:
    def __init__(self,x,y,velocity_x,velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
    def move_x(self):
        self.x += self.velocity_x
    def move_y(self):
        self.y += self.velocity_y
    def change_vx(self):
        if random.random() < 0.5:
            self.velocity_x = 1
        else:
            self.velocity_x = -1
    def change_vy(self):
        if random.random() < 0.5:
            self.velocity_y = 1
        else:
            self.velocity_y = -1

#function renders rectangle
def render(x,y):
    thing = pygame.Rect((x,y,1,1))
    pygame.draw.rect(screen,(255,0,0),thing)

#function changes velocity based on screen borders
def particle_velocity_calculation(particle):
    if particle.y < 0 or particle.y > screen_height:
        particle.change_vy()

    if particle.x < 0 or particle.x > screen_width:
        particle.change_vx()

#Forms array of particles
particles =[particle(screen_height%2,screen_width%2,1,1)]

run = True
while run:
    screen.fill((0,0,0))

    #For each particle in the array, they move in x and y direction based on their velocity
    for i in range(len(particles)):
        particles[i].move_y()
        particles[i].move_x()
        #If the particle is about to collide with another particle it changes it's x and y values
        if (particles[i].x-particles[i-1].x) & (particles[i].y-particles[i-1].y):
            particles[i].change_vy()
            particles[i].change_vx()
        particle_velocity_calculation(particles[i])
        #Renders a rectangle which represent a particle in the array
        x=particles[i].x 
        y=particles[i].y
        render(x,y)

    #Press space bar and wherever your mouse is it can add and render more particles there
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        x,y=pygame.mouse.get_pos()
        particles.append(particle(x,y,1,1))

    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        run = False
    pygame.display.update()

pygame.quit()