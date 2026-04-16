from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

circulos = [
    (1.0, 0.5, 0.0, 0.0),  # Color azul, tamaño 0.5, posición (0.0, 0.0)
    (1.0, 0.2, -0.5, -0.5), # Color azul, tamaño 0.2, posición (-0.5, -0.5)
    (1.0, 0.2, 0.5, -0.5)   # Color azul, tamaño 0.2, posición (0.5, -0.5)
]



def draw_circle(x, y, radius, segments=100): # Funcion de circulo, no borrar

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y) 
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        glVertex2f(x + dx, y + dy)
    glEnd()


def display():


    glClear(GL_COLOR_BUFFER_BIT)

    for Color, tamaño, x, y in circulos:
        glColor3f(0.0, 0.0, Color)
        draw_circle(x, y, tamaño)

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    
    # ✅ Arreglo: codificar a UTF-8
    glutCreateWindow("Círculo en PyOpenGL".encode("utf-8"))

    init()

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()

