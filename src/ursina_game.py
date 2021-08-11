from typing import Collection
from ursina import *
import random as r

app = Ursina()
Sky()

bird = Animation("gif_bean.gif", collider='box')

camera.orthographic = True
camera.fov = 20


def update():
  bird.y = bird.y - 4*time.dt
  for p in pipes:
    p.x = p.x - 8*time.dt

  pipes[:] = [p for p in pipes if p.x >= -23]

  touch = bird.intersects()

  if touch.hit or bird.y < -10:
    quit()

def input(key):
  if key == 'space':
    bird.y = bird.y + 2
  if key == 'q':
      quit()

pipes = []

pipe = Entity(model='quad',
              color=color.green,
              texture='white_cube',
              position=(20,10),
              scale=(3,15,1),
              collider='box')

def newPipe():
  y = r.randint(4, 10)
  new1 = duplicate(pipe, y=y)
  new2 = duplicate(pipe, y=y-25)
  pipes.extend((new1, new2))
  invoke(newPipe, delay=3)

newPipe()


window.fullscreen = True
app.run()