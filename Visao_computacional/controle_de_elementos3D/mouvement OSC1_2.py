import cv2
import mediapipe as mp
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialisation MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils

# Initialisation Pygame + OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -6)
glEnable(GL_DEPTH_TEST)

def draw_manual_cube(x, y, angle, scale, color):
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
        glColor3fv(color)
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

# Webcam
cap = cv2.VideoCapture(0)

# Positions des cubes
positions = [[0, 0], [0, 0]]
angles = [0, 0]
scales = [1.0, 1.0]
colors = [(1, 0, 0), (0, 0.5, 1)]  # rouge et bleu

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for i, handLms in enumerate(results.multi_hand_landmarks[:2]):
            draw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

            # Position centrale main (point 9)
            lm = handLms.landmark[9]
            positions[i][0] = (lm.x - 0.5) * 4
            positions[i][1] = -(lm.y - 0.5) * 3

            # Rotation
            p5 = handLms.landmark[5]
            p17 = handLms.landmark[17]
            dx = p17.x - p5.x
            angles[i] = dx * 180

            # Zoom (pouce 4 - index 8)
            p4 = handLms.landmark[4]
            p8 = handLms.landmark[8]
            dist = ((p4.x - p8.x) ** 2 + (p4.y - p8.y) ** 2) ** 0.5
            scales[i] = min(max(dist * 5, 0.5), 2)

    # Rendu OpenGL
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for i in range(2):
        draw_manual_cube(positions[i][0], positions[i][1], angles[i], scales[i], colors[i])
    pygame.display.flip()

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