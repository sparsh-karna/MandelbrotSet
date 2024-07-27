from __future__ import division
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GL import shaders

from sys import exit as exitsystem

from numpy import array

WIDTH, HEIGHT = 1920, 1080

zoomOut = 1.001
zoomIn = 0.999
movementSpeed = 0.002

def ReadFile(filename):
    with open(filename, 'r') as f:
        return f.read()

VERTEX_SHADER = ReadFile('./vertexShader.glsl')
FRAGMENT_SHADER = ReadFile('./fragmentShader.glsl')

class Main(object):
    def __init__(self):
        pygame.init()
        self.resolution = WIDTH, HEIGHT
        pygame.display.set_mode(self.resolution, DOUBLEBUF | OPENGL)
        pygame.display.set_caption('PyShadeToy')

        self.vertex_shader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
        self.fragment_shader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(self.vertex_shader, self.fragment_shader)

        self.uni_mouse = glGetUniformLocation(self.shader, 'iMouse')
        self.uni_ticks = glGetUniformLocation(self.shader, 'iTime')

        glUseProgram(self.shader)  
        glUniform2f(glGetUniformLocation(self.shader, 'iResolution'), *self.resolution)

        self.vertices = array([-1.0, -1.0, 0.0,
                               1.0, -1.0, 0.0,
                               1.0, 1.0, 0.0,
                               -1.0, 1.0, 0.0
                               ], dtype='float32')

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        self.clock = pygame.time.Clock()
        self.CenterX = glGetUniformLocation(self.shader, 'CenterX')
        self.CenterY = glGetUniformLocation(self.shader, 'CenterY')
        self.ZoomScale = glGetUniformLocation(self.shader, 'ZoomScale')
        self.ColorRanges = glGetUniformLocation(self.shader, "ColorRanges")

    def mainloop(self):
        x, y, z = 0.0, 0.0, 1.0
        cr = (0.0001, 0.33333, 0.66667, 1.00)

        while True:
            delta = self.clock.tick(60)

            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y += movementSpeed * z
                y = min(y, 1.0)

            if keys[pygame.K_DOWN]:
                y -= movementSpeed * z
                y = max(y, -1.0)

            if keys[pygame.K_LEFT]:
                x -= movementSpeed * z
                x = max(x, -1.0)

            if keys[pygame.K_RIGHT]:
                x += movementSpeed * z
                x = min(x, 1.0)

            if keys[pygame.K_w]:  # Zoom in
                z *= zoomIn
                z = min(z, 1.0)

            if keys[pygame.K_s]:  # Zoom out
                z *= zoomOut
                z = max(z, 0.01)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    exitsystem()

            glUseProgram(self.shader)
            glUniform2f(self.uni_mouse, *pygame.mouse.get_pos())
            glUniform1f(self.uni_ticks, pygame.time.get_ticks() / 1000.0)
            glUniform1f(self.CenterX, x)
            glUniform1f(self.CenterY, y)
            glUniform1f(self.ZoomScale, z)
            glUniform4f(self.ColorRanges, *cr)

            glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
            
            glDrawArrays(GL_QUADS, 0, 4)
            
            pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")
            pygame.display.flip()
  
if __name__ == '__main__':
    Main().mainloop()