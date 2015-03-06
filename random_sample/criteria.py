import numpy as np
import matplotlib.pyplot as plot
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import matplotlib.text as mtext
class MyLine(lines.Line2D):

   def __init__(self, *args, **kwargs):
      # we'll update the position when the line data is set
      self.text = mtext.Text(0, 0, '')
      lines.Line2D.__init__(self, *args, **kwargs)

      # we can't access the label attr until *after* the line is
      # inited
      self.text.set_text(self.get_label())

   def set_figure(self, figure):
      self.text.set_figure(figure)
      lines.Line2D.set_figure(self, figure)

   def set_axes(self, axes):
      self.text.set_axes(axes)
      lines.Line2D.set_axes(self, axes)

   def set_transform(self, transform):
      # 2 pixel offset
      texttrans = transform + mtransforms.Affine2D().translate(1, 1)
      self.text.set_transform(texttrans)
      lines.Line2D.set_transform(self, transform)


   def set_data(self, x, y):
      if len(x):
         self.text.set_position((x[-1], y[-1]))

      lines.Line2D.set_data(self, x, y)

   def draw(self, renderer):
      # draw my label at the end of the line with 2 pixel offset
      lines.Line2D.draw(self, renderer)
      self.text.draw(renderer)

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 15,
        }
font_1 = {'family' : 'serif',
        'color'  : 'red',
        'weight' : 'normal',
        'size'   : 30,
        }
N = 3
T1 = np.random.rand(N)
T2 = np.random.rand(N)

r = np.sqrt( -2*0.0001* np.log(T1))
theta = 2 * np.pi * T2
X = r * np.sin(theta)
Y = r * np.cos(theta)

N = 20
T3 = np.random.rand(N)
T4 = np.random.rand(N)
r = np.sqrt( -2 * 0.001 * np.log(T3))
theta = 2 * np.pi * T4
X1 = r * np.sin(theta)
Y1 = r * np.cos(theta)-0.2


line_x = [-1,1]
line_y = [-0.00,-0.00]
line1 = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')


fig, ax = plot.subplots()
ax.scatter(X,Y,c = 'b',lw = 0.1,label = r"$anomaly$")
ax.scatter(X1,Y1,s = 100,c = 'r',marker = (5,1), lw=0.1,label = r"$rare$")
ax.add_line(line1)

#ax.set_xticks([])
g_circle = plot.Circle(0,1, fc="g")
r_circle = plot.Circle(0,1, fc="y")
ax.legend()
#ax.arrow(1,1.5,-0.5,-1.1,head_width = 0.07,head_length =0.1 ,fc = 'black',ec = 'black',color ='black')
#ax.text(1.1,1.6,r"$z$",fontdict = font_1)
ax.set_yticks([])
ax.set_xticks([])
plot.show()
