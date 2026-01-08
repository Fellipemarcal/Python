import cv2
import mediapipe as mp
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from sys import argv

# Initialisation correcte de GLUT
glutInit(argv)

# Initialisation Pygame + OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -7)
glEnable(GL_DEPTH_TEST)

# Initialisation MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
draw_utils = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Fonctions
def draw_cube(pos, size, color):
    glPushMatrix()
    glTranslatef(*pos)
    glColor3fv(color)
    glutSolidCube(size)
    glPopMatrix()

def check_collision(pos1, pos2, size=1.0):
    return (
        abs(pos1[0] - pos2[0]) < size and
        abs(pos1[1] - pos2[1]) < size and
        abs(pos1[2] - pos2[2]) < size
    )

# Positions initiales
cube1_pos = [0, 0, 0]
cube2_pos = [0, 0, 0]

# Boucle principale
running = True
while running:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    hand_positions = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            draw_utils.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            lm = handLms.landmark[9]
            x = (lm.x - 0.5) * 4
            y = -(lm.y - 0.5) * 3
            z = (lm.z) * 5
            hand_positions.append([x, y, z])

    if len(hand_positions) > 0:
        cube1_pos = hand_positions[0]
    if len(hand_positions) > 1:
        cube2_pos = hand_positions[1]

    # Collision
    collision = check_collision(cube1_pos, cube2_pos, size=1.0)
    color1 = [1, 0, 0] if collision else [0, 1, 0]
    color2 = [1, 0, 0] if collision else [0, 0, 1]

    # Affichage OpenGL
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube(cube1_pos, 1, color1)
    draw_cube(cube2_pos, 1, color2)
    pygame.display.flip()

    # Webcam
    cv2.imshow("Webcam", frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Nettoyage
cap.release()
cv2.destroyAllWindows()
pygame.quit()
