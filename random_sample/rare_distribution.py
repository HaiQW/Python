import numpy as np
import matplotlib.pyplot as plot
import matplotlib.mlab as mlab
from sklearn.neighbors import KernelDensity
from matplotlib.patches import Ellipse
def kde_sklearn(x, x_grid, bandwidth=0.2, **kwargs):
    """Kernel Density Estimation with Scikit-learn"""
    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(x[:, np.newaxis])
    # score_samples() returns the log-likelihood of the samples
    log_pdf = kde_skl.score_samples(x_grid[:, np.newaxis])
    return np.exp(log_pdf)


el = Ellipse((2, -1), 0.5, 0.5)
N = 2000
M = 100
s = np.random.normal(0,1,N)
y = np.random.normal(2,0.001,M)
z = np.append(s,y)
print z.size
x_grid = np.linspace(-10, 10, 1000)
fig,ax = plot.subplots()
ax.plot(x_grid, kde_sklearn(z,x_grid, bandwidth=0.15),label='bw={0}'.format(0.1), linewidth=4, alpha=0.7)
ax.annotate('rare class', xy=(2, 0.19),  xycoords='data',color = 'red',
                xytext=(100, 60), textcoords='offset points',
                size = '20',
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle= "fancy",
                                fc = "0.6",ec = "none",
                                patchB=el,
                                connectionstyle="angle3,angleA=0,angleB=-90"),
                )
ax.set_xlim(-10, 10)

n, bins, patches = ax.hist(z, 30,color = 'green', normed=True,alpha = 0.4)
plot.show()
