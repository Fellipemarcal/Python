import cv2
import mediapipe as mp
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialisation MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils

# Initialisation Pygame + OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
glEnable(GL_DEPTH_TEST)

def draw_manual_cube(x, y, angle, scale):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(angle, 0, 1, 0)
    glScalef(scale, scale, scale)

    vertices = [
        [ 0.5,  0.5, -0.5],
        [ 0.5, -0.5, -0.5],
        [-0.5, -0.5, -0.5],
        [-0.5,  0.5, -0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5, -0.5,  0.5],
        [-0.5, -0.5,  0.5],
        [-0.5,  0.5,  0.5]
    ]

    surfaces = [
        (0,1,2,3),
        (4,5,6,7),
        (0,1,5,4),
        (2,3,7,6),
        (1,2,6,5),
        (0,3,7,4)
    ]

    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    ]

    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3f(0.2, 0.7, 1.0)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glPopMatrix()
    pygame.display.flip()

# Webcam
cap = cv2.VideoCapture(0)

x, y = 0, 0
angle = 0
scale = 1.0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

            # Position centrale main (point 9)
            lm = handLms.landmark[9]
            x = (lm.x - 0.5) * 4
            y = -(lm.y - 0.5) * 3

            # Rotation selon la main (diff entre 5 et 17)
            p5 = handLms.landmark[5]
            p17 = handLms.landmark[17]
            dx = p17.x - p5.x
            angle = dx * 180  # mise à l’échelle de l’angle

            # Zoom avec distance pouce (4) - index (8)
            p4 = handLms.landmark[4]
            p8 = handLms.landmark[8]
            dist = ((p4.x - p8.x) ** 2 + (p4.y - p8.y) ** 2) ** 0.5
            scale = min(max(dist * 5, 0.5), 2)  # Limite de zoom

    draw_manual_cube(x, y, angle, scale)

    cv2.imshow("Webcam", frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            pygame.quit()
            cv2.destroyAllWindows()
            quit()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
