import cv2
import mediapipe as mp
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialisation MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
draw_utils = mp.solutions.drawing_utils

# Initialisation Pygame + OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, display[0]/display[1], 0.1, 50.0)
glEnable(GL_DEPTH_TEST)
glTranslatef(0.0, 0.0, -8)

# Webcam
cap = cv2.VideoCapture(0)

def draw_manual_cube(size=1):
    hs = size / 2
    vertices = [
        [ hs,  hs, -hs], [ hs, -hs, -hs], [-hs, -hs, -hs], [-hs,  hs, -hs],
        [ hs,  hs,  hs], [ hs, -hs,  hs], [-hs, -hs,  hs], [-hs,  hs,  hs]
    ]
    surfaces = [
        (0,1,2,3), (4,5,6,7),
        (0,1,5,4), (2,3,7,6),
        (0,3,7,4), (1,2,6,5)
    ]
    glBegin(GL_QUADS)
    for face in surfaces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cube(x, y, z, size=1, color=(1, 1, 1)):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(*color)
    draw_manual_cube(size)
    glPopMatrix()

# Positions initiales des cubes
pos1 = [0, 0, 0]
pos2 = [0, 0, 0]

running = True

while running:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    # Mise à jour des positions avec les mains
    if results.multi_hand_landmarks and len(results.multi_hand_landmarks) >= 1:
        for idx, handLms in enumerate(results.multi_hand_landmarks[:2]):
            draw_utils.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            lm = handLms.landmark[0]  # poignet
            x = (lm.x - 0.5) * 6
            y = -(lm.y - 0.5) * 4
            z = (0.5 - lm.z) * 4
            if idx == 0:
                pos1 = [x, y, z]
            elif idx == 1:
                pos2 = [x, y, z]

    # Nettoyage de l'écran
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Dessin des cubes
    draw_cube(*pos1, size=1, color=(1, 0.5, 0.3))  # Cube 1 - orange
    draw_cube(*pos2, size=0.8, color=(0.3, 0.6, 1.0))  # Cube 2 - bleu

    # Affichage
    pygame.display.flip()
    cv2.imshow("Webcam", frame)

    # Événements Pygame / OpenCV
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False

cap.release()
cv2.destroyAllWindows()
pygame.quit()
