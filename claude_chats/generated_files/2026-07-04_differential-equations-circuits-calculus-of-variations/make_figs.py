import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 11,
    'axes.edgecolor': '#444',
    'axes.linewidth': 0.9,
    'axes.titlesize': 12,
    'figure.facecolor': 'white',
    'axes.facecolor': '#FDFDFB',
    'mathtext.fontset': 'dejavuserif',
})
INK   = '#1E2230'
BLUE  = '#2E4172'
TEAL  = '#2F6F6A'
AMBER = '#B7791F'
RED   = '#A23B3B'

# ---------------- Fig 1: RL growth / RC charging ----------------
fig, ax = plt.subplots(1, 2, figsize=(9.6, 3.6))
t = np.linspace(0, 5, 400)
ax[0].plot(t, 1 - np.exp(-t), color=BLUE, lw=2.2)
ax[0].axhline(1, ls='--', color='#999', lw=1)
ax[0].axvline(1, ls=':', color=AMBER, lw=1.4)
ax[0].plot([0, 1], [0, 1], ls='--', color=TEAL, lw=1.2)
ax[0].scatter([1], [1 - np.exp(-1)], color=RED, zorder=5, s=25)
ax[0].annotate('63.2% at $t=\\tau$', xy=(1, 0.632), xytext=(1.7, 0.42),
               arrowprops=dict(arrowstyle='->', color=INK, lw=0.9), fontsize=10)
ax[0].text(3.4, 1.03, '$i_{max}=E/R$', fontsize=10, color='#555')
ax[0].text(0.25, 0.9, 'initial slope\nhits max at $t=\\tau$', fontsize=9, color=TEAL)
ax[0].set_title('R–L growth:  $i=\\frac{E}{R}\\left(1-e^{-t/\\tau}\\right)$,  $\\tau=L/R$')
ax[0].set_xlabel('$t/\\tau$'); ax[0].set_ylabel('$i/i_{max}$'); ax[0].set_ylim(0, 1.15)

