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

line_x = [-5,4]
line_y = [0,0]
line = MyLine(line_x, line_y, color = 'black',mfc='black', ms=12)
line.text.set_color('black')
line.text.set_fontsize(16)

line_x = [1,1]
line_y = [0,4]
line2 = MyLine(line_x, line_y, color = 'black', mfc='red', ms=12)
line2.text.set_color('black')
line2.text.set_fontsize(16)


line_x = [-1,-1]
line_y = [0,4]
line3 = MyLine(line_x, line_y, color = 'black', mfc='red', ms=12)
line3.text.set_color('black')
line3.text.set_fontsize(16)

line_x = [-4,-1]
line_y = [2.5,2.5]
line4 = MyLine(line_x, line_y,  color = 'black',mfc='red', ms=12)
line4.text.set_color('black')
line4.text.set_fontsize(16)

line_x = [-2.5,-2.5]
line_y = [2.5,4]
line5 = MyLine(line_x, line_y, color = 'black', mfc='red', ms=12)
line5.text.set_color('black')
line5.text.set_fontsize(16)
X1 = np.append(X1,X2)
Y1 = np.append(Y1,Y2)
fig, ax = plot.subplots()
ax.scatter(X,Y,c = 'g',lw = 0.1,label = r"$major$")
ax.scatter(X1,Y1,s = 100,c = 'r',marker = (5,1), lw=0.1,label = r"$anomaly$")
#ax.scatter(X2,Y2,s = 100,c = 'r',marker = (5,1), lw = 0.1,label = r"$anomaly$")
ax.text(-2,0,r"$split:1$",fontdict = font)
ax.text(1,3.5,r"$split:2$",fontdict = font)
ax.text(-1,3.5,r"$split:3$",fontdict = font)
ax.text(-2,2.5,r"$split:4$",fontdict = font)
ax.text(-2.5,3.5,r"$split:5$",fontdict = font)
ax.text(-3.85,3.7,r"$x$",fontdict = font_1)
ax.legend()
ax.add_line(line)
ax.add_line(line2)
ax.add_line(line3)
ax.add_line(line4)
ax.add_line(line5)
ax.spines['left'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['bottom'].set_color('black')
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
ax.set_yticks([])
ax.set_xticks([])
g_circle = plot.Circle(0,1, ec = 'black',fc="g")
r_circle = plot.Circle(0,1, ec = 'black',fc="r")
#ax.legend([g_circle,r_circle],[r"$major$",r"$anomaly$"])
ax.get_legend().get_frame().set_edgecolor('black')
#ax.legend.spines['left'].set_color('blue')
#ax.annotate('X',size = 20,xy=(-3.1,3.1),xytext=(-3.7,3.7),arrowprops=dict(facecolor='black', shrink=0.01,lw = 0.1))
ax.arrow(-3.7,3.7,0.6,-0.6,head_width = 0.07,head_length =0.1 ,fc = 'black',ec = 'black',color ='black')

plot.show()
