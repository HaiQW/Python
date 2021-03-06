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
N = 500
T1 = np.random.rand(N)
T2 = np.random.rand(N)

r = np.sqrt( -2 * np.log(T1))
theta = 2 * np.pi * T2
X = r * np.sin(theta)
Y = r * np.cos(theta)

N = 2
T3 = np.random.rand(N)
T4 = np.random.rand(N)


r = np.sqrt( -2 * 0.001 * np.log(T3))
theta = 2 * np.pi * T4
X1 = r * np.sin(theta)-3
Y1 = r * np.cos(theta)-3


N = 1
T5 = np.random.rand(N)
T6 = np.random.rand(N)


r = np.sqrt( -2 * 0.001 * np.log(T5))
theta = 2 * np.pi * T6
X2 = r * np.sin(theta)-3
Y2= r * np.cos(theta)+3

N = 20
T7 = np.random.rand(N)
T8 = np.random.rand(N)

r = np.sqrt( -2 * 0.001 * np.log(T7))
theta = 2 * np.pi * T8
X3 = r * np.sin(theta)-0.5
Y3 = r * np.cos(theta)-1

line_x = [-5,4]
line_y = [0,0]
line = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')
line.text.set_color('black')
line.text.set_fontsize(16)

line_x = [-5,4]
line_y = [-1.5,-1.5]
line2 = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')
line2.text.set_color('black')
line2.text.set_fontsize(16)


line_x = [0.5,0.5]
line_y = [-1.5,0]
line3 = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')
line3.text.set_color('black')
line3.text.set_fontsize(16)

line_x = [-0,-0]
line_y = [-1.5,0]
line4 = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')
line4.text.set_color('black')
line4.text.set_fontsize(16)

line_x = [-1,-1]
line_y = [-1.5,0]
line5 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line5.text.set_color('black')
line5.text.set_fontsize(16)

line_x = [-1,0]
line_y = [-0.5,-0.5]
line6 = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')
line6.text.set_color('black')
line6.text.set_fontsize(16)

line_x = [-0.5,-0.5]
line_y = [-1.5,-0.5]
line7 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line7.text.set_color('black')
line7.text.set_fontsize(16)


line_x = [-0.5,-0]
line_y = [-1,-1]
line8 = MyLine(line_x, line_y, mfc='red', ms=12,color = 'black')
line8.text.set_color('black')
line8.text.set_fontsize(16)

line_x = [-0.2,-0.2]
line_y = [-1,-0.5]
line9 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line9.text.set_color('black')
line9.text.set_fontsize(16)


line_x = [-0.5,-0.2]
line_y = [-0.8,-0.8]
line10 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line10.text.set_color('black')
line10.text.set_fontsize(16)

line_x = [-0.5,-0.2]
line_y = [-1,-1]
line11 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line11.text.set_color('black')
line11.text.set_fontsize(16)

line_x = [-0.5,-0.2]
line_y = [-0.9,-0.9]
line12 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line12.text.set_color('black')
line12.text.set_fontsize(16)

line_x = [-0.4,-0.4]
line_y = [-0.9,-1]
line13 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line13.text.set_color('black')
line13.text.set_fontsize(16)

line_x = [-0.45,-0.45]
line_y = [-0.9,-1]
line14 = MyLine(line_x, line_y, mfc='red', ms=12, color = 'black')
line14.text.set_color('black')
line14.text.set_fontsize(16)

X1 = np.append(X1,X2)
Y1 = np.append(Y1,Y2)
fig, ax = plot.subplots()
ax.scatter(X,Y,c = 'g',lw = 0.1,label = r"$major$")
ax.scatter(X1,Y1,s = 100,c = 'r',marker = (5,1), lw=0.1,label = r"$anomaly$")
ax.scatter(X3,Y3,s = 100,c = 'y',marker = (3,1), lw=0.1,label = r"$rare$")
ax.add_line(line)
ax.add_line(line2)
ax.add_line(line3)
ax.add_line(line4)
ax.add_line(line5)
ax.add_line(line6)
ax.add_line(line7)
ax.add_line(line8)
ax.add_line(line9)
ax.add_line(line10)
ax.add_line(line11)
ax.add_line(line12)
ax.add_line(line13)
ax.add_line(line14)
ax.set_yticks([])
ax.set_xticks([])
g_circle = plot.Circle(0,1, fc="g")
r_circle = plot.Circle(0,1, fc="y")
ax.legend()
ax.arrow(-1,-2,0.5,0.95,head_width = 0.07,head_length =0.1 ,fc = 'black',ec = 'black',color ='black')
ax.text(-1.3,-2.3,r"$y$",fontdict = font_1)

plot.show()
