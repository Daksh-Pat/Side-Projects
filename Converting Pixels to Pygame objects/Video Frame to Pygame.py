import pygame
import cv2
import os

#initialize pygame module
pygame.init()

#Set screen size to video
screen_width = 480
screen_height = 360
screen = pygame.display.set_mode((screen_width,screen_height))

#Pygame clock used for setting framerate later
clock = pygame.time.Clock()

#Captures mp4 in directory
cap = cv2.VideoCapture(os.path.join('bad apple.mp4'))

#Counts total frames in mp4
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#Sets up array which will hold all the frames
frames_array=[]

for frame_idx in range(int(frames)):
    #Captures frame from mp4
    ret, frame = cap.read()

    #Converts frame from BGR to Grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Sets up frame in OpenCV2 video player
    cv2.imshow('Video Player', gray)

    #Adds Grayscale frame to frame array
    frames_array.append(gray)

    #Press q to close video
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

#Releases the capture and closes all OpenCV2 windows
cap.release()
cv2.destroyAllWindows()

#Manual frame counter so once the video ends pygame will close as well
frame_time = 0

#Function renders a pygame rectangle object in relation to the Grayscale value
#Uses argument of frame and scaling factor as a higher one will reduce quality but is faster
def render(frame,scaling):
    for y in range(0,len(frame),scaling):
        for x in range(0,len(frame[y]),scaling):
            if frame[y][x] > 50:
                pygame.draw.rect(screen,(0,0,240),(x,y,scaling,scaling))

run = True
while run:

    #Set to 30fps to match the original mp4
    screen.fill((0,0,0))
    clock.tick(30)

    #Closes program once all frames the frames in the array are rendered
    try:
        #Loads a frame from the array of frames and renders them
        frame = frames_array[frame_time]
        render(frame,3)
    except IndexError:
        run = False

    frame_time += 1

    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        run = False

    pygame.display.update()

pygame.quit()
