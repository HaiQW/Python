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


N = 500
T1 = np.random.rand(N)
T2 = np.random.rand(N)

r = np.sqrt( -2 * np.log(T1))
theta = 2 * np.pi * T2
X = r * np.sin(theta)
Y = r * np.cos(theta)

N = 30
T3 = np.random.rand(N)
T4 = np.random.rand(N)


r = np.sqrt( -2 * 0.001 * np.log(T3))
theta = 2 * np.pi * T4
X1 = r * np.sin(theta)-0.5
Y1 = r * np.cos(theta)-1



line_x = [-5,4]
line_y = [0,0]
line = MyLine(line_x, line_y, mfc='red', ms=12, label='split:1')
line.text.set_color('black')
line.text.set_fontsize(16)

line_x = [-5,4]
line_y = [-1.5,-1.5]
line2 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:2')
line2.text.set_color('black')
line2.text.set_fontsize(16)


line_x = [0.5,0.5]
line_y = [-1.5,0]
line3 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:3')
line3.text.set_color('black')
line3.text.set_fontsize(16)

line_x = [-0,-0]
line_y = [-1.5,0]
line4 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:4')
line4.text.set_color('black')
line4.text.set_fontsize(16)

line_x = [-1,-1]
line_y = [-1.5,0]
line5 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:5')
line5.text.set_color('black')
line5.text.set_fontsize(16)

line_x = [-1,0]
line_y = [-0.5,-0.5]
line6 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:6')
line6.text.set_color('black')
line6.text.set_fontsize(16)

line_x = [-0.5,-0.5]
line_y = [-1.5,-0.5]
line7 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:7')
line7.text.set_color('black')
line7.text.set_fontsize(16)


line_x = [-0.5,-0]
line_y = [-1,-1]
line8 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:8')
line8.text.set_color('black')
line8.text.set_fontsize(16)

line_x = [-0.2,-0.2]
line_y = [-1,-0.5]
line9 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:9')
line9.text.set_color('black')
line9.text.set_fontsize(16)


line_x = [-0.5,-0.2]
line_y = [-0.8,-0.8]
line10 = MyLine(line_x, line_y, mfc='red', ms=12, label='split:10')
line10.text.set_color('black')
line10.text.set_fontsize(16)

fig, ax = plot.subplots()
ax.scatter(X,Y,c = 'g',lw = 0.1)
ax.scatter(X1,Y1,s = 100,c = 'y',marker = (5,1), lw=0.1)
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
ax.set_xlabel('X')
ax.set_ylabel('Y')
g_circle = plot.Circle(0,1, fc="g")
r_circle = plot.Circle(0,1, fc="y")
ax.legend([g_circle,r_circle],['major','rare'])
ax.annotate('X',size = 20,xy=(-0.45,-0.95),xytext=(-1,-2),arrowprops=dict(facecolor='black', shrink=0.01,lw = 0.1))

plot.show()
