#Teste de Esfera no Python
from vpython import *

sph = sphere(pos=vector(0,0,0),
             color=vector(1,2,5),
             shininess=1,
             radius=2,
             size=vector(1,1,1),
             texture=textures.stucco)
i = 1
dx = 0.1

while (i<=1000):
    rate(10)
    sph.pos.x = sph.pos.x + dx
    i += 1