ax[1].plot(t, np.exp(-t), color=RED, lw=2.2, label='decay $e^{-t/\\tau}$')
ax[1].plot(t, 1 - np.exp(-t), color=BLUE, lw=2.2, label='charge $1-e^{-t/\\tau}$')
ax[1].axvline(1, ls=':', color=AMBER, lw=1.4)
ax[1].scatter([1, 1], [np.exp(-1), 1-np.exp(-1)], color=INK, zorder=5, s=22)
ax[1].text(1.1, 0.33, '36.8%', fontsize=9); ax[1].text(1.1, 0.68, '63.2%', fontsize=9)
ax[1].set_title('R–C:  charging & discharging,  $\\tau=RC$')
ax[1].set_xlabel('$t/\\tau$'); ax[1].set_ylabel('$q/q_{max}$'); ax[1].legend(frameon=False, fontsize=9)
for a in ax: a.grid(alpha=0.25, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/fig_rlrc.png', dpi=150); plt.close(fig)

# ---------------- Fig 2: three damping cases ----------------
fig, ax = plt.subplots(figsize=(9.6, 4.2))
t = np.linspace(0, 12, 800)
w0 = 2.0
b_u = 0.35
wd = np.sqrt(w0**2 - b_u**2)
x_u = np.exp(-b_u*t)*np.cos(wd*t)
ax.plot(t, x_u, color=BLUE, lw=1.9, label='underdamped  $\\beta<\\omega_0$')
ax.plot(t, np.exp(-b_u*t), ls='--', color=BLUE, lw=1.1, alpha=0.7)
ax.plot(t, -np.exp(-b_u*t), ls='--', color=BLUE, lw=1.1, alpha=0.7)
ax.text(6.3, 0.18, 'envelope $\\pm a e^{-\\beta t}$', color=BLUE, fontsize=10)
x_c = (1 + w0*t)*np.exp(-w0*t)
ax.plot(t, x_c, color=TEAL, lw=2.2, label='critically damped  $\\beta=\\omega_0$ (fastest return)')
b_o = 5.0
m1 = -b_o + np.sqrt(b_o**2 - w0**2); m2 = -b_o - np.sqrt(b_o**2 - w0**2)
A = -m2/(m1-m2); B = m1/(m1-m2)
x_o = A*np.exp(m1*t) + B*np.exp(m2*t)
ax.plot(t, x_o, color=AMBER, lw=2.2, label='overdamped  $\\beta>\\omega_0$ (sluggish, no oscillation)')
ax.axhline(0, color='#888', lw=0.8)
ax.set_xlabel('$t$'); ax.set_ylabel('$x(t)$')
ax.set_title('Damped free oscillations:  $\\ddot{x}+2\\beta\\dot{x}+\\omega_0^2 x=0$')
ax.legend(frameon=False, fontsize=10); ax.grid(alpha=0.25, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/fig_damping.png', dpi=150); plt.close(fig)

# ---------------- Fig 3: resonance amplitude + phase ----------------
fig, ax = plt.subplots(1, 2, figsize=(9.6, 3.9))
w = np.linspace(0.01, 2.5, 900); w0 = 1.0; F = 1.0
for b, c, lab in [(0.05, RED, '$\\beta=0.05\\,\\omega_0$ (high Q)'),
                  (0.15, BLUE, '$\\beta=0.15\\,\\omega_0$'),
                  (0.40, TEAL, '$\\beta=0.40\\,\\omega_0$'),
                  (0.7071, AMBER, '$\\beta=\\omega_0/\\sqrt{2}$ (no peak)')]:
    A = F/np.sqrt((w0**2-w**2)**2 + 4*b**2*w**2)
    ax[0].plot(w, A, color=c, lw=1.9, label=lab)
    if b < 0.7:
        wr = np.sqrt(w0**2 - 2*b**2)
        ax[0].scatter([wr], [F/np.sqrt((w0**2-wr**2)**2+4*b**2*wr**2)], color=c, s=18, zorder=5)
ax[0].axvline(1, ls=':', color='#777', lw=1)
ax[0].text(1.03, 8.6, '$\\omega_0$', fontsize=10, color='#555')
ax[0].annotate('peaks at $\\omega_r=\\sqrt{\\omega_0^2-2\\beta^2}<\\omega_0$',
               xy=(0.95, 9.5), xytext=(1.25, 7.4),
               arrowprops=dict(arrowstyle='->', lw=0.9), fontsize=9)
ax[0].set_xlabel('driving $\\omega$'); ax[0].set_ylabel('amplitude $A(\\omega)$')
ax[0].set_title('Amplitude resonance'); ax[0].set_ylim(0, 10.5)
ax[0].legend(frameon=False, fontsize=8.5)

for b, c in [(0.05, RED), (0.15, BLUE), (0.40, TEAL)]:
    phi = np.arctan2(2*b*w, (w0**2 - w**2))
    ax[1].plot(w, phi, color=c, lw=1.9)
ax[1].axhline(np.pi/2, ls='--', color='#888', lw=1)
ax[1].axvline(1, ls=':', color='#777', lw=1)
ax[1].set_yticks([0, np.pi/2, np.pi]); ax[1].set_yticklabels(['0', '$\\pi/2$', '$\\pi$'])
ax[1].text(1.05, 0.35, 'at $\\omega=\\omega_0$:\nlag is exactly $\\pi/2$\n(any damping)', fontsize=9)
ax[1].set_xlabel('driving $\\omega$'); ax[1].set_ylabel('phase lag $\\phi$')
ax[1].set_title('Phase of response behind driver')
for a in ax: a.grid(alpha=0.25, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/fig_resonance.png', dpi=150); plt.close(fig)

# ---------------- Fig 4: beats and secular resonance ----------------
fig, ax = plt.subplots(1, 2, figsize=(9.6, 3.6))
t = np.linspace(0, 60, 3000)
w0, w = 1.0, 1.1
xb = (2/(w0**2-w**2))*np.sin((w0-w)*t/2)*np.sin((w0+w)*t/2)
ax[0].plot(t, xb, color=BLUE, lw=1.2)
env = np.abs((2/(w0**2-w**2))*np.sin((w0-w)*t/2))
ax[0].plot(t, env, '--', color=RED, lw=1.2); ax[0].plot(t, -env, '--', color=RED, lw=1.2)
ax[0].set_title('$\\omega\\approx\\omega_0$, no damping: BEATS')
ax[0].set_xlabel('$t$'); ax[0].set_ylabel('$x$')
xr = t*np.sin(t)/2
ax[1].plot(t[:1500], xr[:1500], color=TEAL, lw=1.3)
ax[1].plot(t[:1500], t[:1500]/2, '--', color=RED, lw=1.2)
ax[1].plot(t[:1500], -t[:1500]/2, '--', color=RED, lw=1.2)
ax[1].text(9, 12.5, '$x=\\frac{F_0}{2m\\omega_0}\\,t\\sin\\omega_0 t$', fontsize=11, color=INK)
ax[1].set_title('$\\omega=\\omega_0$, no damping: amplitude grows $\\propto t$')
ax[1].set_xlabel('$t$'); ax[1].set_ylabel('$x$')
for a in ax: a.grid(alpha=0.25, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/fig_beats.png', dpi=150); plt.close(fig)

# ---------------- Fig 5: terminal velocity ----------------
fig, ax = plt.subplots(figsize=(7.2, 3.6))
t = np.linspace(0, 5, 400)
ax.plot(t, 1-np.exp(-t), color=BLUE, lw=2.2, label='fall: $v=v_T(1-e^{-kt/m})$')
ax.axhline(1, ls='--', color=RED, lw=1.3)
ax.text(3.3, 1.04, 'terminal velocity $v_T=mg/k$', color=RED, fontsize=10)
ax.text(0.4, 0.75, 'never actually reaches $v_T$\n(asymptote, $t\\to\\infty$)', fontsize=9, color='#555')
ax.set_xlabel('$t$ (units of $m/k$)'); ax.set_ylabel('$v/v_T$'); ax.set_ylim(0, 1.2)
ax.set_title('Fall with resistance $\\propto v$:  $m\\dot{v}=mg-kv$')
ax.grid(alpha=0.25, ls=':'); ax.legend(frameon=False, fontsize=10, loc='lower right')
fig.tight_layout(); fig.savefig('/home/claude/figs/fig_terminal.png', dpi=150); plt.close(fig)

# ---------------- Fig 6: LCR discharge (electrical damping) ----------------
fig, ax = plt.subplots(figsize=(9.6, 3.8))
t = np.linspace(0, 12, 900)
w0 = 2.0
for R2_4LC, c, lab in [(0.35, BLUE, '$R^2<4L/C$: oscillatory discharge'),
                       (2.0,  TEAL, '$R^2=4L/C$: critical, $R_c=2\\sqrt{L/C}$'),
                       (5.0,  AMBER, '$R^2>4L/C$: dead-beat (non-oscillatory)')]:
    b = R2_4LC
    if b < w0:
        wd = np.sqrt(w0**2-b**2)
        q = np.exp(-b*t)*(np.cos(wd*t) + b/wd*np.sin(wd*t))
    elif b == w0:
        q = (1+w0*t)*np.exp(-w0*t)
    else:
        s = np.sqrt(b**2-w0**2)
        m1, m2 = -b+s, -b-s
        q = (m1*np.exp(m2*t)-m2*np.exp(m1*t))/(m1-m2)
    ax.plot(t, q, color=c, lw=2.0, label=lab)
ax.axhline(0, color='#888', lw=0.8)
ax.set_xlabel('$t$'); ax.set_ylabel('$q(t)/q_0$')
ax.set_title('LCR discharge:  $L\\ddot{q}+R\\dot{q}+q/C=0$  — same mathematics as the damped spring')
ax.legend(frameon=False, fontsize=10); ax.grid(alpha=0.25, ls=':')
fig.tight_layout(); fig.savefig('/home/claude/figs/fig_lcr.png', dpi=150); plt.close(fig)

print("done")
