import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

# Initialisation Pygame + OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)  # recule la caméra pour voir le modèle

# Charge le modèle .obj (avec .mtl et textures dans le même dossier)
scene = pywavefront.Wavefront('skull.obj', collect_faces=True)

def draw_model():
    glBegin(GL_TRIANGLES)
    # Parcours tous les meshes dans la scène
    for name, mesh in scene.meshes.items():
        for face in mesh.faces:  # chaque face est une liste d'indices vertices
            for vertex_index in face:
                vertex = scene.vertices[vertex_index]
                glVertex3f(*vertex)
    glEnd()

def main():
    running = True
    rotation_angle = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(rotation_angle, 0, 1, 0)  # rotation autour de l'axe Y
        draw_model()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

        rotation_angle += 1  # pour faire tourner le modèle

    pygame.quit()

if __name__ == "__main__":
    main()
