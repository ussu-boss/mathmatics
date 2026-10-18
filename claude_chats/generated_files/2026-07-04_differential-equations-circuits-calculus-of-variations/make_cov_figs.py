import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams.update({
    'font.family': 'DejaVu Serif', 'font.size': 11,
    'axes.edgecolor': '#444', 'axes.linewidth': 0.9, 'axes.titlesize': 12,
    'figure.facecolor': 'white', 'axes.facecolor': '#FDFDFB',
    'mathtext.fontset': 'dejavuserif',
})
INK='#1C2128'; BLUE='#2E4172'; TEAL='#2F6F6A'; AMBER='#B7791F'; RED='#A23B3B'

# ---- Fig 1: family of varied paths ----
fig, ax = plt.subplots(figsize=(8.4, 4.0))
x = np.linspace(0, 1, 300)
y0 = 0.2 + 0.6*x + 0.25*np.sin(np.pi*x)          # extremal
eta = np.sin(np.pi*x)*np.sin(2.2*np.pi*x+0.4)     # variation shape (vanishes at ends)
for eps, alpha in [(-0.22,0.45),(-0.11,0.45),(0.11,0.45),(0.22,0.45)]:
    ax.plot(x, y0+eps*eta, color=TEAL, lw=1.1, alpha=alpha)
ax.plot(x, y0, color=BLUE, lw=2.6, label='extremal $y(x)$')
ax.plot(x, y0+0.22*eta, color=TEAL, lw=1.1)
ax.scatter([0,1],[y0[0],y0[-1]], color=RED, s=55, zorder=6)
ax.annotate('A $(x_1,y_1)$ fixed', xy=(0,y0[0]), xytext=(0.03,0.08), fontsize=11)
ax.annotate('B $(x_2,y_2)$ fixed', xy=(1,y0[-1]), xytext=(0.80,0.95), fontsize=11)
ax.annotate('varied paths\n$y+\\epsilon\\,\\eta(x)$,  $\\eta(x_1)=\\eta(x_2)=0$',
            xy=(0.52, y0[150]+0.22*eta[150]), xytext=(0.12,0.86),
            arrowprops=dict(arrowstyle='->', lw=0.9), fontsize=10.5, color=TEAL)
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_title("A functional $I[y]=\\int_{x_1}^{x_2}F(x,y,y')\\,dx$ assigns a number to each whole curve")
ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False, loc='lower right')
fig.tight_layout(); fig.savefig('/home/claude/figs/cov_paths.png', dpi=150); plt.close(fig)

# ---- Fig 2: brachistochrone ----
fig, ax = plt.subplots(figsize=(9.2, 4.4))
th = np.linspace(0, np.pi, 400)
a = 1/np.pi  # so that x runs 0..(a*pi)=1 at theta=pi ... choose endpoint B=(1, -2a)
xc = a*(th - np.sin(th)); yc = -a*(1 - np.cos(th))
ax.plot(xc, yc, color=RED, lw=2.8, label='cycloid (brachistochrone) — FASTEST')
xB, yB = xc[-1], yc[-1]
ax.plot([0,xB],[0,yB], color=BLUE, lw=2.0, ls='--', label='straight line — shortest, NOT fastest')
# circular arc through A,B sagging below the line
t = np.linspace(0,1,200)
sag = 0.55*np.sin(np.pi*t)
xa = t*xB; ya = t*yB - sag*0.35
ax.plot(xa, ya, color=TEAL, lw=1.6, ls=':', label='some other curve — slower than cycloid')
ax.scatter([0,xB],[0,yB], color=INK, s=55, zorder=6)
ax.annotate('A (start, at rest)', xy=(0,0), xytext=(0.03,0.06), fontsize=11)
ax.annotate('B', xy=(xB,yB), xytext=(xB-0.06,yB-0.09), fontsize=12)
ax.annotate('vertical start!\n(tangent is vertical at A)', xy=(0.005,-0.05), xytext=(0.16,-0.42),
            arrowprops=dict(arrowstyle='->', lw=0.9), fontsize=10, color=RED)
