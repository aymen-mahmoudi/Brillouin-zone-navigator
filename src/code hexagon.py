import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon


plt.rcParams['figure.figsize'] = [8, 5]
fig,ax = plt.subplots(1)



ax.set_aspect('equal')
gk = 2

hexagon = RegularPolygon((0,0), numVertices=6, radius=gk,ls='-', alpha=1, edgecolor='k')
hexagon2 = RegularPolygon((0,0), numVertices=4, radius=.2,ls='-', alpha=.3, edgecolor='k')
    
t2 = mpl.transforms.Affine2D().rotate_deg(30) + ax.transData
t3 = mpl.transforms.Affine2D().rotate_deg(45) + ax.transData
hexagon.set_transform(t2)
hexagon2.set_transform(t3)
k1_cord = (-1,0)
k2_cord = (1,0)
M1_cord = (0,-.87)
M2_cord = (0,.87)

w = .3
#tilt
l = 2


Rectangle1 = plt.Rectangle((0,0), w, l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')
Rectangle2 = plt.Rectangle((0,0), w, -l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')
Rectangle3 = plt.Rectangle((0,0), -w, l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')
Rectangle4 = plt.Rectangle((0,0), -w, -l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')

line1 = plt.Line2D((k1_cord[0],k2_cord[0]),(k1_cord[1],k2_cord[1]),ls='--',lw=2,color = 'blue')
line2 = plt.Line2D((M1_cord[0],M2_cord[0]),(M1_cord[1],M2_cord[1]),ls='--',lw=2,color = 'blue')

ax.add_patch(hexagon)
ax.add_patch(Rectangle1)
ax.add_patch(Rectangle2)
ax.add_patch(Rectangle3)
ax.add_patch(Rectangle4)
#ax.add_patch(hexagon2)
ax.add_line(line1)
ax.add_line(line2)

ax.set_xlim(0,10)
ax.set_ylim(0,3)

#plt.axis('scaled')
plt.autoscale(enable = True)
#plt.axis("off")

fig.tight_layout()