ax.text(0.52,-0.14,'gravity $g$', fontsize=11)
ax.annotate('', xy=(0.62,-0.30), xytext=(0.62,-0.16), arrowprops=dict(arrowstyle='->', lw=1.6, color=INK))
ax.set_xlabel('$x$'); ax.set_ylabel('$y$ (down is negative here)')
ax.set_title('Brachistochrone:  $x=a(\\theta-\\sin\\theta),\\ \\ y=a(1-\\cos\\theta)$ measured downward')
ax.legend(frameon=False, fontsize=10, loc='upper right'); ax.set_aspect('equal')
ax.grid(alpha=0.2, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/cov_brach.png', dpi=150); plt.close(fig)

# ---- Fig 3: catenary & soap film ----
fig = plt.figure(figsize=(9.6, 3.9))
ax1 = fig.add_subplot(1,2,1)
x = np.linspace(-1.2, 1.2, 300)
c = 0.6
y = c*np.cosh(x/c)
ax1.plot(x, y, color=BLUE, lw=2.4)
ax1.scatter([-1.2,1.2],[c*np.cosh(1.2/c)]*2, color=RED, s=45, zorder=5)
ax1.axvline(0, color='#999', lw=0.9, ls=':')
ax1.text(0.04, c+0.05, '$y_{min}=c$', fontsize=10)
ax1.set_title('Profile: catenary  $y=c\\,\\cosh\\dfrac{x-b}{c}$')
ax1.set_xlabel('$x$ (axis of revolution)'); ax1.set_ylabel('$y$')
ax1.grid(alpha=0.25, ls=':')
ax2 = fig.add_subplot(1,2,2, projection='3d')
xs = np.linspace(-1.2,1.2,60); ph = np.linspace(0,2*np.pi,60)
XS, PH = np.meshgrid(xs, ph)
R = c*np.cosh(XS/c)
Y = R*np.cos(PH); Z = R*np.sin(PH)
ax2.plot_surface(XS, Y, Z, alpha=0.55, color='#7C93C4', edgecolor='#46598A', linewidth=0.15)
th2 = np.linspace(0,2*np.pi,100)
r_end = c*np.cosh(1.2/c)
for xe in (-1.2, 1.2):
    ax2.plot(xe*np.ones_like(th2), r_end*np.cos(th2), r_end*np.sin(th2), color=RED, lw=2.2)
ax2.set_title('Soap film between two rings:\nminimal surface of revolution')
ax2.set_box_aspect((2.2,1.4,1.4)); ax2.set_axis_off()
fig.tight_layout(); fig.savefig('/home/claude/figs/cov_catenary.png', dpi=150); plt.close(fig)

# ---- Fig 4: geodesics on sphere and cylinder ----
fig = plt.figure(figsize=(9.6, 4.2))
ax1 = fig.add_subplot(1,2,1, projection='3d')
u, v = np.meshgrid(np.linspace(0,2*np.pi,50), np.linspace(0,np.pi,50))
ax1.plot_surface(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v),
                 alpha=0.25, color='#9FB3D8', edgecolor='none')
t = np.linspace(0,2*np.pi,200)
# great circle tilted
n = np.array([0.4,0.3,0.87]); n/=np.linalg.norm(n)
e1 = np.cross(n,[0,0,1]); e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
gc = np.outer(np.cos(t),e1)+np.outer(np.sin(t),e2)
ax1.plot(gc[:,0],gc[:,1],gc[:,2], color=RED, lw=2.4)
ax1.scatter(*gc[20], color=INK, s=40); ax1.scatter(*gc[90], color=INK, s=40)
ax1.set_title('Sphere: geodesic = GREAT circle\n(centre of circle = centre of sphere)')
ax1.set_box_aspect((1,1,1)); ax1.set_axis_off()
ax2 = fig.add_subplot(1,2,2, projection='3d')
ph2, z2 = np.meshgrid(np.linspace(0,2*np.pi,50), np.linspace(0,3,30))
ax2.plot_surface(np.cos(ph2), np.sin(ph2), z2, alpha=0.25, color='#A9CBC5', edgecolor='none')
tt = np.linspace(0, 4*np.pi, 300)
ax2.plot(np.cos(tt), np.sin(tt), 0.22*tt, color=TEAL, lw=2.4)
ax2.scatter([1],[0],[0], color=INK, s=40); ax2.scatter([np.cos(4*np.pi)],[np.sin(4*np.pi)],[0.22*4*np.pi], color=INK, s=40)
ax2.set_title('Cylinder: geodesic = HELIX\n(unroll the cylinder $\\to$ straight line)')
ax2.set_box_aspect((1,1,1.2)); ax2.set_axis_off()
fig.tight_layout(); fig.savefig('/home/claude/figs/cov_geodesic.png', dpi=150); plt.close(fig)

# ---- Fig 5: Rayleigh-Ritz trial function vs exact ----
fig, ax = plt.subplots(figsize=(8.6, 3.8))
xL = np.linspace(0,1,300)
psi_exact = np.sqrt(2)*np.sin(np.pi*xL)
psi_trial = xL*(1-xL); psi_trial /= np.sqrt(np.trapezoid(psi_trial**2, xL))
ax.plot(xL, psi_exact, color=BLUE, lw=2.3, label='exact ground state $\\sqrt{2}\\sin\\pi x$;  $E_1=\\pi^2\\hbar^2/2mL^2\\approx 9.87\\,\\epsilon$')
ax.plot(xL, psi_trial, color=RED, lw=2.3, ls='--', label='trial $\\psi= N\\,x(L-x)$;  $\\langle H\\rangle = 10\\,\\epsilon$ (above, as it must be!)')
ax.fill_between(xL, psi_exact, psi_trial, color='#F1D9A7', alpha=0.5)
ax.set_xlabel('$x/L$'); ax.set_ylabel('$\\psi$ (normalised)')
ax.set_title('Variational principle: any trial function gives $\\langle H\\rangle \\geq E_{ground}$   ($\\epsilon\\equiv\\hbar^2/2mL^2$)')
ax.legend(frameon=False, fontsize=9.5); ax.grid(alpha=0.25, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/cov_ritz.png', dpi=150); plt.close(fig)

print('done')
