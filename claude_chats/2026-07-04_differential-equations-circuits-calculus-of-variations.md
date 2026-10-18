# Differential equations in circuits and mechanics

| | |
|---|---|
| **Started** | 2026-07-04 03:18:42 |
| **Last updated** | 2026-07-04 03:43:20 |
| **Messages** | 4 |
| **Conversation id** | `43f7b385-688d-4b87-884a-19fe270d50bf` |

> Exported from the Claude data export (`conversations-000.zip`, 2026-08-28).
> Files Claude generated in-chat are reproduced inline below and saved separately
> under `generated_files/`.


---

### [1] **You** - 2026-07-04 03:18:47

Applications to differential equations.
1 . electric circuit( all types in l,r,c based)

1. mechanical engineering problems(i.e rectilinear motion,vertical motion,vertical elastic string,horizontal elatic string,simple harmonic motion,simple pendulum,oscillations of a spring(free,damped free,forced (without dampling), forced (with damping)
have to cover first  of all , all explanation with all possible tricky concepts and then show all with examples and mathematical solutions, and all should be drawn for tricky questions as well and csir point of view , go and do your best


---

### [2] **Claude** - 2026-07-04 03:29:49

*Searched project knowledge: `differential equations applications LCR circuit oscillations`*

*Searched project knowledge: `damped harmonic oscillator forced resonance quality factor`*

*Viewed `/mnt/skills/public/frontend-design/SKILL.md`*

**Command** - Check matplotlib availability

```bash
mkdir -p /home/claude/figs && cd /home/claude && pip list 2>/dev/null | grep -i matplotlib
```

**File created: `/home/claude/make_figs.py`** - Script to generate all physics graphs for the study document

```py
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
```

**Command** - Generate all graphs

```bash
cd /home/claude && python make_figs.py && ls -la figs/
```

**Command** - Write document header, styles, TOC and master-equation section

```bash
mkdir -p /home/claude/build && cat > /home/claude/build/part1.html << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Applications of Differential Equations — LCR Circuits &amp; Mechanical Oscillations (CSIR-NET)</title>
<script>
window.MathJax = { tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']] }, chtml: { scale: 1.0 } };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<style>
  :root{
    --paper:#F7F8F6; --ink:#1C2128; --indigo:#2E4172; --indigo-soft:#E7EBF4;
    --teal:#2F6F6A; --teal-soft:#E4F0EE; --amber:#9C6512; --amber-soft:#FBF1DD;
    --red:#A23B3B; --red-soft:#F7E7E7; --rule:#D8DAD4; --mut:#5B6068;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);
       font-family:Charter,'Bitstream Charter','Sitka Text',Georgia,serif;
       font-size:16.5px;line-height:1.62;}
  .wrap{max-width:920px;margin:0 auto;padding:28px 22px 90px;}
  header.doc{border-bottom:3px double var(--indigo);padding-bottom:18px;margin-bottom:8px;}
  .kicker{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:12px;letter-spacing:.22em;
          text-transform:uppercase;color:var(--indigo);font-weight:700;}
  h1{font-size:clamp(26px,4.4vw,38px);line-height:1.15;margin:.35em 0 .2em;font-weight:700;}
  .sub{color:var(--mut);font-style:italic;margin:0;}
  h2{font-size:24px;margin:2.2em 0 .5em;color:var(--indigo);border-bottom:1.5px solid var(--indigo);
     padding-bottom:6px;font-weight:700;}
  h2 .num{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:13px;letter-spacing:.14em;
     background:var(--indigo);color:#fff;padding:3px 9px;border-radius:3px;vertical-align:3px;margin-right:10px;}
  h3{font-size:19px;margin:1.7em 0 .35em;color:var(--ink);font-weight:700;}
  h3 .tag{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:11px;letter-spacing:.16em;
     text-transform:uppercase;color:var(--teal);display:block;font-weight:700;margin-bottom:2px;}
  p{margin:.55em 0 .9em}
  .box{border:1px solid var(--rule);border-left:5px solid var(--indigo);background:#fff;
       padding:12px 16px;margin:16px 0;border-radius:0 6px 6px 0;}
  .box .lbl{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:11px;font-weight:800;
       letter-spacing:.18em;text-transform:uppercase;color:var(--indigo);display:block;margin-bottom:4px;}
  .trick{border-left-color:var(--teal);background:var(--teal-soft);}
  .trick .lbl{color:var(--teal);}
  .trap{border-left-color:var(--amber);background:var(--amber-soft);}
  .trap .lbl{color:var(--amber);}
  .exam{border-left-color:var(--red);background:var(--red-soft);}
  .exam .lbl{color:var(--red);}
  .keyeq{background:var(--indigo-soft);border:1px solid #C3CDE2;border-radius:6px;
       padding:10px 16px;margin:16px 0;text-align:center;}
  table{border-collapse:collapse;width:100%;margin:16px 0;background:#fff;font-size:15.5px;}
  th{background:var(--indigo);color:#fff;font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;
     font-size:13px;letter-spacing:.05em;padding:8px 10px;text-align:left;}
  td{border:1px solid var(--rule);padding:7px 10px;vertical-align:top;}
  tr:nth-child(even) td{background:#FBFBF9;}
  figure{margin:20px 0;text-align:center;}
  figure img{max-width:100%;border:1px solid var(--rule);border-radius:6px;background:#fff;}
  figure svg{max-width:100%;height:auto;}
  figcaption{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:13px;color:var(--mut);
     margin-top:8px;}
  .ex{background:#fff;border:1px solid var(--rule);border-radius:8px;margin:20px 0;overflow:hidden;}
  .ex .q{padding:12px 16px;border-bottom:1px dashed var(--rule);}
  .ex .q .qn{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-weight:800;color:var(--red);
     font-size:13px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:4px;}
  .ex .s{padding:12px 16px;background:#FAFBF9;}
  .ex .s .sn{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-weight:800;color:var(--teal);
     font-size:13px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:4px;}
  .ans{display:inline-block;background:var(--ink);color:#fff;border-radius:4px;padding:1px 10px;
     font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:13.5px;font-weight:700;}
  ol,ul{margin:.4em 0 1em;padding-left:1.4em}
  li{margin:.3em 0}
  .toc{background:#fff;border:1px solid var(--rule);border-radius:8px;padding:14px 20px;margin:22px 0;}
  .toc b{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:12px;letter-spacing:.18em;
     text-transform:uppercase;color:var(--indigo);}
  .toc a{color:var(--ink);text-decoration:none;border-bottom:1px dotted var(--indigo);}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:0 26px;}
  @media(max-width:640px){.two{grid-template-columns:1fr}}
  code{font-family:ui-monospace,Consolas,monospace;font-size:.9em;background:#EEF0EC;padding:1px 5px;border-radius:3px;}
  .small{font-size:14px;color:var(--mut);}
</style>
</head>
<body><div class="wrap">

<header class="doc">
  <span class="kicker">CSIR-NET / GATE / JEST · Mathematical Physics &amp; Classical Mechanics</span>
  <h1>Applications of Differential Equations</h1>
  <p class="sub">Electric circuits (R, L, C in every combination) &nbsp;·&nbsp; Rectilinear &amp; vertical motion &nbsp;·&nbsp; Elastic strings &nbsp;·&nbsp; SHM &amp; the simple pendulum &nbsp;·&nbsp; Free, damped and forced spring oscillations — with every tricky concept, drawn figures and fully worked exam-style problems.</p>
</header>

<div class="toc">
  <b>Contents</b>
  <ol>
    <li><a href="#s0">The master equation — one ODE rules everything</a></li>
    <li><a href="#s1">Electric circuits: R–L, R–C, L–C, and the full L–C–R story</a></li>
    <li><a href="#s2">The electrical ↔ mechanical dictionary (score free marks)</a></li>
    <li><a href="#s3">Rectilinear &amp; vertical motion with resistance</a></li>
    <li><a href="#s4">Simple Harmonic Motion — the core facts and clock tricks</a></li>
    <li><a href="#s5">Vertical &amp; horizontal elastic strings (string ≠ spring!)</a></li>
    <li><a href="#s6">The simple pendulum and all its exam variations</a></li>
    <li><a href="#s7">Spring oscillations: free · damped · forced (undamped) · forced (damped)</a></li>
    <li><a href="#s8">Solved problems — CSIR style</a></li>
    <li><a href="#s9">One-page formula sheet &amp; trap list</a></li>
  </ol>
</div>

<!-- ============================================================ -->
<h2 id="s0"><span class="num">1</span>The Master Equation</h2>

<p>Almost everything in this topic — every circuit, every spring, every pendulum — is one and the same second-order linear ODE with constant coefficients:</p>

<div class="keyeq">\[ \ddot{x} + 2\beta\,\dot{x} + \omega_0^2\,x = f(t) \]</div>

<p>Here \(2\beta\) is the <b>damping coefficient per unit mass</b> (dimension of frequency), \(\omega_0\) is the <b>natural frequency</b>, and \(f(t)\) is the driving term. Substituting \(x=e^{mt}\) into the homogeneous part gives the <b>auxiliary equation</b></p>

<div class="keyeq">\[ m^2 + 2\beta m + \omega_0^2 = 0 \quad\Longrightarrow\quad m = -\beta \pm \sqrt{\beta^2-\omega_0^2} \]</div>

<table>
<tr><th>Case</th><th>Roots</th><th>General solution</th><th>Physics name</th></tr>
<tr><td>\(\beta<\omega_0\)</td><td>complex: \(-\beta\pm i\omega_d\), &nbsp; \(\omega_d=\sqrt{\omega_0^2-\beta^2}\)</td><td>\(x=a\,e^{-\beta t}\cos(\omega_d t+\varphi)\)</td><td><b>Underdamped</b> — oscillates inside a decaying envelope</td></tr>
<tr><td>\(\beta=\omega_0\)</td><td>repeated real: \(m=-\beta\) (twice)</td><td>\(x=(A+Bt)\,e^{-\beta t}\)</td><td><b>Critically damped</b> — fastest non-oscillatory return</td></tr>
<tr><td>\(\beta>\omega_0\)</td><td>two real negative: \(m_{1,2}=-\beta\pm\sqrt{\beta^2-\omega_0^2}\)</td><td>\(x=Ae^{m_1 t}+Be^{m_2 t}\)</td><td><b>Overdamped</b> — sluggish creep, no oscillation</td></tr>
</table>

<div class="box trick"><span class="lbl">Trick — read the answer off the equation</span>
Given \(\ddot{x}+2\beta\dot{x}+\omega_0^2x=0\) in an MCQ, don't "solve" it. Just <b>compare coefficients</b>: half the middle coefficient is \(\beta\); the square root of the last is \(\omega_0\). Then instantly: damped frequency \(\omega_d=\sqrt{\omega_0^2-\beta^2}\), quality factor \(Q=\omega_0/2\beta\), amplitude envelope \(e^{-\beta t}\), energy envelope \(e^{-2\beta t}\). Example: \(\ddot{x}+2\dot{x}+5x=0 \Rightarrow \beta=1,\ \omega_0=\sqrt5,\ \omega_d=2\).</div>

<div class="box trap"><span class="lbl">Trap — the repeated-root factor of \(t\)</span>
For critical damping the second solution is \(t\,e^{-\beta t}\), <em>not</em> another pure exponential. Options that offer \(x=(A+B)e^{-\beta t}\) (one constant effectively) are wrong — a 2nd-order ODE always needs <b>two independent constants</b>. The same "multiply by \(t\)" rule reappears at exact resonance of an undamped forced oscillator — that is not a coincidence, it is the same repeated-root mathematics.</div>

<div class="box"><span class="lbl">Particular integral you must know cold</span>
For driving \(f(t)=F\cos\omega t\) (or \(\sin\)), try \(x_p=A\cos(\omega t-\phi)\). Operator shortcut: replace \(D^2\to-\omega^2\) in \(1/F(D)\). If the denominator vanishes (resonance!), multiply by \(t\) and differentiate the denominator: \(\dfrac{1}{D^2+\omega_0^2}\cos\omega_0 t = \dfrac{t}{2\omega_0}\sin\omega_0 t.\)</div>
HTMLEOF
echo "part1 ok"
```

**Command** - Write electric circuits section with SVG circuit diagram

```bash
cat > /home/claude/build/part2.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="s1"><span class="num">2</span>Electric Circuits — R, L, C in Every Combination</h2>

<h3>2.1 The three elements and Kirchhoff's voltage law</h3>
<p>Every circuit equation is built by walking around the loop and demanding that the applied EMF equals the sum of the voltage drops (KVL):</p>

<table>
<tr><th>Element</th><th>Voltage drop</th><th>Stores</th><th>Continuity rule (huge exam trick)</th></tr>
<tr><td>Resistor \(R\)</td><td>\(V_R=Ri\)</td><td>nothing — dissipates \(i^2R\)</td><td>—</td></tr>
<tr><td>Inductor \(L\)</td><td>\(V_L=L\dfrac{di}{dt}\)</td><td>magnetic energy \(\tfrac12 Li^2\)</td><td><b>Current through \(L\) cannot jump</b> (else \(V_L\to\infty\))</td></tr>
<tr><td>Capacitor \(C\)</td><td>\(V_C=\dfrac{q}{C}\), with \(i=\dfrac{dq}{dt}\)</td><td>electric energy \(\tfrac{q^2}{2C}\)</td><td><b>Voltage/charge on \(C\) cannot jump</b> (else \(i\to\infty\))</td></tr>
</table>

<figure>
<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" font-family="Georgia,serif">
  <rect x="0" y="0" width="700" height="200" fill="#FFFFFF"/>
  <!-- wire loop -->
  <path d="M 90 160 L 90 60 L 150 60" stroke="#1C2128" stroke-width="2.4" fill="none"/>
  <path d="M 250 60 L 320 60" stroke="#1C2128" stroke-width="2.4" fill="none"/>
  <path d="M 430 60 L 500 60" stroke="#1C2128" stroke-width="2.4" fill="none"/>
  <path d="M 560 60 L 620 60 L 620 160 L 90 160" stroke="#1C2128" stroke-width="2.4" fill="none"/>
  <!-- AC source -->
  <circle cx="90" cy="110" r="22" fill="#fff" stroke="#A23B3B" stroke-width="2.4"/>
  <path d="M 76 110 q 7 -12 14 0 q 7 12 14 0" stroke="#A23B3B" stroke-width="2" fill="none"/>
  <text x="30" y="100" font-size="15" fill="#A23B3B">E(t)=</text>
  <text x="24" y="120" font-size="15" fill="#A23B3B">E&#8320;sin&#969;t</text>
  <!-- Resistor: zigzag -->
  <path d="M 150 60 l 10 -14 l 16 26 l 16 -26 l 16 26 l 16 -26 l 16 26 l 10 -12" stroke="#2E4172" stroke-width="2.6" fill="none"/>
  <text x="185" y="30" font-size="17" fill="#2E4172" font-style="italic">R</text>
  <!-- Inductor: coils -->
  <g stroke="#2F6F6A" stroke-width="2.6" fill="none">
    <path d="M 320 60 a 14 14 0 0 1 28 0"/>
    <path d="M 348 60 a 14 14 0 0 1 28 0"/>
    <path d="M 376 60 a 14 14 0 0 1 28 0"/>
    <path d="M 404 60 a 13 13 0 0 1 26 0"/>
  </g>
  <text x="368" y="24" font-size="17" fill="#2F6F6A" font-style="italic">L</text>
  <!-- Capacitor -->
  <line x1="500" y1="60" x2="522" y2="60" stroke="#1C2128" stroke-width="2.4"/>
  <line x1="522" y1="38" x2="522" y2="82" stroke="#9C6512" stroke-width="3"/>
  <line x1="538" y1="38" x2="538" y2="82" stroke="#9C6512" stroke-width="3"/>
  <line x1="538" y1="60" x2="560" y2="60" stroke="#1C2128" stroke-width="2.4"/>
  <text x="522" y="24" font-size="17" fill="#9C6512" font-style="italic">C</text>
  <!-- current arrow -->
  <path d="M 300 160 l 40 0" stroke="#A23B3B" stroke-width="2" marker-end="url(#arr)"/>
  <defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L7,3 L0,6 z" fill="#A23B3B"/></marker></defs>
  <text x="348" y="152" font-size="16" fill="#A23B3B" font-style="italic">i(t)</text>
  <!-- KVL note -->
  <text x="150" y="188" font-size="14.5" fill="#5B6068">KVL:&#160;&#160; L di/dt + Ri + q/C = E(t),&#160;&#160; i = dq/dt</text>
</svg>
<figcaption>Fig. 1 — The series L–C–R circuit. Every sub-case (R–L, R–C, L–C) is obtained by deleting one element.</figcaption>
</figure>

<h3>2.2 R–L circuit (first order — growth of current)</h3>
<p>KVL: \(L\dfrac{di}{dt}+Ri=E\). This is linear first order; integrating factor \(e^{Rt/L}\). With constant EMF and \(i(0)=0\):</p>
<div class="keyeq">\[ i(t)=\frac{E}{R}\Bigl(1-e^{-t/\tau}\Bigr),\qquad \boxed{\tau=\frac{L}{R}}\ \text{(time constant)} \]</div>
<ul>
<li>At \(t=\tau\): current reaches \(63.2\%\) of the final value; at \(t=5\tau\) it is essentially steady.</li>
<li><b>Decay</b> (source removed, circuit shorted): \(i=i_0e^{-t/\tau}\) — falls to \(36.8\%\) at \(t=\tau\).</li>
<li>Half-value time: \(t_{1/2}=\tau\ln 2\) (memorise; it is asked constantly).</li>
<li>Sinusoidal EMF \(E_0\sin\omega t\): after transients die, \[ i_{ss}=\frac{E_0}{\sqrt{R^2+\omega^2L^2}}\,\sin(\omega t-\phi),\qquad \tan\phi=\frac{\omega L}{R} \] — the current <b>lags</b> the voltage in an inductive circuit.</li>
</ul>

<h3>2.3 R–C circuit (first order — charging a capacitor)</h3>
<p>KVL in terms of charge: \(R\dfrac{dq}{dt}+\dfrac{q}{C}=E\). With \(q(0)=0\):</p>
<div class="keyeq">\[ q(t)=CE\Bigl(1-e^{-t/\tau}\Bigr),\qquad \boxed{\tau=RC},\qquad i(t)=\frac{E}{R}e^{-t/\tau} \]</div>
<div class="box trap"><span class="lbl">Trap — charge grows, current decays, simultaneously</span>
During <em>charging</em>, the charge rises as \(1-e^{-t/RC}\) but the <b>current is maximum at \(t=0\)</b> \((=E/R)\) and decays exponentially. At \(t=0\) an uncharged capacitor behaves like a <b>short circuit</b>; as \(t\to\infty\) it behaves like an <b>open circuit</b>. The inductor is exactly the opposite: open at \(t=0^+\), short in steady DC state. Many MCQ options are built purely on flipping these.</div>
<p><b>Discharge</b> through \(R\): \(q=q_0e^{-t/RC}\). Since energy \(\propto q^2\), the <b>energy decays twice as fast</b>: \(U=U_0e^{-2t/RC}\); energy halves in \(t=\frac{RC}{2}\ln2\).</p>

<figure><img src="{{FIG:fig_rlrc}}" alt="RL growth and RC charging curves"/>
<figcaption>Fig. 2 — First-order transients. Left: R–L current growth; the initial tangent reaches the final value exactly at \(t=\tau\). Right: R–C charging and discharging with the 63.2% / 36.8% landmarks.</figcaption></figure>

<h3>2.4 L–C circuit — pure electrical SHM</h3>
<p>No resistance: \(L\ddot q + \dfrac{q}{C}=0 \Rightarrow \ddot q + \dfrac{1}{LC}q=0\). The charge executes SHM:</p>
<div class="keyeq">\[ q=q_0\cos(\omega_0 t+\varphi),\qquad \boxed{\omega_0=\frac{1}{\sqrt{LC}}},\qquad f_0=\frac{1}{2\pi\sqrt{LC}} \]</div>
<p>Energy sloshes back and forth: \(\dfrac{q^2}{2C}+\dfrac{Li^2}{2}=\dfrac{q_0^2}{2C}=\) constant. When the capacitor is fully charged \(i=0\); when \(q=0\) the current is maximal, \(i_{max}=\omega_0q_0\). Exactly the position–velocity exchange of a mass on a spring.</p>

<h3>2.5 L–C–R free discharge — electrical damping</h3>
<p>KVL with all three elements and no source:</p>
<div class="keyeq">\[ L\ddot q+R\dot q+\frac{q}{C}=0 \;\Longrightarrow\; \ddot q+\underbrace{\frac{R}{L}}_{2\beta}\dot q+\underbrace{\frac{1}{LC}}_{\omega_0^2}q=0 \]</div>
<p>Compare with the master equation: \(\beta=\dfrac{R}{2L}\), \(\omega_0=\dfrac{1}{\sqrt{LC}}\). The discriminant condition \(\beta \lessgtr \omega_0\) becomes:</p>
<table>
<tr><th>Condition on R</th><th>Nature of discharge</th><th>Details</th></tr>
<tr><td>\(R^2<\dfrac{4L}{C}\)</td><td>Oscillatory (underdamped)</td><td>\(q=q_0e^{-Rt/2L}\cos(\omega_d t+\varphi)\), \(\ \omega_d=\sqrt{\dfrac{1}{LC}-\dfrac{R^2}{4L^2}}\)</td></tr>
<tr><td>\(R^2=\dfrac{4L}{C}\)</td><td>Critically damped</td><td>\(\boxed{R_c=2\sqrt{L/C}}\) — fastest dead-beat; the resistance \(\sqrt{L/C}\) itself is the "characteristic impedance"</td></tr>
<tr><td>\(R^2>\dfrac{4L}{C}\)</td><td>Non-oscillatory (dead-beat)</td><td>sum of two decaying exponentials</td></tr>
</table>

<figure><img src="{{FIG:fig_lcr}}" alt="LCR discharge three cases"/>
<figcaption>Fig. 3 — Discharge of a capacitor through L and R. The three curves are decided purely by comparing \(R\) with \(2\sqrt{L/C}\).</figcaption></figure>

<div class="box trick"><span class="lbl">Trick — instant Q factor of a circuit</span>
\[ Q=\frac{\omega_0}{2\beta}=\frac{\omega_0 L}{R}=\frac{1}{\omega_0 CR}=\frac{1}{R}\sqrt{\frac{L}{C}} \]
All four forms are equivalent — CSIR loves giving you the "wrong" pair of quantities to test whether you can convert. Also: energy of the free oscillation decays as \(e^{-Rt/L}\) (twice the amplitude rate).</div>

<h3>2.6 Forced L–C–R: AC source, impedance and resonance</h3>
<p>With \(E=E_0\sin\omega t\), the steady-state (particular integral) current is</p>
<div class="keyeq">\[ i_{ss}=\frac{E_0}{Z}\sin(\omega t-\phi),\qquad Z=\sqrt{R^2+\Bigl(\omega L-\frac{1}{\omega C}\Bigr)^2},\qquad \tan\phi=\frac{\omega L-\dfrac{1}{\omega C}}{R} \]</div>
<ul>
<li>\(\omega L>\dfrac{1}{\omega C}\): inductive circuit, current <b>lags</b> \((\phi>0)\). Opposite case: capacitive, current <b>leads</b>.</li>
<li><b>Series resonance</b> at \(\omega_0=\dfrac{1}{\sqrt{LC}}\): \(Z\) is minimum \((=R)\), current is maximum \((E_0/R)\), \(\phi=0\), power factor \(\cos\phi=1\) — the circuit looks purely resistive.</li>
<li><b>Voltage magnification:</b> at resonance \(V_L=V_C=Q\,E_0\) — the voltage across \(L\) or \(C\) individually can be far <em>larger</em> than the source (they are equal and opposite so they cancel in the loop). Classic conceptual MCQ.</li>
<li><b>Bandwidth:</b> half-power points where \(Z=\sqrt2\,R\); width \(\Delta\omega=\dfrac{R}{L}=2\beta\), so \(\boxed{Q=\omega_0/\Delta\omega}\) — sharpness of resonance.</li>
<li>Average power drawn: \(P=\dfrac{E_0 i_0}{2}\cos\phi = i_{rms}^2R\); maximum at resonance.</li>
</ul>

<div class="box trap"><span class="lbl">Trap — two different "resonances" in the same circuit</span>
The <b>current amplitude</b> (analogue of velocity) peaks <em>exactly</em> at \(\omega=1/\sqrt{LC}\), independent of \(R\). But the <b>charge amplitude</b> on the capacitor (analogue of displacement) peaks at the lower frequency \(\omega_q=\sqrt{\dfrac{1}{LC}-\dfrac{R^2}{2L^2}}\). If a question asks "at what frequency is the voltage across the capacitor maximum?", the answer is \(\omega_q\), <em>not</em> \(\omega_0\). This mirrors amplitude vs velocity resonance in mechanics (Sec. 8.4).</div>
HTMLEOF
echo "part2 ok"
```

**Command** - Write analogy table, rectilinear/vertical motion, SHM sections

```bash
cat > /home/claude/build/part3.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="s2"><span class="num">3</span>The Electrical ↔ Mechanical Dictionary</h2>
<p>The series LCR circuit and the damped-driven spring are the <em>same differential equation</em> wearing different clothes. Memorise this table and you solve two chapters for the price of one — CSIR frequently asks the mechanical question with electrical numbers or vice-versa.</p>

<table>
<tr><th>Mechanical</th><th>Electrical</th><th>Correspondence</th></tr>
<tr><td>\(m\ddot x + c\dot x + kx = F(t)\)</td><td>\(L\ddot q + R\dot q + \frac{q}{C} = E(t)\)</td><td>the governing ODE</td></tr>
<tr><td>displacement \(x\)</td><td>charge \(q\)</td><td>\(x\leftrightarrow q\)</td></tr>
<tr><td>velocity \(\dot x\)</td><td>current \(i=\dot q\)</td><td>\(v\leftrightarrow i\)</td></tr>
<tr><td>mass \(m\) (inertia)</td><td>inductance \(L\)</td><td>opposes change of \(v\) / \(i\)</td></tr>
<tr><td>damping constant \(c\)</td><td>resistance \(R\)</td><td>dissipates energy</td></tr>
<tr><td>spring constant \(k\)</td><td>reciprocal capacitance \(1/C\)</td><td>restoring agent</td></tr>
<tr><td>applied force \(F(t)\)</td><td>EMF \(E(t)\)</td><td>driver</td></tr>
<tr><td>kinetic energy \(\tfrac12 mv^2\)</td><td>magnetic energy \(\tfrac12 Li^2\)</td><td rowspan="2">energy pair</td></tr>
<tr><td>potential energy \(\tfrac12 kx^2\)</td><td>electric energy \(\tfrac{q^2}{2C}\)</td></tr>
<tr><td>\(\omega_0=\sqrt{k/m}\)</td><td>\(\omega_0=1/\sqrt{LC}\)</td><td>natural frequency</td></tr>
<tr><td>\(\beta=c/2m\), \(Q=\sqrt{km}/c\)</td><td>\(\beta=R/2L\), \(Q=\frac1R\sqrt{L/C}\)</td><td>damping / quality</td></tr>
</table>

<div class="box trick"><span class="lbl">Trick</span> Critical damping translates instantly: mechanical \(c^2=4mk\) &nbsp;⇄&nbsp; electrical \(R^2=4L/C\). Velocity resonance (at \(\omega_0\), any damping) ⇄ current resonance. Amplitude resonance (below \(\omega_0\)) ⇄ capacitor-charge resonance.</div>

<!-- ============================================================ -->
<h2 id="s3"><span class="num">4</span>Rectilinear &amp; Vertical Motion with Resistance</h2>

<h3>4.1 Choosing the right form of acceleration</h3>
<p>Newton's second law \(m a = F\) — but write \(a\) in the form that matches what the force depends on:</p>
<table>
<tr><th>Force depends on</th><th>Write acceleration as</th><th>Typical outcome</th></tr>
<tr><td>time \(t\)</td><td>\(\dfrac{dv}{dt}\)</td><td>\(v(t)\) directly</td></tr>
<tr><td>velocity \(v\), want \(v(t)\)</td><td>\(\dfrac{dv}{dt}\)</td><td>separable in \(t\)</td></tr>
<tr><td>velocity \(v\), want \(v(x)\); or force depends on position \(x\)</td><td>\(v\dfrac{dv}{dx}=\dfrac{d}{dx}\Bigl(\tfrac12v^2\Bigr)\)</td><td>energy-like relation \(v(x)\)</td></tr>
</table>
<div class="box trick"><span class="lbl">Trick</span> The single most common mark-loser is grinding \(dv/dt\) when the question asks for "speed after falling a distance \(h\)". The moment you see <b>distance</b> in the question, switch to \(v\,dv/dx\).</div>

<h3>4.2 Vertical fall, resistance \(\propto v\)</h3>
<p>Taking downward positive: \(m\dfrac{dv}{dt}=mg-kv\). Setting \(dv/dt=0\) gives the <b>terminal velocity</b> \(v_T=mg/k\). Solving (linear / separable) with \(v(0)=0\):</p>
<div class="keyeq">\[ v=v_T\Bigl(1-e^{-gt/v_T}\Bigr),\qquad x=v_T t-\frac{v_T^2}{g}\Bigl(1-e^{-gt/v_T}\Bigr) \]</div>
<figure><img src="{{FIG:fig_terminal}}" alt="terminal velocity approach"/>
<figcaption>Fig. 4 — Approach to terminal velocity: exponential saturation, exactly the same curve as R–L current growth (same ODE!).</figcaption></figure>

<p><b>Upward throw</b> with speed \(v_0\): \(m\dfrac{dv}{dt}=-mg-kv\) ⇒ time to the top \(t_{up}=\dfrac{v_T}{g}\ln\!\Bigl(1+\dfrac{v_0}{v_T}\Bigr)\), and greatest height (use \(v\,dv/dx\)) \(H=\dfrac{v_T}{g}\Bigl[v_0-v_T\ln\bigl(1+\tfrac{v_0}{v_T}\bigr)\Bigr]\).</p>

<h3>4.3 Resistance \(\propto v^2\)</h3>
<p><b>Falling:</b> \(m\dfrac{dv}{dt}=mg-kv^2\), terminal \(v_T=\sqrt{mg/k}\):</p>
<div class="keyeq">\[ v=v_T\tanh\!\Bigl(\frac{gt}{v_T}\Bigr) \qquad\text{and (via } v\,dv/dx\text{)}\qquad v^2=v_T^2\Bigl(1-e^{-2gx/v_T^2}\Bigr) \]</div>
<p><b>Rising:</b> \(m\,v\dfrac{dv}{dx}=-mg-kv^2\) gives height \(H=\dfrac{v_T^2}{2g}\ln\!\Bigl(1+\dfrac{v_0^2}{v_T^2}\Bigr)\), and time up \(t_{up}=\dfrac{v_T}{g}\tan^{-1}\dfrac{v_0}{v_T}\).</p>

<div class="box trap"><span class="lbl">Traps that decide the mark</span>
<ul style="margin:.2em 0">
<li>The body <b>never actually reaches</b> \(v_T\) — it is an asymptote. "Time to reach terminal velocity" is a trick option; only "time to reach \(\,0.63\,v_T\)" etc. is finite.</li>
<li>With resistance, <b>time of ascent &lt; time of descent</b>, and the return speed at the launch point is <b>less</b> than the launch speed (energy lost to drag). Undamped intuition (\(t_{up}=t_{down}\)) is the wrong option.</li>
<li>Sign discipline: while rising, both gravity and drag point down; while falling they oppose. Never carry one equation through the top.</li>
<li>Dimensional shortcut: in \(mg-kv\), \([k]=\) kg/s; in \(mg-kv^2\), \([k]=\) kg/m. Checking which \(v_T\) formula is dimensionally sane kills wrong options instantly.</li>
</ul></div>

<!-- ============================================================ -->
<h2 id="s4"><span class="num">5</span>Simple Harmonic Motion — Core Facts and Clock Tricks</h2>

<p><b>Definition (as an ODE):</b> acceleration proportional to displacement and directed towards a fixed point:</p>
<div class="keyeq">\[ \ddot x=-\omega^2x \;\Longrightarrow\; x=a\sin(\omega t+\varphi),\qquad T=\frac{2\pi}{\omega} \]</div>
<p>First integral (multiply by \(\dot x\) and integrate, or use \(v\,dv/dx=-\omega^2x\)):</p>
<div class="keyeq">\[ v^2=\omega^2\bigl(a^2-x^2\bigr) \]</div>
<table>
<tr><th>Quantity</th><th>At centre \(x=0\)</th><th>At extreme \(x=\pm a\)</th></tr>
<tr><td>speed</td><td>maximum \(=a\omega\)</td><td>zero</td></tr>
<tr><td>acceleration</td><td>zero</td><td>maximum \(=a\omega^2\)</td></tr>
<tr><td>KE / PE</td><td>all KE</td><td>all PE</td></tr>
</table>
<ul>
<li>Period is <b>independent of amplitude</b> (isochronism) — the hallmark of a linear restoring force.</li>
<li>Average KE over a cycle = average PE = \(\tfrac14 m\omega^2a^2\); total \(E=\tfrac12 m\omega^2a^2\).</li>
<li>KE = PE when \(x=\pm a/\sqrt2\), <em>not</em> at \(a/2\) — a beloved trap.</li>
</ul>
<div class="box trick"><span class="lbl">Trick — the circle clock (timing questions in 10 seconds)</span>
Project uniform circular motion: \(x=a\cos\omega t\). Time to go from a point to another = (angle swept)/\(\omega\).
<ul style="margin:.3em 0">
<li>centre → \(a/2\): angle \(30^\circ\) ⇒ time \(=T/12\)</li>
<li>extreme → \(a/2\): angle \(60^\circ\) ⇒ time \(=T/6\) &nbsp;(twice as long — motion is slow near the extremes!)</li>
<li>centre → \(a/\sqrt2\): \(T/8\);&nbsp; centre → extreme: \(T/4\).</li>
</ul>
Never integrate for these; read them off the reference circle.</div>
HTMLEOF
echo "part3 ok"
```

**Command** - Write elastic strings section with two SVG setup diagrams

```bash
cat > /home/claude/build/part4.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="s5"><span class="num">6</span>Elastic Strings — Vertical and Horizontal (a string is NOT a spring)</h2>

<h3>6.1 Hooke's law for a string, and the one fact that changes everything</h3>
<p>For an elastic string of <b>natural length</b> \(l\) and <b>modulus of elasticity</b> \(\lambda\) (units of force), stretched by extension \(s\):</p>
<div class="keyeq">\[ T=\frac{\lambda s}{l} \qquad\text{(equivalent spring constant } k=\lambda/l\text{)} \]</div>
<div class="box trap"><span class="lbl">The defining trap</span>
A <b>spring</b> obeys \(F=-kx\) for both extension <em>and</em> compression. A <b>string can only pull, never push</b>: the instant its length drops below the natural length \(l\), the tension vanishes and the particle moves <em>freely</em>. So a string gives SHM only while taut; large-amplitude motion becomes a <b>patchwork of SHM + free motion</b>, and the "period" must be assembled piece by piece. This single fact generates most string questions.</div>

<h3>6.2 Vertical elastic string (or vertical spring)</h3>

<figure>
<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" font-family="Georgia,serif">
  <rect width="720" height="300" fill="#fff"/>
  <!-- ceiling -->
  <line x1="60" y1="30" x2="420" y2="30" stroke="#1C2128" stroke-width="3"/>
  <g stroke="#888" stroke-width="1.4">
    <line x1="70" y1="30" x2="60" y2="18"/><line x1="100" y1="30" x2="90" y2="18"/>
    <line x1="130" y1="30" x2="120" y2="18"/><line x1="160" y1="30" x2="150" y2="18"/>
    <line x1="190" y1="30" x2="180" y2="18"/><line x1="220" y1="30" x2="210" y2="18"/>
    <line x1="250" y1="30" x2="240" y2="18"/><line x1="280" y1="30" x2="270" y2="18"/>
    <line x1="310" y1="30" x2="300" y2="18"/><line x1="340" y1="30" x2="330" y2="18"/>
    <line x1="370" y1="30" x2="360" y2="18"/><line x1="400" y1="30" x2="390" y2="18"/>
  </g>
  <!-- natural length string -->
  <line x1="120" y1="30" x2="120" y2="130" stroke="#2F6F6A" stroke-width="2.4"/>
  <circle cx="120" cy="140" r="10" fill="#E4F0EE" stroke="#2F6F6A" stroke-width="2"/>
  <text x="70" y="170" font-size="14" fill="#2F6F6A">no mass:</text>
  <text x="70" y="188" font-size="14" fill="#2F6F6A">natural length l</text>
  <!-- equilibrium -->
  <line x1="280" y1="30" x2="280" y2="190" stroke="#2E4172" stroke-width="2.4"/>
  <circle cx="280" cy="202" r="12" fill="#E7EBF4" stroke="#2E4172" stroke-width="2.2"/>
  <text x="273" y="207" font-size="13" fill="#2E4172">m</text>
  <!-- brackets -->
  <path d="M 440 30 L 452 30 L 452 130 L 440 130" stroke="#2F6F6A" stroke-width="1.6" fill="none"/>
  <text x="460" y="85" font-size="15" fill="#2F6F6A" font-style="italic">l</text>
  <path d="M 440 130 L 452 130 L 452 190 L 440 190" stroke="#9C6512" stroke-width="1.6" fill="none"/>
  <text x="460" y="165" font-size="15" fill="#9C6512">e = mgl/&#955;</text>
  <line x1="60" y1="130" x2="452" y2="130" stroke="#2F6F6A" stroke-width="1" stroke-dasharray="6 5"/>
  <text x="475" y="134" font-size="13.5" fill="#2F6F6A">natural-length level (string goes slack above this!)</text>
  <line x1="60" y1="190" x2="452" y2="190" stroke="#2E4172" stroke-width="1" stroke-dasharray="6 5"/>
  <text x="475" y="194" font-size="13.5" fill="#2E4172">equilibrium: mg = &#955;e/l &#8594; centre of SHM</text>
  <!-- oscillation arrows -->
  <path d="M 280 225 l 0 30" stroke="#A23B3B" stroke-width="2" marker-end="url(#arr2)"/>
  <path d="M 280 178 l 0 -18" stroke="#A23B3B" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L7,3 L0,6 z" fill="#A23B3B"/></marker></defs>
  <text x="300" y="245" font-size="14" fill="#A23B3B">SHM about equilibrium, amplitude a</text>
  <text x="300" y="264" font-size="14" fill="#A23B3B">pure SHM only if a &#8804; e (string stays taut)</text>
</svg>
<figcaption>Fig. 5 — Vertical elastic string: natural length \(l\), equilibrium extension \(e\), and the slack region above the natural-length level.</figcaption>
</figure>

<p><b>Step 1 — equilibrium.</b> Hanging mass \(m\) stretches the string by \(e\) where \(mg=\dfrac{\lambda e}{l}\), i.e. \(e=\dfrac{mgl}{\lambda}\).</p>
<p><b>Step 2 — displace by \(x\) below equilibrium.</b> Measuring \(x\) downward from the <em>equilibrium</em> position:</p>
\[ m\ddot x = mg - \frac{\lambda}{l}(e+x) = \underbrace{mg-\frac{\lambda e}{l}}_{=0} - \frac{\lambda}{l}x = -\frac{\lambda}{l}x \]
<div class="keyeq">\[ \ddot x=-\frac{\lambda}{ml}\,x=-\frac{g}{e}\,x \quad\Longrightarrow\quad \boxed{T=2\pi\sqrt{\frac{e}{g}}=2\pi\sqrt{\frac{ml}{\lambda}}=2\pi\sqrt{\frac{m}{k}}} \]</div>

<div class="box trick"><span class="lbl">Three exam-winning consequences</span>
<ol style="margin:.2em 0">
<li><b>Gravity does not appear in the period.</b> It only shifts the centre of oscillation down by \(e\). A vertical spring and a horizontal spring with the same \(m,k\) have identical periods.</li>
<li><b>The "static extension" shortcut:</b> \(T=2\pi\sqrt{e/g}\). Told only that a load stretches a spring by \(e=4\) cm? Then \(T=2\pi\sqrt{0.04/9.8}\approx0.4\) s. No \(m\), no \(k\) needed. This is a very frequent one-liner.</li>
<li><b>Energy method:</b> \(E=\tfrac12 m\dot x^2+\tfrac12 kx^2\) (measuring \(x\) from equilibrium absorbs gravity completely). Differentiating \(dE/dt=0\) regenerates the SHM equation — the fastest derivation in the exam hall.</li>
</ol></div>

<div class="box trap"><span class="lbl">Trap — amplitude larger than \(e\) (string only)</span>
If the amplitude \(a>e\), the particle rises above the natural-length level, the string goes <b>slack</b>, and the motion becomes <b>free flight under gravity</b> (a vertical projectile) until the string tightens again. The full period is then
\[ T=\underbrace{2\Bigl[\pi-\cos^{-1}\Bigl(\frac{e}{a}\Bigr)\Bigr]\sqrt{\frac{e}{g}}}_{\text{taut: partial SHM arc}}\;+\;\underbrace{\frac{2v_1}{g}}_{\text{free flight up and down}},\qquad v_1=\omega\sqrt{a^2-e^2} \]
where \(v_1\) is the speed at the natural-length point (from \(v^2=\omega^2(a^2-x^2)\) at \(x=e\) above equilibrium). You are rarely asked to reproduce this formula — you <em>are</em> asked whether the motion "remains simple harmonic" (No) and where each phase begins (at the natural-length level, not at equilibrium). For a <b>spring</b>, motion stays SHM at any amplitude (it can push).</div>

<h3>6.3 Horizontal elastic string on a smooth table</h3>

<figure>
<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" font-family="Georgia,serif">
  <rect width="760" height="240" fill="#fff"/>
  <!-- table -->
  <line x1="30" y1="150" x2="730" y2="150" stroke="#1C2128" stroke-width="3"/>
  <g stroke="#999" stroke-width="1.2">
    <line x1="60" y1="150" x2="48" y2="164"/><line x1="120" y1="150" x2="108" y2="164"/>
    <line x1="180" y1="150" x2="168" y2="164"/><line x1="240" y1="150" x2="228" y2="164"/>
    <line x1="300" y1="150" x2="288" y2="164"/><line x1="360" y1="150" x2="348" y2="164"/>
    <line x1="420" y1="150" x2="408" y2="164"/><line x1="480" y1="150" x2="468" y2="164"/>
    <line x1="540" y1="150" x2="528" y2="164"/><line x1="600" y1="150" x2="588" y2="164"/>
    <line x1="660" y1="150" x2="648" y2="164"/><line x1="716" y1="150" x2="704" y2="164"/>
  </g>
  <text x="290" y="185" font-size="14" fill="#5B6068">smooth (frictionless) table</text>
  <!-- fixed peg -->
  <circle cx="90" cy="130" r="7" fill="#1C2128"/>
  <text x="66" y="112" font-size="14" fill="#1C2128">fixed end O</text>
  <!-- string taut -->
  <line x1="97" y1="130" x2="560" y2="130" stroke="#2F6F6A" stroke-width="2.6"/>
  <circle cx="575" cy="130" r="13" fill="#E7EBF4" stroke="#2E4172" stroke-width="2.2"/>
  <text x="568" y="135" font-size="13" fill="#2E4172">m</text>
  <!-- markers -->
  <line x1="400" y1="95" x2="400" y2="150" stroke="#2F6F6A" stroke-width="1.4" stroke-dasharray="5 4"/>
  <text x="352" y="88" font-size="13.5" fill="#2F6F6A">natural length point N (x = l)</text>
  <path d="M 97 62 L 97 74 L 400 74 L 400 62" stroke="#2F6F6A" stroke-width="1.4" fill="none"/>
  <text x="240" y="58" font-size="15" fill="#2F6F6A" font-style="italic">l</text>
  <path d="M 400 62 L 400 74 L 575 74 L 575 62" stroke="#9C6512" stroke-width="1.4" fill="none"/>
  <text x="472" y="58" font-size="15" fill="#9C6512">extension a</text>
  <!-- zones -->
  <rect x="400" y="200" width="330" height="26" fill="#E4F0EE" stroke="#2F6F6A" stroke-width="1"/>
  <text x="428" y="218" font-size="13.5" fill="#2F6F6A">string taut &#8594; SHM, &#969;&#178; = &#955;/(ml)</text>
  <rect x="30" y="200" width="370" height="26" fill="#FBF1DD" stroke="#9C6512" stroke-width="1"/>
  <text x="60" y="218" font-size="13.5" fill="#9C6512">string slack &#8594; NO force &#8594; constant velocity a&#969;</text>
</svg>
<figcaption>Fig. 6 — Horizontal elastic string: SHM zone (beyond the natural length) and free zone (inside it).</figcaption>
</figure>

<p>Particle on a smooth horizontal table, tied by an elastic string (natural length \(l\), modulus \(\lambda\)) to a fixed point \(O\); pulled to extension \(a\) and released. Gravity is balanced by the table, so the only horizontal force is tension.</p>
<ol>
<li><b>While extended</b> (\(x>l\) from \(O\)): \(m\ddot s=-\dfrac{\lambda}{l}s\) where \(s\) is the extension ⇒ SHM with \(\omega=\sqrt{\lambda/ml}\) <em>centred at the natural-length point \(N\)</em>. From \(x=l+a\) it reaches \(N\) in a <b>quarter period</b> \(\dfrac{\pi}{2\omega}\), arriving with speed \(v=a\omega\).</li>
<li><b>Past \(N\)</b> the string is slack: zero force ⇒ the particle glides at <b>constant speed \(a\omega\)</b>, passes over/through \(O\) (idealised), and travels the slack stretch of length \(2l\) in time \(\dfrac{2l}{a\omega}\), until the string becomes taut on the far side.</li>
<li>There it does another half-SHM (in, stop at extension \(a\), out — by symmetry/energy the extension is again \(a\)), returns, glides back, and completes the cycle.</li>
</ol>
<div class="keyeq">\[ T=\underbrace{2\pi\sqrt{\frac{ml}{\lambda}}}_{\text{4 quarter-SHM arcs}}\;+\;\underbrace{\frac{4l}{a\omega}}_{\text{2 slack glides}} \qquad\text{(periodic, but NOT simple harmonic)} \]</div>
<div class="box trap"><span class="lbl">Traps</span>
<ul style="margin:.2em 0">
<li>The centre of the SHM piece is the <b>natural-length point</b>, not the fixed end \(O\).</li>
<li>The composite motion is <b>periodic but not SHM</b> — "the particle executes SHM" is the classic wrong option.</li>
<li>The slack-glide time depends on amplitude \(a\); hence the total period is <b>amplitude-dependent</b>, unlike genuine SHM. That amplitude-dependence is itself an MCQ discriminator.</li>
<li>If instead the mass is between <b>two stretched springs/strings that never go slack</b>, effective constants add: \(k_{\rm eff}=k_1+k_2\) (parallel action), and the motion <em>is</em> pure SHM.</li>
</ul></div>
HTMLEOF
echo "part4 ok"
```

**Command** - Write pendulum (with SVG) and complete spring-oscillation regimes

```bash
cat > /home/claude/build/part5.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="s6"><span class="num">7</span>The Simple Pendulum — and Every Exam Variation</h2>

<figure>
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" font-family="Georgia,serif">
  <rect width="700" height="300" fill="#fff"/>
  <!-- pivot -->
  <line x1="150" y1="34" x2="330" y2="34" stroke="#1C2128" stroke-width="3"/>
  <g stroke="#888" stroke-width="1.3">
    <line x1="165" y1="34" x2="155" y2="22"/><line x1="195" y1="34" x2="185" y2="22"/>
    <line x1="225" y1="34" x2="215" y2="22"/><line x1="255" y1="34" x2="245" y2="22"/>
    <line x1="285" y1="34" x2="275" y2="22"/><line x1="315" y1="34" x2="305" y2="22"/>
  </g>
  <circle cx="240" cy="34" r="4" fill="#1C2128"/>
  <!-- vertical dashed -->
  <line x1="240" y1="34" x2="240" y2="270" stroke="#999" stroke-width="1.2" stroke-dasharray="6 5"/>
  <!-- string at angle -->
  <line x1="240" y1="34" x2="356" y2="228" stroke="#2E4172" stroke-width="2.4"/>
  <circle cx="360" cy="236" r="15" fill="#E7EBF4" stroke="#2E4172" stroke-width="2.2"/>
  <text x="353" y="241" font-size="13" fill="#2E4172">m</text>
  <!-- angle arc -->
  <path d="M 240 110 A 76 76 0 0 1 279 99" stroke="#A23B3B" stroke-width="1.8" fill="none"/>
  <text x="252" y="96" font-size="16" fill="#A23B3B" font-style="italic">&#952;</text>
  <text x="268" y="140" font-size="15" fill="#2E4172" font-style="italic">l</text>
  <!-- forces -->
  <line x1="360" y1="236" x2="360" y2="292" stroke="#1C2128" stroke-width="2" marker-end="url(#arr3)"/>
  <text x="368" y="288" font-size="14" fill="#1C2128">mg</text>
  <line x1="360" y1="236" x2="312" y2="264" stroke="#A23B3B" stroke-width="2" marker-end="url(#arr3)"/>
  <text x="238" y="278" font-size="13.5" fill="#A23B3B">mg sin&#952; (restoring, tangential)</text>
  <line x1="360" y1="236" x2="296" y2="130" stroke="#2F6F6A" stroke-width="2" marker-end="url(#arr3)"/>
  <text x="255" y="122" font-size="13.5" fill="#2F6F6A">T (tension)</text>
  <defs><marker id="arr3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L7,3 L0,6 z" fill="context-stroke"/></marker></defs>
  <!-- arc of swing -->
  <path d="M 130 220 A 226 226 0 0 1 356 260" stroke="#B7791F" stroke-width="1.4" fill="none" stroke-dasharray="3 5"/>
  <!-- equations panel -->
  <text x="470" y="80" font-size="15" fill="#1C2128">Tangential Newton&#8217;s law:</text>
  <text x="470" y="106" font-size="15.5" fill="#2E4172" font-style="italic">ml&#952;&#776; = &#8722;mg sin&#952;</text>
  <text x="470" y="146" font-size="15" fill="#1C2128">Small angle (sin&#952; &#8776; &#952;):</text>
  <text x="470" y="172" font-size="15.5" fill="#2E4172" font-style="italic">&#952;&#776; + (g/l)&#952; = 0</text>
  <text x="470" y="212" font-size="15" fill="#A23B3B">T = 2&#960;&#8730;(l/g)</text>
  <text x="470" y="238" font-size="13.5" fill="#5B6068">independent of mass and</text>
  <text x="470" y="256" font-size="13.5" fill="#5B6068">(for small &#952;) of amplitude</text>
</svg>
<figcaption>Fig. 7 — Simple pendulum: only the tangential component \(mg\sin\theta\) restores; the tension does no work.</figcaption>
</figure>

<p>Resolving along the arc \(s=l\theta\): \(\;ml\ddot\theta=-mg\sin\theta\), i.e.</p>
<div class="keyeq">\[ \ddot\theta+\frac{g}{l}\sin\theta=0 \;\;\xrightarrow{\ \theta\ \text{small}\ }\;\; \ddot\theta+\frac{g}{l}\theta=0,\qquad \boxed{T=2\pi\sqrt{\frac{l}{g}}} \]</div>

<h3>7.1 The variations CSIR actually asks</h3>
<table>
<tr><th>Variation</th><th>Result</th><th>Why</th></tr>
<tr><td>Lift accelerating <b>up</b> with \(a\)</td><td>\(T=2\pi\sqrt{\dfrac{l}{g+a}}\) (shorter)</td><td>pseudo-force adds to gravity: \(g_{\rm eff}=g+a\)</td></tr>
<tr><td>Lift accelerating <b>down</b> with \(a\)</td><td>\(T=2\pi\sqrt{\dfrac{l}{g-a}}\) (longer)</td><td>\(g_{\rm eff}=g-a\)</td></tr>
<tr><td>Freely falling lift / orbiting satellite</td><td>\(T\to\infty\) — no oscillation</td><td>\(g_{\rm eff}=0\); the pendulum floats</td></tr>
<tr><td>Cart accelerating horizontally with \(a\)</td><td>\(T=2\pi\sqrt{\dfrac{l}{\sqrt{g^2+a^2}}}\); equilibrium tilts by \(\tan\theta_0=a/g\)</td><td>effective gravity is the vector sum</td></tr>
<tr><td>Charged bob \(+q\) in downward field \(E\)</td><td>\(g_{\rm eff}=g+\dfrac{qE}{m}\)</td><td>constant extra "gravity"</td></tr>
<tr><td>Bob fully immersed in liquid, density ratio \(\sigma/\rho\)</td><td>\(g_{\rm eff}=g\bigl(1-\tfrac{\sigma_{\rm liq}}{\rho_{\rm bob}}\bigr)\)</td><td>buoyancy reduces effective weight</td></tr>
<tr><td>Length comparable to Earth's radius \(R\)</td><td>\(T=2\pi\Bigl[g\bigl(\tfrac1l+\tfrac1R\bigr)\Bigr]^{-1/2}\); as \(l\to\infty\), \(T\to2\pi\sqrt{R/g}\approx84.6\) min</td><td>gravity is no longer parallel over the swing</td></tr>
<tr><td>Large amplitude \(\theta_0\)</td><td>\(T\simeq T_0\Bigl(1+\dfrac{\theta_0^2}{16}+\cdots\Bigr)\)</td><td>\(\sin\theta<\theta\): restoring force weaker ⇒ slower</td></tr>
<tr><td>Seconds pendulum (\(T=2\) s)</td><td>\(l=\dfrac{gT^2}{4\pi^2}\approx0.993\) m \(\approx1\) m</td><td>standard number worth memorising</td></tr>
</table>

<div class="box trick"><span class="lbl">Trick — percentage/error questions</span>
\(T\propto\sqrt{l}\) ⇒ \(\dfrac{\Delta T}{T}=\dfrac12\dfrac{\Delta l}{l}-\dfrac12\dfrac{\Delta g}{g}\). "Length increases by 2%" ⇒ period increases by 1%; a pendulum clock then <b>loses</b> time — about \(\tfrac12(0.02)(86400)=864\) s per day per unit fraction. Clock <em>runs slow</em> if \(T\) increases (hot day, longer rod), <em>fast</em> if \(T\) decreases.</div>

<div class="box trap"><span class="lbl">Traps</span>
<ul style="margin:.2em 0">
<li>\(\ddot\theta+\frac{g}{l}\sin\theta=0\) is <b>nonlinear</b>; the pendulum is SHM only in the small-angle limit. "The pendulum is exactly simple harmonic" = wrong option.</li>
<li>Large amplitude makes the period <b>longer</b>, never shorter.</li>
<li>Period is independent of the <b>mass</b> — options inserting \(m\) are automatically wrong (contrast with the spring, where \(m\) matters but \(g\) doesn't: the two systems are complementary traps).</li>
<li>On the Moon (\(g/6\)): pendulum period grows by \(\sqrt6\); a spring-mass period is <b>unchanged</b>. A favourite paired question.</li>
</ul></div>

<!-- ============================================================ -->
<h2 id="s7"><span class="num">8</span>Oscillations of a Spring — the Four Regimes</h2>

<h3><span class="tag">Regime 1</span>Free oscillations</h3>
<p>\(m\ddot x+kx=0\Rightarrow\omega_0=\sqrt{k/m},\ T=2\pi\sqrt{m/k}\). Useful hardware facts:</p>
<ul>
<li><b>Series springs:</b> \(\dfrac1{k_s}=\dfrac1{k_1}+\dfrac1{k_2}\) (softer). <b>Parallel:</b> \(k_p=k_1+k_2\) (stiffer). A mass <em>between</em> two springs attached to walls oscillates with \(k_1+k_2\) (they act in parallel even though they look "in series").</li>
<li><b>Cutting a spring</b> into \(n\) equal parts multiplies \(k\) by \(n\) (half spring ⇒ \(k\to2k\) ⇒ \(T\to T/\sqrt2\)).</li>
<li>Spring of mass \(m_s\): effective inertia \(m+\dfrac{m_s}{3}\) (correction worth one conceptual mark).</li>
</ul>

<h3><span class="tag">Regime 2</span>Damped free oscillations</h3>
<p>Resistive force \(-c\dot x\):</p>
<div class="keyeq">\[ m\ddot x+c\dot x+kx=0 \;\Longrightarrow\; \ddot x+2\beta\dot x+\omega_0^2x=0,\qquad \beta=\frac{c}{2m},\ \ \omega_0=\sqrt{\frac{k}{m}} \]</div>
<p>The three cases of Section 1 apply verbatim. For the <b>underdamped</b> case (\(\beta<\omega_0\)):</p>
\[ x=a\,e^{-\beta t}\cos(\omega_d t+\varphi),\qquad \omega_d=\sqrt{\omega_0^2-\beta^2}<\omega_0 \]

<figure><img src="{{FIG:fig_damping}}" alt="damping three cases"/>
<figcaption>Fig. 8 — The three damping regimes. Note the critically damped curve returns fastest; the overdamped one crawls.</figcaption></figure>

<table>
<tr><th>Concept</th><th>Formula</th><th>Comment</th></tr>
<tr><td>Damped period</td><td>\(T_d=\dfrac{2\pi}{\sqrt{\omega_0^2-\beta^2}}\)</td><td>always <b>longer</b> than the undamped period</td></tr>
<tr><td>Amplitude decay</td><td>\(a(t)=a_0e^{-\beta t}\)</td><td>falls to \(1/e\) in relaxation time \(\tau_a=1/\beta\)</td></tr>
<tr><td>Energy decay</td><td>\(E(t)=E_0e^{-2\beta t}\)</td><td><b>twice as fast</b> as amplitude (since \(E\propto a^2\)); \(\tau_E=1/2\beta\)</td></tr>
<tr><td>Logarithmic decrement</td><td>\(\delta=\ln\dfrac{a_n}{a_{n+1}}=\beta T_d\)</td><td>successive same-side amplitudes form a GP with ratio \(e^{-\delta}\)</td></tr>
<tr><td>Quality factor</td><td>\(Q=\dfrac{\omega_0}{2\beta}\ \bigl(=\dfrac{\sqrt{km}}{c}=\omega_0\tau_E\bigr)\)</td><td>big \(Q\) = light damping</td></tr>
<tr><td>Energy lost per cycle</td><td>\(\dfrac{\Delta E}{E}\simeq\dfrac{2\pi}{Q}\)</td><td>defining property of \(Q\)</td></tr>
<tr><td>Oscillations before amplitude \(\to1/e\)</td><td>\(n\simeq\dfrac{Q}{\pi}\)</td><td>so \(Q=n\pi\) if told "\(n\) oscillations to decay to \(1/e\)"</td></tr>
</table>

<div class="box trick"><span class="lbl">Tricks</span>
<ul style="margin:.2em 0">
<li>Critical damping gives the <b>fastest return without overshoot</b> — the design point of galvanometers ("dead-beat"), vehicle shock absorbers, door closers. "Which damping brings the system to rest quickest?" → critical, always.</li>
<li>Weak damping expansion: \(\omega_d\approx\omega_0\Bigl(1-\dfrac{\beta^2}{2\omega_0^2}\Bigr)=\omega_0\Bigl(1-\dfrac{1}{8Q^2}\Bigr)\) — the fractional frequency shift is second order, which is why high-\(Q\) clocks barely notice damping.</li>
<li>Amplitude after \(n\) full swings: \(a_n=a_0e^{-n\delta}\). If the amplitude halves every swing, \(\delta=\ln2\), and after 3 swings it is \(a_0/8\) — geometric, not linear, decay.</li>
</ul></div>

<h3><span class="tag">Regime 3</span>Forced oscillations, no damping</h3>
<p>\(m\ddot x+kx=F_0\cos\omega t\). Particular integral (replace \(D^2\to-\omega^2\)):</p>
<div class="keyeq">\[ x_p=\frac{F_0/m}{\omega_0^2-\omega^2}\cos\omega t \qquad(\omega\neq\omega_0) \]</div>
<ul>
<li>\(\omega<\omega_0\): response <b>in phase</b> with the force; \(\omega>\omega_0\): exactly <b>out of phase</b> (\(\pi\)). The phase flips discontinuously through resonance when there is no damping.</li>
<li>With initial conditions \(x(0)=\dot x(0)=0\) and \(\omega\approx\omega_0\), the free + forced parts superpose into <b>beats</b>: \[ x=\frac{2F_0/m}{\omega_0^2-\omega^2}\,\sin\Bigl(\frac{(\omega_0-\omega)t}{2}\Bigr)\sin\Bigl(\frac{(\omega_0+\omega)t}{2}\Bigr) \] — a fast oscillation inside a slow envelope of beat frequency \(|\omega_0-\omega|/2\pi\).</li>
<li><b>Exact resonance</b> \(\omega=\omega_0\): the naive PI blows up; the correct one carries the tell-tale factor of \(t\): \[ \boxed{\,x=\frac{F_0}{2m\omega_0}\,t\sin\omega_0 t\,} \] — amplitude grows <b>linearly and without bound</b>. (Same "repeated root ⇒ multiply by \(t\)" rule as critical damping.)</li>
</ul>

<figure><img src="{{FIG:fig_beats}}" alt="beats and secular growth"/>
<figcaption>Fig. 9 — Undamped forcing. Left: near resonance, beats. Right: at resonance, the amplitude ramps linearly in \(t\) — the classic "bridge collapse" picture.</figcaption></figure>

<h3><span class="tag">Regime 4</span>Forced oscillations with damping — the full story</h3>
<div class="keyeq">\[ \ddot x+2\beta\dot x+\omega_0^2x=\frac{F_0}{m}\cos\omega t \]</div>
<p><b>Solution = transient + steady state.</b> The complementary function decays as \(e^{-\beta t}\) (the transient, gone after a few \(1/\beta\)); what survives is the particular integral:</p>
<div class="keyeq">\[ x_{ss}=A(\omega)\cos(\omega t-\phi),\qquad A(\omega)=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}},\qquad \tan\phi=\frac{2\beta\omega}{\omega_0^2-\omega^2} \]</div>
<p>The steady state oscillates at the <b>driver's frequency</b> \(\omega\) (not \(\omega_0\), not \(\omega_d\)), with a constant amplitude and a phase lag \(\phi\in(0,\pi)\).</p>

<figure><img src="{{FIG:fig_resonance}}" alt="resonance amplitude and phase"/>
<figcaption>Fig. 10 — Steady-state amplitude and phase. Lighter damping → taller, sharper peak, sitting slightly <em>below</em> \(\omega_0\). The phase lag is \(\pi/2\) exactly at \(\omega_0\) for any damping.</figcaption></figure>

<table>
<tr><th>Fact</th><th>Statement</th></tr>
<tr><td><b>Amplitude resonance</b></td><td>\(A(\omega)\) peaks at \(\;\boxed{\omega_r=\sqrt{\omega_0^2-2\beta^2}}\;<\omega_d<\omega_0\), and only exists if \(\beta<\omega_0/\sqrt2\) (otherwise \(A\) decreases monotonically — no peak).</td></tr>
<tr><td><b>Peak height</b></td><td>\(A_{max}=\dfrac{F_0}{2m\beta\sqrt{\omega_0^2-\beta^2}}\;\xrightarrow{\text{light damping}}\;\dfrac{F_0}{2m\beta\omega_0}=Q\cdot\dfrac{F_0}{k}\) — i.e. <b>\(Q\) times the static deflection</b>. Finite because of damping.</td></tr>
<tr><td><b>Velocity resonance</b></td><td>velocity amplitude \(\omega A(\omega)\) peaks <b>exactly at \(\omega=\omega_0\)</b>, for any damping. So does the average <b>power absorbed</b>. (Electrical twin: current resonance.)</td></tr>
<tr><td><b>Phase</b></td><td>\(\phi\to0\) for \(\omega\ll\omega_0\) (in phase), \(\phi=\pi/2\) exactly at \(\omega_0\), \(\phi\to\pi\) for \(\omega\gg\omega_0\). Damping smooths the jump into an S-curve.</td></tr>
<tr><td><b>Bandwidth</b></td><td>power falls to half its peak at \(\omega_0\pm\beta\): full width \(\Delta\omega=2\beta=\omega_0/Q\).</td></tr>
<tr><td><b>Frequency-domain limits</b></td><td>\(\omega\to0\): \(A\to F_0/k\) — <em>stiffness-controlled</em>. \(\omega\to\infty\): \(A\to F_0/m\omega^2\to0\) — <em>mass-controlled</em>, lag \(\to\pi\). Near \(\omega_0\): <em>damping-controlled</em>.</td></tr>
</table>

<div class="box trap"><span class="lbl">The single most examined trap in this whole chapter</span>
<b>Three different frequencies, know which is which:</b>
\[ \underbrace{\omega_r=\sqrt{\omega_0^2-2\beta^2}}_{\text{amplitude resonance}}\;<\;\underbrace{\omega_d=\sqrt{\omega_0^2-\beta^2}}_{\text{free damped oscillation}}\;<\;\underbrace{\omega_0=\sqrt{k/m}}_{\text{natural; velocity/power resonance}} \]
A question that says "maximum displacement amplitude" wants \(\omega_r\); "maximum velocity amplitude / maximum power absorbed / current resonance" wants \(\omega_0\); "frequency of free damped vibration" wants \(\omega_d\). Options are built to punish mixing these.</div>

<div class="box trick"><span class="lbl">Tricks</span>
<ul style="margin:.2em 0">
<li>Steady state has <b>no memory of initial conditions</b> — initial conditions live only in the transient. If asked "amplitude after a long time", ignore \(x(0),\dot x(0)\) entirely.</li>
<li>At \(\omega=\omega_0\) the driving force is in phase with the <b>velocity</b> (lag \(\pi/2\) behind on displacement) — that is exactly why power transfer is maximal there.</li>
<li>Complex-exponential shortcut: put \(x=\mathrm{Re}\,\tilde A e^{i\omega t}\), get \(\tilde A=\dfrac{F_0/m}{\omega_0^2-\omega^2+2i\beta\omega}\); modulus is the amplitude, argument is (minus) the phase. Fastest route in the exam.</li>
<li>Sharpness of resonance \(\propto Q\): halving \(R\) (or \(c\)) doubles the peak and halves the bandwidth — the area under the power curve stays comparable.</li>
</ul></div>
HTMLEOF
echo "part5 ok"
```

**Command** - Write solved problems, formula sheet, trap list and close document

```bash
cat > /home/claude/build/part6.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="s8"><span class="num">9</span>Solved Problems — CSIR Style</h2>

<div class="ex"><div class="q"><span class="qn">Problem 1 · R–L transient</span>
A coil of \(L=2\) H and \(R=10\ \Omega\) is suddenly connected to a \(100\) V battery. Find \(i(t)\) and the time for the current to reach half its final value.</div>
<div class="s"><span class="sn">Solution</span>
\(\tau=L/R=0.2\) s, \(i_{max}=E/R=10\) A, so \(i(t)=10\bigl(1-e^{-5t}\bigr)\) A. Half value: \(1-e^{-t/\tau}=\tfrac12\Rightarrow t=\tau\ln2=0.2\times0.693\). <span class="ans">t ≈ 0.139 s</span></div></div>

<div class="ex"><div class="q"><span class="qn">Problem 2 · R–C energy decay</span>
A charged capacitor discharges through a resistor. After what time is the stored <em>energy</em> half of its initial value?</div>
<div class="s"><span class="sn">Solution</span>
\(q=q_0e^{-t/RC}\Rightarrow U=\dfrac{q^2}{2C}=U_0e^{-2t/RC}\). Energy decays with time constant \(RC/2\), twice as fast as charge. Setting \(e^{-2t/RC}=\tfrac12\): <span class="ans">t = (RC/2) ln 2</span> &nbsp;— <em>not</em> \(RC\ln2\), the option built for the careless.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 3 · Critical resistance</span>
In a series LCR circuit \(L=1\) H, \(C=1\ \mu\)F. For what \(R\) is the discharge of the capacitor just non-oscillatory?</div>
<div class="s"><span class="sn">Solution</span>
Critical damping: \(R_c=2\sqrt{L/C}=2\sqrt{1/10^{-6}}\). <span class="ans">R = 2000 Ω</span>. For \(R<2\) kΩ the discharge rings at \(\omega_d=\sqrt{\frac{1}{LC}-\frac{R^2}{4L^2}}\); for \(R>2\) kΩ it is dead-beat.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 4 · Resonance and voltage magnification</span>
Series circuit: \(L=10\) mH, \(C=1\ \mu\)F, \(R=10\ \Omega\), source amplitude \(E_0=5\) V. Find the resonant angular frequency, \(Q\), and the peak voltage across the capacitor at resonance.</div>
<div class="s"><span class="sn">Solution</span>
\(\omega_0=1/\sqrt{LC}=1/\sqrt{10^{-2}\times10^{-6}}=10^4\) rad/s. \(Q=\dfrac{\omega_0L}{R}=\dfrac{10^4\times10^{-2}}{10}=10\). At resonance current \(i_0=E_0/R\), so \(V_C=\dfrac{i_0}{\omega_0C}=Q\,E_0=10\times5\). <span class="ans">ω₀ = 10⁴ rad/s, Q = 10, V_C = 50 V</span> — ten times the source: voltage magnification.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 5 · Which resonance? (the classic discriminator)</span>
In the circuit of Problem 4, at what frequency is the voltage across the <em>capacitor</em> maximum?</div>
<div class="s"><span class="sn">Solution</span>
\(V_C\propto q\), and charge amplitude peaks at \(\omega_q=\sqrt{\dfrac{1}{LC}-\dfrac{R^2}{2L^2}}=\sqrt{10^8-\dfrac{100}{2\times10^{-4}}}=\sqrt{10^8-5\times10^5}\approx9.975\times10^3\) rad/s. <span class="ans">ω_q = √(1/LC − R²/2L²) &lt; ω₀</span> — slightly below current resonance; the "obvious" answer \(10^4\) is the trap (that is where the <em>current</em>, hence \(V_R\), peaks).</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 6 · Actual CSIR-NET (June 2011, from your question bank)</span>
\(\dfrac{d^2x}{dt^2}-3\dfrac{dx}{dt}+2x=0\) with \(x=0\) at \(t=0\) and \(x=1\) at \(t=1\). The value of \(x\) at \(t=2\) is: &nbsp;(a) \(e^2+1\) &nbsp;(b) \(e^2+e\) &nbsp;(c) \(e+2\) &nbsp;(d) \(2e\)</div>
<div class="s"><span class="sn">Solution</span>
Auxiliary: \(m^2-3m+2=(m-1)(m-2)=0\Rightarrow x=c_1e^{t}+c_2e^{2t}\). \(x(0)=0\Rightarrow c_2=-c_1\). \(x(1)=1\Rightarrow c_1(e-e^2)=1\). Then \(x(2)=c_1(e^2-e^4)=\dfrac{e^2(1-e^2)}{e(1-e)}=e(1+e)\). <span class="ans">(b) e² + e</span>. Note the method is <em>identical</em> to a damped oscillator — only the sign of the middle term (growth instead of decay) differs.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 7 · Circuit by Laplace transform (CSIR's favourite method)</span>
Solve \(L\dfrac{di}{dt}+Ri=E\), \(i(0)=0\), using Laplace transforms.</div>
<div class="s"><span class="sn">Solution</span>
Transform: \(L\,[sI(s)-i(0)]+RI(s)=\dfrac{E}{s}\Rightarrow I(s)=\dfrac{E}{L}\cdot\dfrac{1}{s\,(s+R/L)}\). Partial fractions: \(\dfrac{1}{s(s+a)}=\dfrac1a\Bigl(\dfrac1s-\dfrac1{s+a}\Bigr)\) with \(a=R/L\). Invert: <span class="ans">i(t) = (E/R)(1 − e^{−Rt/L})</span>. The Laplace route handles initial conditions automatically — use it whenever the problem states them.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 8 · Fall with linear drag</span>
A particle falls from rest with resistance \(mkv\) (per unit mass \(kv\)). Show \(v=\dfrac{g}{k}(1-e^{-kt})\) and find \(v\) at \(t=\dfrac{\ln2}{k}\).</div>
<div class="s"><span class="sn">Solution</span>
\(\dfrac{dv}{dt}=g-kv\Rightarrow\dfrac{dv}{g-kv}=dt\Rightarrow-\dfrac1k\ln(g-kv)=t+C\). With \(v(0)=0\): \(v=\dfrac{g}{k}(1-e^{-kt})\), terminal \(v_T=g/k\). At \(t=\ln2/k\): \(v=v_T(1-\tfrac12)\). <span class="ans">v = v_T/2 = g/2k</span></div></div>

<div class="ex"><div class="q"><span class="qn">Problem 9 · SHM timing</span>
A particle in SHM of period \(T\) starts from the positive extreme. How long does it take to first reach \(x=a/2\)?</div>
<div class="s"><span class="sn">Solution</span>
\(x=a\cos\omega t\); \(a/2=a\cos\omega t\Rightarrow\omega t=\pi/3\Rightarrow t=\dfrac{\pi/3}{2\pi/T}\). <span class="ans">t = T/6</span>. (From the <em>centre</em> to \(a/2\) it is only \(T/12\) — the particle is fast near the centre, slow near the extremes.)</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 10 · Static-extension shortcut</span>
A load hung on a light spring stretches it by \(1\) cm. Find the period of vertical oscillation. \((g=\pi^2\ \text{m/s}^2\approx9.87)\)</div>
<div class="s"><span class="sn">Solution</span>
\(T=2\pi\sqrt{e/g}=2\pi\sqrt{0.01/\pi^2}=2\pi\cdot\dfrac{0.1}{\pi}\). <span class="ans">T = 0.2 s</span>. Neither \(m\) nor \(k\) was given — nor needed.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 11 · Elastic string, amplitude &gt; e</span>
A mass hangs on an elastic string with equilibrium extension \(e\). It is pulled down a further \(2e\) and released. Find its speed when the string first becomes slack, and how much higher it rises.</div>
<div class="s"><span class="sn">Solution</span>
SHM about equilibrium with \(\omega^2=g/e\), amplitude \(a=2e\). The string goes slack at the natural-length point, i.e. \(x=e\) <em>above</em> equilibrium. Speed there: \(v^2=\omega^2(a^2-x^2)=\dfrac{g}{e}(4e^2-e^2)=3ge\Rightarrow v=\sqrt{3ge}\). Above that point: free flight, extra rise \(h=\dfrac{v^2}{2g}=\dfrac{3e}{2}\). <span class="ans">v = √(3ge); rises a further 3e/2</span>. The motion is periodic but <b>not</b> SHM overall.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 12 · Pendulum in a lift</span>
A pendulum has period \(2\) s in a stationary lift. The lift accelerates upward at \(g/3\). New period?</div>
<div class="s"><span class="sn">Solution</span>
\(T\propto1/\sqrt{g_{\rm eff}}\), \(g_{\rm eff}=g+g/3=\dfrac{4g}{3}\). \(T'=2\sqrt{\dfrac{g}{4g/3}}=2\sqrt{3}/2\). <span class="ans">T′ = √3 ≈ 1.73 s</span> (shorter — stronger effective gravity).</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 13 · Read a damped equation at sight</span>
For \(\ddot x+2\dot x+5x=0\): find the frequency of oscillation, the quality factor, and the ratio of successive same-side amplitudes.</div>
<div class="s"><span class="sn">Solution</span>
Compare: \(2\beta=2\Rightarrow\beta=1\); \(\omega_0^2=5\). Underdamped since \(\beta<\omega_0\). \(\omega_d=\sqrt{5-1}=2\) rad/s, \(T_d=\pi\) s. \(Q=\dfrac{\omega_0}{2\beta}=\dfrac{\sqrt5}{2}\). Log decrement \(\delta=\beta T_d=\pi\), so amplitude ratio \(=e^{\delta}\). <span class="ans">ω_d = 2, Q = √5/2, aₙ/aₙ₊₁ = e^π</span></div></div>

<div class="ex"><div class="q"><span class="qn">Problem 14 · Forced with damping — the three frequencies</span>
\(\ddot x+4\dot x+25x=10\cos\omega t\). Find (i) the driving frequency for maximum displacement amplitude, (ii) for maximum velocity amplitude, (iii) the maximum displacement amplitude itself.</div>
<div class="s"><span class="sn">Solution</span>
\(\beta=2,\ \omega_0=5,\ F_0/m=10\). (i) Amplitude resonance \(\omega_r=\sqrt{\omega_0^2-2\beta^2}=\sqrt{25-8}=\sqrt{17}\). (ii) Velocity resonance at \(\omega_0=5\). (iii) \(A_{max}=\dfrac{F_0/m}{2\beta\sqrt{\omega_0^2-\beta^2}}=\dfrac{10}{4\sqrt{21}}\). <span class="ans">ω_r = √17, ω_v = 5, A_max = 5/(2√21) ≈ 0.546</span></div></div>

<div class="ex"><div class="q"><span class="qn">Problem 15 · Q from an observed decay</span>
The amplitude of a lightly damped oscillator drops to \(1/e\) of its initial value in \(10\) complete oscillations. Estimate \(Q\).</div>
<div class="s"><span class="sn">Solution</span>
Amplitude \(\propto e^{-\beta t}\): \(\beta\,(10\,T_d)=1\). With \(T_d\approx2\pi/\omega_0\): \(\beta=\dfrac{\omega_0}{20\pi}\), so \(Q=\dfrac{\omega_0}{2\beta}=10\pi\). <span class="ans">Q ≈ 31.4</span> — general rule: \(Q=n\pi\) for decay to \(1/e\) in \(n\) oscillations.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 16 · Undamped resonance growth</span>
\(\ddot x+9x=6\cos3t\), \(x(0)=\dot x(0)=0\). Find \(x(t)\).</div>
<div class="s"><span class="sn">Solution</span>
Driving at the natural frequency \(\omega_0=3\): resonance. \(x_p=\dfrac{1}{D^2+9}\,6\cos3t=\dfrac{6t}{2\cdot3}\sin3t=t\sin3t\) (the "multiply by \(t\), differentiate the denominator" rule). The CF adjusts to the initial conditions and here vanishes. <span class="ans">x = t sin 3t</span> — amplitude grows linearly forever (no damping to stop it).</div></div>

<!-- ============================================================ -->
<h2 id="s9"><span class="num">10</span>One-Page Formula Sheet &amp; Final Trap List</h2>

<div class="two">
<div>
<h3>Circuits</h3>
<ul class="small">
<li>R–L: \(i=\frac{E}{R}(1-e^{-t/\tau}),\ \tau=L/R\); decay \(i_0e^{-t/\tau}\)</li>
<li>R–C: \(q=CE(1-e^{-t/\tau}),\ \tau=RC\); \(i=\frac{E}{R}e^{-t/\tau}\)</li>
<li>L–C: \(\omega_0=1/\sqrt{LC}\); energy \(\frac{q^2}{2C}+\frac{Li^2}{2}=\)const</li>
<li>LCR free: \(\beta=\frac{R}{2L}\); critical \(R_c=2\sqrt{L/C}\); \(\omega_d=\sqrt{\frac{1}{LC}-\frac{R^2}{4L^2}}\)</li>
<li>Forced: \(Z=\sqrt{R^2+(\omega L-\frac{1}{\omega C})^2}\), \(\tan\phi=\frac{\omega L-1/\omega C}{R}\)</li>
<li>Resonance \(\omega_0=1/\sqrt{LC}\): \(Z_{min}=R\), \(V_L=V_C=QE_0\)</li>
<li>\(Q=\frac{\omega_0L}{R}=\frac1{\omega_0CR}=\frac1R\sqrt{\frac LC}=\frac{\omega_0}{\Delta\omega}\)</li>
<li>Capacitor-voltage peak: \(\omega_q=\sqrt{\frac{1}{LC}-\frac{R^2}{2L^2}}<\omega_0\)</li>
</ul>
<h3>Motion with resistance</h3>
<ul class="small">
<li>\(\propto v\): \(v_T=\frac{mg}{k}\), \(v=v_T(1-e^{-kt/m})\)</li>
<li>\(\propto v^2\): \(v_T=\sqrt{\frac{mg}{k}}\), \(v=v_T\tanh\frac{gt}{v_T}\), \(v^2=v_T^2(1-e^{-2gx/v_T^2})\)</li>
<li>Force of \(x\) or "after distance…": use \(v\frac{dv}{dx}\)</li>
</ul>
</div>
<div>
<h3>Oscillations</h3>
<ul class="small">
<li>SHM: \(v^2=\omega^2(a^2-x^2)\); \(v_{max}=a\omega\), \(a_{max}=a\omega^2\)</li>
<li>Vertical spring/string: \(mg=ke\); \(T=2\pi\sqrt{e/g}=2\pi\sqrt{m/k}\)</li>
<li>String slack above natural length ⇒ SHM + free-flight patchwork</li>
<li>Horizontal string: \(T=2\pi\sqrt{\frac{ml}{\lambda}}+\frac{4l}{a\omega}\) (not SHM)</li>
<li>Pendulum: \(T=2\pi\sqrt{l/g_{\rm eff}}\); lift ±a; horizontal: \(\sqrt{g^2+a^2}\); \(l\to\infty\): 84.6 min</li>
<li>Damped: \(\beta=\frac{c}{2m}\), \(\omega_d=\sqrt{\omega_0^2-\beta^2}\), \(\delta=\beta T_d\), \(E\propto e^{-2\beta t}\)</li>
<li>\(Q=\frac{\omega_0}{2\beta}\); \(\frac{\Delta E}{E}\big|_{\rm cycle}=\frac{2\pi}{Q}\); \(n_{1/e}\approx\frac{Q}{\pi}\)</li>
<li>Forced: \(A=\frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2+4\beta^2\omega^2}}\), \(\tan\phi=\frac{2\beta\omega}{\omega_0^2-\omega^2}\)</li>
<li>\(\omega_r=\sqrt{\omega_0^2-2\beta^2}\) (needs \(\beta<\omega_0/\sqrt2\)); \(A_{max}\approx Q\frac{F_0}{k}\)</li>
<li>Bandwidth \(2\beta=\omega_0/Q\); resonance (undamped): \(x=\frac{F_0}{2m\omega_0}t\sin\omega_0t\)</li>
</ul>
</div>
</div>

<div class="box exam"><span class="lbl">Final ten traps — scan before the exam</span>
<ol style="margin:.3em 0">
<li>Capacitor at \(t=0\): short; at \(\infty\): open. Inductor: exactly the opposite.</li>
<li>Energy decays <b>twice</b> as fast as charge/amplitude (\(e^{-2t/\tau}\) vs \(e^{-t/\tau}\)).</li>
<li>Terminal velocity is an asymptote — never reached in finite time.</li>
<li>With drag: \(t_{\rm up}<t_{\rm down}\); return speed &lt; launch speed.</li>
<li>KE = PE at \(x=a/\sqrt2\), not \(a/2\); extreme→\(a/2\) takes \(T/6\), centre→\(a/2\) takes \(T/12\).</li>
<li>Gravity never enters a spring's period; mass never enters a pendulum's. (Moon: pendulum slows ×√6, spring unchanged.)</li>
<li>A slack string exerts <b>zero</b> force — composite motion is periodic, not SHM, and its period depends on amplitude.</li>
<li>Damping <b>lengthens</b> the free period (\(\omega_d<\omega_0\)); critical damping is the <b>fastest</b> return.</li>
<li>Three frequencies: \(\omega_r<\omega_d<\omega_0\). Displacement peak at \(\omega_r\); velocity/power/current peak exactly at \(\omega_0\); phase lag is \(\pi/2\) at \(\omega_0\) regardless of damping.</li>
<li>Steady-state response oscillates at the <b>driver's</b> frequency and forgets initial conditions; at resonance \(A_{max}=Q\times\) static deflection, and \(V_C=QE_0\) in the circuit twin.</li>
</ol></div>

<p class="small" style="margin-top:34px;border-top:1px solid var(--rule);padding-top:12px;">
Prepared for CSIR-NET / GATE / JEST preparation · Every system here is the master equation \( \ddot{x}+2\beta\dot{x}+\omega_0^2x=f(t) \) in disguise — learn the dictionary once, answer in four subjects.
</p>

</div></body></html>
HTMLEOF
echo "part6 ok"
```

**Command** - Assemble parts, embed figures as base64, write final HTML to outputs

```bash
cd /home/claude && python3 - << 'PY'
import base64, re, pathlib

parts = ''.join(pathlib.Path(f'build/part{i}.html').read_text() for i in range(1,7))

def embed(m):
    name = m.group(1)
    data = base64.b64encode(pathlib.Path(f'figs/{name}.png').read_bytes()).decode()
    return f'data:image/png;base64,{data}'

out = re.sub(r'\{\{FIG:(\w+)\}\}', embed, parts)
missing = re.findall(r'\{\{FIG:\w+\}\}', out)
print("missing placeholders:", missing)
pathlib.Path('/mnt/user-data/outputs/Differential_Equations_Applications_LCR_and_Mechanics_CSIR.html').write_text(out)
print("bytes:", len(out))
PY
ls -la /mnt/user-data/outputs/
```

**Command** - Fix SVG marker compatibility and sanity-check structure

```bash
cd /mnt/user-data/outputs && sed -i 's/fill="context-stroke"/fill="#1C2128"/' Differential_Equations_Applications_LCR_and_Mechanics_CSIR.html && grep -c "base64" Differential_Equations_Applications_LCR_and_Mechanics_CSIR.html && grep -o "<h2" Differential_Equations_Applications_LCR_and_Mechanics_CSIR.html | wc -l
```

*Presented files: `/mnt/user-data/outputs/Differential_Equations_Applications_LCR_and_Mechanics_CSIR.html`*

Your complete illustrated notes are ready above — open the HTML file and all the math and figures will render.

What's inside, in the order you asked for:

**Circuits (every L, R, C combination):** the three elements with their continuity rules, R–L growth/decay with time constant, R–C charging/discharging, pure L–C oscillation, L–C–R free discharge with the three damping cases and the critical resistance $R_c = 2\sqrt{L/C}$, and the full forced-LCR treatment (impedance, phase, series resonance, voltage magnification $V_C = QE_0$, bandwidth, and the current-vs-charge resonance trap). A drawn LCR circuit and three plotted graphs accompany this.

**Mechanics:** rectilinear motion (including the $v\,dv/dx$ selection trick), vertical motion with resistance $\propto v$ and $\propto v^2$ with terminal-velocity graph, SHM with the reference-circle clock tricks, vertical elastic string (with the $T = 2\pi\sqrt{e/g}$ shortcut and the slack-string composite motion), horizontal elastic string on a smooth table with its full assembled period, the simple pendulum with all nine exam variations (lifts, horizontal acceleration, buoyancy, infinite length → 84.6 min), and springs in all four regimes — free, damped free, forced undamped (beats + $t\sin\omega_0 t$ resonance growth), and forced damped (the three-frequency trap $\omega_r < \omega_d < \omega_0$, peak = $Q\times$ static deflection, bandwidth $= \omega_0/Q$).

**CSIR-specific extras:** the electrical↔mechanical dictionary table, 16 fully worked exam-style problems (including the actual CSIR June 2011 ODE from your question bank, solved to answer $e^2 + e$, and a Laplace-transform circuit solution since CSIR loves that method), plus a one-page formula sheet and a final ten-trap checklist.

If you'd like, I can next turn the trap list and formula sheet into a set of rapid-fire practice MCQs to test yourself against.


---

### [3] **You** - 2026-07-04 03:36:53

now go for calculus of variation.


---

### [4] **Claude** - 2026-07-04 03:43:20

*Searched project knowledge: `calculus of variations Euler Lagrange functional extremum`*

**File created: `/home/claude/make_cov_figs.py`** - Script to generate calculus of variations figures

```py
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
ax.set_title('A functional $I[y]=\\int_{x_1}^{x_2}F(x,y,y\\')\\,dx$ assigns a number to each whole curve')
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
```

**Command** - Generate calculus of variations figures

```bash
cd /home/claude && python make_cov_figs.py && ls -la figs/cov*
```

**Edit to `/home/claude/make_cov_figs.py`** - Fix quote escaping in title string

*replaced:*
```
ax.set_title('A functional $I[y]=\\int_{x_1}^{x_2}F(x,y,y\\')\\,dx$ assigns a number to each whole curve')
```

*with:*
```
ax.set_title("A functional $I[y]=\\int_{x_1}^{x_2}F(x,y,y')\\,dx$ assigns a number to each whole curve")
```

**Command** - Generate calculus of variations figures

```bash
cd /home/claude && python make_cov_figs.py && ls -la figs/cov*
```

All five figures ready. Now assembling the document in the same style:

**Command** - Write CoV document header, functional concept, Euler-Lagrange derivation

```bash
mkdir -p /home/claude/cov && head -c 6200 /home/claude/build/part1.html > /dev/null && cat > /home/claude/cov/p1.html << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calculus of Variations — Complete CSIR-NET Notes</title>
<script>
window.MathJax = { tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']] }, chtml: { scale: 1.0 } };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<style>
  :root{
    --paper:#F7F8F6; --ink:#1C2128; --indigo:#2E4172; --indigo-soft:#E7EBF4;
    --teal:#2F6F6A; --teal-soft:#E4F0EE; --amber:#9C6512; --amber-soft:#FBF1DD;
    --red:#A23B3B; --red-soft:#F7E7E7; --rule:#D8DAD4; --mut:#5B6068;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);
       font-family:Charter,'Bitstream Charter','Sitka Text',Georgia,serif;
       font-size:16.5px;line-height:1.62;}
  .wrap{max-width:920px;margin:0 auto;padding:28px 22px 90px;}
  header.doc{border-bottom:3px double var(--indigo);padding-bottom:18px;margin-bottom:8px;}
  .kicker{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:12px;letter-spacing:.22em;
          text-transform:uppercase;color:var(--indigo);font-weight:700;}
  h1{font-size:clamp(26px,4.4vw,38px);line-height:1.15;margin:.35em 0 .2em;font-weight:700;}
  .sub{color:var(--mut);font-style:italic;margin:0;}
  h2{font-size:24px;margin:2.2em 0 .5em;color:var(--indigo);border-bottom:1.5px solid var(--indigo);
     padding-bottom:6px;font-weight:700;}
  h2 .num{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:13px;letter-spacing:.14em;
     background:var(--indigo);color:#fff;padding:3px 9px;border-radius:3px;vertical-align:3px;margin-right:10px;}
  h3{font-size:19px;margin:1.7em 0 .35em;color:var(--ink);font-weight:700;}
  h3 .tag{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:11px;letter-spacing:.16em;
     text-transform:uppercase;color:var(--teal);display:block;font-weight:700;margin-bottom:2px;}
  p{margin:.55em 0 .9em}
  .box{border:1px solid var(--rule);border-left:5px solid var(--indigo);background:#fff;
       padding:12px 16px;margin:16px 0;border-radius:0 6px 6px 0;}
  .box .lbl{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:11px;font-weight:800;
       letter-spacing:.18em;text-transform:uppercase;color:var(--indigo);display:block;margin-bottom:4px;}
  .trick{border-left-color:var(--teal);background:var(--teal-soft);}
  .trick .lbl{color:var(--teal);}
  .trap{border-left-color:var(--amber);background:var(--amber-soft);}
  .trap .lbl{color:var(--amber);}
  .exam{border-left-color:var(--red);background:var(--red-soft);}
  .exam .lbl{color:var(--red);}
  .keyeq{background:var(--indigo-soft);border:1px solid #C3CDE2;border-radius:6px;
       padding:10px 16px;margin:16px 0;text-align:center;}
  table{border-collapse:collapse;width:100%;margin:16px 0;background:#fff;font-size:15.5px;}
  th{background:var(--indigo);color:#fff;font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;
     font-size:13px;letter-spacing:.05em;padding:8px 10px;text-align:left;}
  td{border:1px solid var(--rule);padding:7px 10px;vertical-align:top;}
  tr:nth-child(even) td{background:#FBFBF9;}
  figure{margin:20px 0;text-align:center;}
  figure img{max-width:100%;border:1px solid var(--rule);border-radius:6px;background:#fff;}
  figure svg{max-width:100%;height:auto;}
  figcaption{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:13px;color:var(--mut);
     margin-top:8px;}
  .ex{background:#fff;border:1px solid var(--rule);border-radius:8px;margin:20px 0;overflow:hidden;}
  .ex .q{padding:12px 16px;border-bottom:1px dashed var(--rule);}
  .ex .q .qn{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-weight:800;color:var(--red);
     font-size:13px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:4px;}
  .ex .s{padding:12px 16px;background:#FAFBF9;}
  .ex .s .sn{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-weight:800;color:var(--teal);
     font-size:13px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:4px;}
  .ans{display:inline-block;background:var(--ink);color:#fff;border-radius:4px;padding:1px 10px;
     font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:13.5px;font-weight:700;}
  ol,ul{margin:.4em 0 1em;padding-left:1.4em}
  li{margin:.3em 0}
  .toc{background:#fff;border:1px solid var(--rule);border-radius:8px;padding:14px 20px;margin:22px 0;}
  .toc b{font-family:'Avenir Next','Segoe UI',system-ui,sans-serif;font-size:12px;letter-spacing:.18em;
     text-transform:uppercase;color:var(--indigo);}
  .toc a{color:var(--ink);text-decoration:none;border-bottom:1px dotted var(--indigo);}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:0 26px;}
  @media(max-width:640px){.two{grid-template-columns:1fr}}
  .small{font-size:14px;color:var(--mut);}
</style>
</head>
<body><div class="wrap">

<header class="doc">
  <span class="kicker">CSIR-NET / GATE / JEST · Mathematical Physics &amp; Classical Mechanics</span>
  <h1>Calculus of Variations</h1>
  <p class="sub">Functionals · Euler–Lagrange equation · the four first-integral shortcuts · brachistochrone, geodesics, minimal surfaces, Fermat · constraints &amp; isoperimetric problems · Rayleigh–Ritz and the quantum variational principle — with every tricky concept, drawn figures and fully worked exam-style problems.</p>
</header>

<div class="toc">
  <b>Contents</b>
  <ol>
    <li><a href="#c1">What is a functional? The idea of a variation</a></li>
    <li><a href="#c2">The Euler–Lagrange equation (with the 5-line derivation)</a></li>
    <li><a href="#c3">The four special cases — 90% of exam problems die here</a></li>
    <li><a href="#c4">The classic problems: shortest path, brachistochrone, soap film, geodesics, Fermat</a></li>
    <li><a href="#c5">Extensions: many variables, higher derivatives, free ends, constraints</a></li>
    <li><a href="#c6">The physics payoff: Hamilton's principle &amp; the variational (Rayleigh–Ritz) method</a></li>
    <li><a href="#c7">Solved problems — CSIR style</a></li>
    <li><a href="#c8">One-page formula sheet &amp; final trap list</a></li>
  </ol>
</div>

<!-- ============================================================ -->
<h2 id="c1"><span class="num">1</span>What Is a Functional? The Idea of a Variation</h2>

<p>Ordinary calculus optimises a <b>function</b>: given \(f(x)\), find the <em>number</em> \(x\) where \(f'(x)=0\). The calculus of variations optimises a <b>functional</b>: given</p>
<div class="keyeq">\[ I[y]=\int_{x_1}^{x_2}F\bigl(x,\,y,\,y'\bigr)\,dx, \qquad y(x_1)=y_1,\quad y(x_2)=y_2 \ \text{fixed}, \]</div>
<p>find the <em>whole curve</em> \(y(x)\) that makes the number \(I\) stationary. The input is a function; the output is a number — that map is a functional. Arc length, travel time, area of a surface, the action \(\int L\,dt\) — all functionals.</p>

<figure><img src="{{FIG:cov_paths}}" alt="family of varied paths"/>
<figcaption>Fig. 1 — Compare the extremal against neighbouring curves \(y+\epsilon\eta(x)\). Every competitor passes through the same fixed endpoints, so \(\eta\) vanishes there.</figcaption></figure>

<p><b>The variation \(\delta y\):</b> deform the curve to \(y(x)+\epsilon\,\eta(x)\) with \(\eta(x_1)=\eta(x_2)=0\). The change \(\delta y=\epsilon\eta(x)\) happens <em>at fixed \(x\)</em> — you move vertically between curves, you never move along a curve. That is the whole difference between \(\delta\) and \(d\):</p>
<table>
<tr><th></th><th>\(d\) (differential)</th><th>\(\delta\) (variation)</th></tr>
<tr><td>What changes</td><td>the point: \(x\to x+dx\) along one fixed curve</td><td>the curve: \(y(x)\to y(x)+\delta y(x)\) at fixed \(x\)</td></tr>
<tr><td>Endpoint value</td><td>generally nonzero</td><td>zero at fixed endpoints</td></tr>
<tr><td>Key algebra</td><td>—</td><td>\(\delta\) commutes with \(\dfrac{d}{dx}\) and with \(\displaystyle\int dx\): \(\ \delta(y')=(\delta y)'\)</td></tr>
</table>

<div class="box"><span class="lbl">Stationary, not necessarily minimum</span>
The condition \(\delta I=0\) finds curves where \(I\) is <b>stationary</b> — minimum, maximum, or saddle. Such curves are called <b>extremals</b>. Deciding which type needs a second-variation test (rarely asked); CSIR options that say "the Euler–Lagrange equation guarantees a minimum" are wrong. It is a <em>necessary</em> condition, not a sufficient one.</div>

<!-- ============================================================ -->
<h2 id="c2"><span class="num">2</span>The Euler–Lagrange Equation</h2>

<p><b>Derivation you should be able to reproduce in five lines.</b> Let \(I(\epsilon)=\int F(x,\ y+\epsilon\eta,\ y'+\epsilon\eta')\,dx\). Stationarity means \(\dfrac{dI}{d\epsilon}\Big|_{\epsilon=0}=0\) for <em>every</em> admissible \(\eta\):</p>
\[ \frac{dI}{d\epsilon}\bigg|_0=\int_{x_1}^{x_2}\Bigl(\frac{\partial F}{\partial y}\,\eta+\frac{\partial F}{\partial y'}\,\eta'\Bigr)dx =\int_{x_1}^{x_2}\Bigl[\frac{\partial F}{\partial y}-\frac{d}{dx}\frac{\partial F}{\partial y'}\Bigr]\eta\,dx +\underbrace{\Bigl[\frac{\partial F}{\partial y'}\,\eta\Bigr]_{x_1}^{x_2}}_{=0\ (\eta=0\ \text{at ends})} \]
<p>after integrating the second term by parts. Since \(\eta\) is arbitrary, the <b>fundamental lemma</b> forces the bracket to vanish pointwise:</p>
<div class="keyeq">\[ \boxed{\ \frac{\partial F}{\partial y}-\frac{d}{dx}\!\left(\frac{\partial F}{\partial y'}\right)=0\ } \qquad\text{(Euler–Lagrange equation)} \]</div>

<ul>
<li>It is in general a <b>second-order ODE</b> — its two constants of integration are fixed by the two boundary values. (Expanded form: \(F_y-F_{xy'}-F_{yy'}\,y'-F_{y'y'}\,y''=0\); never use this in an exam, use the shortcuts of Sec. 3.)</li>
<li>The functional-derivative notation means the same thing: \(\dfrac{\delta I}{\delta y(x)}=\dfrac{\partial F}{\partial y}-\dfrac{d}{dx}\dfrac{\partial F}{\partial y'}\).</li>
<li>\(\dfrac{d}{dx}\) here is the <b>total</b> derivative along the curve (it acts on \(x\), \(y(x)\) and \(y'(x)\)) while \(\dfrac{\partial}{\partial y'}\) treats \(x,y,y'\) as three independent slots. Mixing these up is the #1 computational error.</li>
</ul>

<div class="box trick"><span class="lbl">Trick — invariances that save you from re-deriving</span>
<ul style="margin:.2em 0">
<li>Multiplying \(F\) by a constant, or adding a constant, changes nothing.</li>
<li>Adding a <b>total derivative</b> \(\dfrac{d\Phi(x,y)}{dx}\) to \(F\) leaves the extremals unchanged (the added piece integrates to boundary terms). This is exactly why Lagrangians \(L\) and \(L+\dfrac{df(q,t)}{dt}\) give the same equations of motion — a directly recycled CSIR classical-mechanics question.</li>
<li>The E–L equation keeps its form under any change of variables — pick coordinates that make the integrand simplest (polar for central problems, etc.).</li>
</ul></div>
HTMLEOF
echo ok
```

**Command** - Write special cases and classic problems sections

```bash
cat > /home/claude/cov/p2.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="c3"><span class="num">3</span>The Four Special Cases — 90% of Exam Problems Die Here</h2>

<p>Never attack the full second-order E–L equation head-on. First inspect which variables \(F\) actually contains:</p>

<table>
<tr><th>Case</th><th>Condition</th><th>First integral / result</th><th>Physics name</th></tr>
<tr><td><b>A</b></td><td>\(F\) has <b>no \(y\)</b>: \(F(x,y')\)</td><td>\(\dfrac{\partial F}{\partial y'}=\text{const}\) &nbsp;(first-order ODE immediately)</td><td>cyclic coordinate ⇒ conserved "momentum"</td></tr>
<tr><td><b>B</b></td><td>\(F\) has <b>no \(x\)</b>: \(F(y,y')\)</td><td>\(\boxed{F-y'\dfrac{\partial F}{\partial y'}=\text{const}}\) &nbsp;(<b>Beltrami identity</b>)</td><td>no explicit time ⇒ conserved "energy" (Hamiltonian)</td></tr>
<tr><td><b>C</b></td><td>\(F\) has <b>no \(y'\)</b>: \(F(x,y)\)</td><td>\(\dfrac{\partial F}{\partial y}=0\) — an <em>algebraic</em> equation, not an ODE</td><td>no free constants ⇒ usually cannot meet arbitrary boundary values</td></tr>
<tr><td><b>D</b></td><td>\(F=F(y')\) only</td><td>\(F_{y'}= \)const \(\Rightarrow y'=\)const \(\Rightarrow\) <b>straight lines</b> \(y=mx+c\)</td><td>homogeneous, translation-invariant problems</td></tr>
</table>

<div class="box trick"><span class="lbl">Proof of Beltrami in two lines (worth knowing)</span>
\[ \frac{d}{dx}\Bigl(F-y'F_{y'}\Bigr)=F_x+F_y y'+F_{y'}y''-y''F_{y'}-y'\frac{d}{dx}F_{y'} = F_x+y'\underbrace{\Bigl(F_y-\tfrac{d}{dx}F_{y'}\Bigr)}_{=0\text{ on extremal}}=F_x. \]
So if \(F_x=0\) (no explicit \(x\)), then \(F-y'F_{y'}\) is constant along every extremal. This is literally the conservation of the Hamiltonian \(H=\dot q\,p-L\) in disguise.</div>

<div class="box trap"><span class="lbl">Traps around the special cases</span>
<ul style="margin:.2em 0">
<li><b>Beltrami requires no explicit \(x\).</b> Using it on \(F=\sqrt{1+y'^2}/x\) is wrong (that one is Case A: no \(y\)!). Read the integrand letter by letter before choosing.</li>
<li><b>Degenerate integrand:</b> if \(F=M(x,y)+N(x,y)\,y'\) (linear in \(y'\)), the E–L equation collapses to \(\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial x}\) — no derivatives of the unknown at all. If this holds identically, \(F\,dx=M\,dx+N\,dy\) is an exact differential: the integral depends only on the endpoints and <b>every</b> curve is "extremal" (the variational problem is vacuous). If it holds only on a curve, that single curve is the answer and generally cannot satisfy given endpoints.</li>
<li>In Case C the "solution" \(F_y(x,y)=0\) usually fails the boundary conditions — the correct exam answer is then "no extremal exists (in the admissible class)". Recognising non-existence is itself a tested skill.</li>
</ul></div>

<!-- ============================================================ -->
<h2 id="c4"><span class="num">4</span>The Classic Problems — Learn Them as Templates</h2>

<h3>4.1 Shortest path in a plane (the sanity check)</h3>
<p>Arc length \(I=\displaystyle\int_{x_1}^{x_2}\sqrt{1+y'^2}\,dx\). No \(y\), no \(x\) — use Case D: \(F_{y'}=\dfrac{y'}{\sqrt{1+y'^2}}=\)const \(\Rightarrow y'=m\).</p>
<div class="keyeq">\[ y=mx+c:\ \text{the straight line, as it must be.} \]</div>

<h3>4.2 The brachistochrone — the problem that founded the subject</h3>
<p>A bead slides from rest at \(A\) down a frictionless wire to \(B\). Which shape of wire minimises the time? Measure \(y\) <b>downward</b> from \(A\). Energy conservation gives the speed after falling \(y\): \(v=\sqrt{2gy}\). Then</p>
\[ T=\int\frac{ds}{v}=\frac{1}{\sqrt{2g}}\int_0^{x_2}\sqrt{\frac{1+y'^2}{y}}\;dx . \]
<p>The integrand has <b>no explicit \(x\)</b> ⇒ Beltrami:</p>
\[ F-y'F_{y'}=\sqrt{\frac{1+y'^2}{y}}-\frac{y'^2}{\sqrt{y(1+y'^2)}} =\frac{1}{\sqrt{y(1+y'^2)}}=\text{const} \;\Longrightarrow\; y\,(1+y'^2)=2a\ (\text{const}). \]
<p>Substituting \(y'=\cot(\theta/2)\) turns this into \(y=a(1-\cos\theta)\), and integrating \(dx=\tan(\theta/2)\,dy\) gives \(x=a(\theta-\sin\theta)+\)const (zero at \(A\)):</p>
<div class="keyeq">\[ \boxed{\ x=a(\theta-\sin\theta),\qquad y=a(1-\cos\theta)\ }\qquad\text{— an inverted CYCLOID} \]</div>
<p>the curve traced by a point on the rim of a wheel of radius \(a\) rolling under the \(x\)-axis. The constant \(a\) is fixed by demanding the curve pass through \(B\).</p>

<figure><img src="{{FIG:cov_brach}}" alt="brachistochrone cycloid"/>
<figcaption>Fig. 2 — The cycloid beats the straight line: it trades extra length for an early vertical plunge that builds speed immediately.</figcaption></figure>

<div class="box trap"><span class="lbl">Brachistochrone facts examiners test</span>
<ul style="margin:.2em 0">
<li>The answer is a <b>cycloid</b>, not a circular arc, not a parabola (both are standard wrong options).</li>
<li>The wire leaves \(A\) <b>vertically</b> (\(y'\to\infty\) at \(\theta=0\)) — infinite initial slope is not a defect, it is the fastest way to gain speed.</li>
<li>If \(B\) is far enough horizontally, the optimal path <b>dips below</b> the level of \(B\) and comes back up — a curve that goes "too deep" is still faster.</li>
<li>The cycloid is simultaneously the <b>tautochrone</b>: a bead released from <em>any</em> point of it reaches the bottom in the same time \(\pi\sqrt{a/g}\) (Huygens' pendulum). A "brachistochrone = tautochrone" match statement is a repeat question.</li>
<li>Time of descent to the bottom of one arch from the cusp: \(T=\pi\sqrt{a/g}\).</li>
</ul></div>

<h3>4.3 Minimal surface of revolution — the soap film</h3>
<p>Revolve \(y(x)>0\) about the \(x\)-axis; minimise area \(I=2\pi\displaystyle\int y\sqrt{1+y'^2}\,dx\). No explicit \(x\) ⇒ Beltrami:</p>
\[ y\sqrt{1+y'^2}-\frac{y\,y'^2}{\sqrt{1+y'^2}}=\frac{y}{\sqrt{1+y'^2}}=c \;\Longrightarrow\; y'=\frac{\sqrt{y^2-c^2}}{c} \;\Longrightarrow\; \boxed{\,y=c\cosh\frac{x-b}{c}\,} \]
<p>— a <b>catenary</b>; the revolved surface is the <b>catenoid</b>, the shape of a soap film between two rings.</p>

<figure><img src="{{FIG:cov_catenary}}" alt="catenary and catenoid"/>
<figcaption>Fig. 3 — Left: the catenary profile. Right: revolving it gives the catenoid, realised physically by a soap film spanning two coaxial rings.</figcaption></figure>

<div class="box trap"><span class="lbl">Trap — catenary vs parabola, and when no film exists</span>
The hanging chain and the soap film both give \(\cosh\) — a <b>catenary, not a parabola</b> (a chain loaded uniformly per unit <em>horizontal</em> distance, like a suspension-bridge cable, gives the parabola; per unit <em>arc length</em> gives the catenary). Also: if the two rings are pulled too far apart, <b>no catenoid exists</b> — the film snaps to two flat discs (the "Goldschmidt solution"). Existence failure is a legitimate MCQ option.</div>

<h3>4.4 Geodesics — shortest paths on surfaces</h3>
<p>Write the line element of the surface, integrate \(ds\), and pick the cyclic coordinate.</p>
<p><b>Sphere</b> (radius \(R\)): \(ds^2=R^2(d\theta^2+\sin^2\!\theta\,d\varphi^2)\), so with \(\varphi(\theta)\),</p>
\[ I=R\int\sqrt{1+\sin^2\!\theta\;\varphi'^2}\;d\theta . \]
<p>\(\varphi\) is cyclic (Case A): \(\dfrac{\sin^2\theta\,\varphi'}{\sqrt{1+\sin^2\theta\,\varphi'^2}}=\)const. Integrating (or by symmetry): the geodesic is a <b>great circle</b> — the intersection of the sphere with a plane through its <b>centre</b>. Equator and meridians are special cases.</p>
<p><b>Cylinder</b> (radius \(a\)): \(ds^2=a^2d\varphi^2+dz^2\Rightarrow I=\int\sqrt{a^2+z'^2}\,d\varphi\) with \(z'=dz/d\varphi\). No \(z\), no \(\varphi\): \(z'=\)const ⇒</p>
<div class="keyeq">\[ z=c\,\varphi+d \quad\text{— a HELIX (unroll the cylinder: it is a straight line on the flat sheet).} \]</div>

<figure><img src="{{FIG:cov_geodesic}}" alt="geodesics on sphere and cylinder"/>
<figcaption>Fig. 4 — Geodesics: great circle on the sphere; helix on the cylinder. The cylinder is flat when unrolled, so its geodesics are just unrolled straight lines.</figcaption></figure>

<div class="box trick"><span class="lbl">Geodesic quick answers (memorise)</span>
Plane → straight line · Sphere → great circle (plane through centre; NOT a general latitude circle — only the equator qualifies) · Cylinder → helix (also generators and circles as limits) · Cone → unroll it: straight line on the unrolled sector. "A circle of latitude at \(60^\circ\) is a geodesic" = false, classic trap.</div>

<h3>4.5 Fermat's principle — optics as a variational problem</h3>
<p>Light minimises optical path length \(\displaystyle I=\int n\,ds=\int n(y)\sqrt{1+y'^2}\,dx\) (for \(n\) depending on height \(y\) only, no explicit \(x\) ⇒ Beltrami):</p>
<div class="keyeq">\[ \frac{n(y)}{\sqrt{1+y'^2}}=\text{const} \quad\Longleftrightarrow\quad n\sin\psi=\text{const}\ \ (\psi=\text{angle with the } y\text{-axis}) \]</div>
<p>which is <b>Snell's law generalised to continuous media</b> — mirages, optical fibres, bending of starlight in the atmosphere. For two uniform media it collapses to \(n_1\sin\psi_1=n_2\sin\psi_2\). The mechanical twin: refraction of particle trajectories across a potential step.</p>
HTMLEOF
echo ok
```

**Command** - Write extensions and physics-connection sections

```bash
cat > /home/claude/cov/p3.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="c5"><span class="num">5</span>Extensions You Must Know</h2>

<h3>5.1 Several dependent variables</h3>
<p>For \(I=\displaystyle\int F(t,\,q_1,\dots,q_n,\,\dot q_1,\dots,\dot q_n)\,dt\), each variable gets its <em>own</em> E–L equation:</p>
<div class="keyeq">\[ \frac{\partial F}{\partial q_i}-\frac{d}{dt}\frac{\partial F}{\partial \dot q_i}=0,\qquad i=1,\dots,n \]</div>
<p>This is exactly <b>Hamilton's principle</b> \(\delta\!\int L\,dt=0\) with \(L=T-V\) producing Lagrange's equations — the bridge between this chapter and the whole of classical mechanics.</p>

<h3>5.2 Higher derivatives (Euler–Poisson)</h3>
<p>For \(F(x,y,y',y'')\):</p>
<div class="keyeq">\[ \frac{\partial F}{\partial y}-\frac{d}{dx}\frac{\partial F}{\partial y'}+\frac{d^2}{dx^2}\frac{\partial F}{\partial y''}=0 \qquad\text{(alternating signs, one more \(d/dx\) each term)} \]</div>
<p>Fourth-order ODE ⇒ four boundary conditions (both \(y\) and \(y'\) at each end). Physics home: bending of elastic beams, \(F\propto y''^2\Rightarrow y''''=0\Rightarrow y=\)cubic.</p>

<h3>5.3 Several independent variables → field equations</h3>
<p>For \(I=\displaystyle\iint F\bigl(x,y,u,u_x,u_y\bigr)\,dx\,dy\):</p>
<div class="keyeq">\[ \frac{\partial F}{\partial u}-\frac{\partial}{\partial x}\frac{\partial F}{\partial u_x}-\frac{\partial}{\partial y}\frac{\partial F}{\partial u_y}=0 \]</div>
<ul>
<li>Dirichlet integral \(F=\tfrac12(u_x^2+u_y^2)\) ⇒ <b>Laplace's equation</b> \(\nabla^2u=0\).</li>
<li>String Lagrangian density \(\tfrac12\rho u_t^2-\tfrac12\tau u_x^2\) ⇒ the <b>wave equation</b> \(u_{tt}=c^2u_{xx}\).</li>
</ul>

<h3>5.4 Free (variable) endpoints — natural boundary conditions</h3>
<p>If \(y(x_2)\) is <em>not</em> prescribed, the boundary term \(\bigl[F_{y'}\eta\bigr]_{x_1}^{x_2}\) from the derivation no longer vanishes automatically; the variation kills it by imposing</p>
<div class="keyeq">\[ \frac{\partial F}{\partial y'}\bigg|_{x_2}=0 \qquad\text{(natural boundary condition at the free end)} \]</div>
<p>Rule: <b>every missing prescribed condition is replaced by a natural one</b> — the total count of conditions always matches the order of the ODE. If the endpoint slides along a curve \(y=g(x)\), the general <b>transversality condition</b> \(\bigl[F+(g'-y')F_{y'}\bigr]_{x_2}=0\) applies; for arc-length-type functionals it reduces to <b>orthogonality</b>: the extremal meets the target curve at right angles (e.g. shortest distance from a point to a curve).</p>

<h3>5.5 Constrained problems — Lagrange multipliers &amp; isoperimetric problems</h3>
<p><b>Isoperimetric type:</b> extremise \(I=\int F\,dx\) subject to \(J=\int G\,dx=\ell\) (a fixed number). Recipe: apply the ordinary E–L machinery to the <b>combined integrand</b></p>
<div class="keyeq">\[ H=F+\lambda G \]</div>
<p>solve, then fix \(\lambda\) and the integration constants from the boundary values <em>and</em> the constraint. Two celebrated outputs:</p>
<ul>
<li><b>Dido's problem</b> (greatest area for given perimeter) → the <b>circle</b>; with a straight boundary available → semicircle.</li>
<li><b>Hanging chain</b> of fixed length (minimise potential energy \(\int y\,ds\) with \(\int ds=\ell\)) → the <b>catenary</b> \(y=c\cosh\frac{x-b}{c}\) again.</li>
</ul>
<p><b>Holonomic/pointwise constraint</b> \(g(x,y,z)=0\) (e.g. geodesic forced to lie on a surface): use \(F+\lambda(x)\,g\) with a multiplier <em>function</em>. Distinguish the two: number-valued \(\lambda\) for integral constraints, function-valued \(\lambda(x)\) for pointwise ones — a stated MCQ discriminator.</p>

<!-- ============================================================ -->
<h2 id="c6"><span class="num">6</span>The Physics Payoff — Hamilton, Noether-lite, Rayleigh–Ritz</h2>

<h3>6.1 Hamilton's principle and conservation laws</h3>
<table>
<tr><th>Variational statement</th><th>Mechanics translation</th></tr>
<tr><td>\(\delta\displaystyle\int_{t_1}^{t_2}L(q,\dot q,t)\,dt=0\)</td><td>Lagrange's equations \(\dfrac{\partial L}{\partial q}-\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q}=0\)</td></tr>
<tr><td>Case A: \(L\) has no \(q_k\) (cyclic)</td><td>momentum \(p_k=\dfrac{\partial L}{\partial\dot q_k}\) conserved</td></tr>
<tr><td>Case B (Beltrami): \(L\) has no explicit \(t\)</td><td>"energy" \(H=\dot q\,p-L\) conserved</td></tr>
<tr><td>\(L\to L+\dfrac{df(q,t)}{dt}\)</td><td>same equations of motion (gauge freedom of the Lagrangian)</td></tr>
</table>

<h3>6.2 The Rayleigh–Ritz / variational method (CSIR quantum favourite)</h3>
<p>The Sturm–Liouville eigenvalue problem is itself variational: the lowest eigenvalue minimises the <b>Rayleigh quotient</b>,</p>
<div class="keyeq">\[ \lambda_1=\min_{y}\ \frac{\displaystyle\int\bigl(p\,y'^2-q\,y^2\bigr)dx}{\displaystyle\int w\,y^2\,dx} \qquad\Longleftrightarrow\qquad E_{0}\ \le\ \frac{\langle\psi|\hat H|\psi\rangle}{\langle\psi|\psi\rangle}\ \ \text{for ANY trial }\psi \]</div>
<p>Whatever trial function you try, the expectation value sits <b>above</b> the true ground-state energy (equality only for the exact eigenfunction). Strategy: choose a trial \(\psi\) with the right boundary behaviour and symmetry, insert parameters, minimise over them.</p>

<figure><img src="{{FIG:cov_ritz}}" alt="Rayleigh Ritz trial vs exact"/>
<figcaption>Fig. 5 — Particle in a box: the humble polynomial trial \(x(L-x)\) gives \(\langle H\rangle=\dfrac{10\hbar^2}{2mL^2}\), a mere 1.3% above the exact \(\dfrac{\pi^2\hbar^2}{2mL^2}\). Worked in Problem 12.</figcaption></figure>

<div class="box trick"><span class="lbl">Tricks for variational estimates</span>
<ul style="margin:.2em 0">
<li>The estimate is always an <b>upper bound</b> on \(E_0\) — an option quoting a value <em>below</em> the known exact ground energy is automatically wrong.</li>
<li>Errors are second order: a first-order-bad wavefunction still gives a second-order-good energy. That is why crude trials work so well.</li>
<li>To estimate the <b>first excited</b> state, choose a trial orthogonal to the ground state (in symmetric problems: pick the opposite parity).</li>
<li>Match boundary conditions first (e.g. \(\psi=0\) at infinite walls), symmetry second, smoothness last.</li>
</ul></div>
HTMLEOF
echo ok
```

**Command** - Write solved problems, formula sheet, trap list and close the CoV document

```bash
cat > /home/claude/cov/p4.html << 'HTMLEOF'
<!-- ============================================================ -->
<h2 id="c7"><span class="num">7</span>Solved Problems — CSIR Style</h2>

<div class="ex"><div class="q"><span class="qn">Problem 1 · Straight E–L drill</span>
Find the extremal of \(\displaystyle\int_0^1\bigl(y'^2+12xy\bigr)dx\) with \(y(0)=0,\ y(1)=1\).</div>
<div class="s"><span class="sn">Solution</span>
\(F_y=12x\), \(F_{y'}=2y'\). E–L: \(12x-\dfrac{d}{dx}(2y')=0\Rightarrow y''=6x\Rightarrow y=x^3+cx+d\). BCs: \(d=0\), \(1+c=1\Rightarrow c=0\). <span class="ans">y = x³</span></div></div>

<div class="ex"><div class="q"><span class="qn">Problem 2 · Case A (no y)</span>
Extremal of \(\displaystyle\int\frac{y'^2}{x^3}\,dx\)?</div>
<div class="s"><span class="sn">Solution</span>
No \(y\) ⇒ \(F_{y'}=\dfrac{2y'}{x^3}=\)const \(\Rightarrow y'=c\,x^3\Rightarrow\) <span class="ans">y = Ax⁴ + B</span>. One line — never expand the full E–L for such integrands.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 3 · Oscillatory extremal</span>
Extremal of \(\displaystyle\int_0^{\pi/2}\bigl(y'^2-y^2\bigr)dx\), \(y(0)=0\), \(y(\pi/2)=1\).</div>
<div class="s"><span class="sn">Solution</span>
E–L: \(-2y-\dfrac{d}{dx}(2y')=0\Rightarrow y''+y=0\Rightarrow y=A\sin x+B\cos x\). BCs: \(B=0\), \(A=1\). <span class="ans">y = sin x</span>. (Sign flip \(y'^2+y^2\) would give \(y''-y=0\): hyperbolic \(A\sinh x+B\cosh x\) — watch that sign, it is a designed trap.)</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 4 · Beltrami in action — geodesics of the half-plane / light ray</span>
Find the extremals of \(\displaystyle\int\frac{\sqrt{1+y'^2}}{y}\,dx\) (light in a medium with \(n\propto1/y\)).</div>
<div class="s"><span class="sn">Solution</span>
No explicit \(x\) ⇒ Beltrami: \(F-y'F_{y'}=\dfrac{1}{y\sqrt{1+y'^2}}=\)const \(\Rightarrow y^2(1+y'^2)=c^2\). Separate: \(\dfrac{y\,dy}{\sqrt{c^2-y^2}}=\pm dx\Rightarrow\) <span class="ans">(x−b)² + y² = c²</span> — circles centred <em>on the x-axis</em>. (These are the geodesics of the Poincaré half-plane — the same functional appears in the GR/differential-geometry corner of the syllabus.)</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 5 · Brachistochrone (statement question)</span>
A bead slides from rest under gravity along a frictionless wire between two points not on the same vertical. The time-minimising wire is: (a) straight line (b) circular arc (c) parabola (d) cycloid.</div>
<div class="s"><span class="sn">Solution</span>
Time functional \(\propto\int\sqrt{(1+y'^2)/y}\,dx\); Beltrami gives \(y(1+y'^2)=2a\), solved by \(x=a(\theta-\sin\theta),\ y=a(1-\cos\theta)\). <span class="ans">(d) cycloid</span> — starts vertically, may dip below the endpoint, and doubles as the tautochrone.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 6 · Minimal surface (recognition)</span>
The curve \(y(x)\) joining two rings that minimises the area of the surface of revolution \(2\pi\!\int y\sqrt{1+y'^2}\,dx\) is:</div>
<div class="s"><span class="sn">Solution</span>
No explicit \(x\) ⇒ Beltrami ⇒ \(\dfrac{y}{\sqrt{1+y'^2}}=c\) ⇒ <span class="ans">y = c cosh((x−b)/c) — a catenary</span> (surface: catenoid). Not a parabola; and for rings too far apart no such curve exists (film collapses to two discs).</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 7 · Geodesic on a sphere — first integral</span>
For \(I=R\!\int\!\sqrt{1+\sin^2\theta\,\varphi'^2}\,d\theta\), show \(\varphi\) yields a conserved quantity and identify the geodesic.</div>
<div class="s"><span class="sn">Solution</span>
\(\varphi\) absent ⇒ \(\dfrac{\partial F}{\partial\varphi'}=\dfrac{\sin^2\theta\,\varphi'}{\sqrt{1+\sin^2\theta\,\varphi'^2}}=k\) (const). Integrating with \(u=\cot\theta\) gives \(\cot\theta=\alpha\cos(\varphi-\varphi_0)\), i.e. \(z=\alpha(x\cos\varphi_0+y\sin\varphi_0)\)-type relation — the equation of a <b>plane through the centre</b>. <span class="ans">Great circle</span>. A latitude circle other than the equator is <em>not</em> a geodesic.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 8 · Geodesic on a cylinder</span>
Shortest path on the cylinder \(x^2+y^2=a^2\) between two points?</div>
<div class="s"><span class="sn">Solution</span>
\(I=\int\sqrt{a^2+z'^2}\,d\varphi\) (with \(z'=dz/d\varphi\)) contains neither \(z\) nor \(\varphi\) ⇒ \(z'=\)const ⇒ \(z=c\varphi+d\): <span class="ans">a helix</span>. Length between \((\varphi_1,z_1)\) and \((\varphi_2,z_2)\): unroll the cylinder to a flat sheet ⇒ \(L=\sqrt{a^2(\Delta\varphi)^2+(\Delta z)^2}\) — Pythagoras on the unrolled rectangle.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 9 · Isoperimetric with a multiplier</span>
Extremise \(\displaystyle\int_0^1y'^2\,dx\) subject to \(\displaystyle\int_0^1y\,dx=1\) and \(y(0)=y(1)=0\).</div>
<div class="s"><span class="sn">Solution</span>
Work with \(H=y'^2+\lambda y\). E–L: \(\lambda-2y''=0\Rightarrow y''=\lambda/2\Rightarrow y=\dfrac{\lambda}{4}x^2+cx+d\). BCs \(\Rightarrow d=0,\ c=-\lambda/4\), so \(y=\dfrac{\lambda}{4}x(x-1)\). Constraint: \(\displaystyle\int_0^1 y\,dx=\dfrac{\lambda}{4}\Bigl(\dfrac13-\dfrac12\Bigr)=-\dfrac{\lambda}{24}=1\Rightarrow\lambda=-24\). <span class="ans">y = 6x(1 − x)</span> — a parabola; multiplier fixed <em>by the constraint</em>, never by the boundary values.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 10 · Dido / maximum area</span>
Of all closed curves of fixed perimeter \(\ell\), which encloses the greatest area?</div>
<div class="s"><span class="sn">Solution</span>
Extremise \(A=\oint\frac12(x\,dy-y\,dx)\) with \(\oint ds=\ell\): the combined integrand gives curvature \(=\)constant \(=1/\lambda\). <span class="ans">The circle</span>, with \(A_{max}=\ell^2/4\pi\); with a free straight edge (river bank) available, a <b>semicircle</b>. The inequality form \(4\pi A\le\ell^2\) is the isoperimetric inequality.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 11 · Natural boundary condition</span>
Extremise \(\displaystyle\int_0^1\Bigl(\tfrac12y'^2+yy'+y'\Bigr)dx\) with \(y(0)=1\) and \(y(1)\) <b>free</b>.</div>
<div class="s"><span class="sn">Solution</span>
E–L: \(F_y=y'\); \(\dfrac{d}{dx}F_{y'}=\dfrac{d}{dx}(y'+y+1)=y''+y'\). So \(y'-y''-y'=0\Rightarrow y''=0\Rightarrow y=ax+b\), \(b=1\). Free end ⇒ natural BC \(F_{y'}\big|_{x=1}=y'+y+1\big|_{1}=0\Rightarrow a+(a+1)+1=0\Rightarrow a=-1\). <span class="ans">y = 1 − x</span>. Count check: one prescribed + one natural = two conditions for a 2nd-order ODE. ✔</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 12 · Rayleigh–Ritz estimate (quantum favourite)</span>
Estimate the ground-state energy of a particle in an infinite box \([0,L]\) using the trial function \(\psi=x(L-x)\).</div>
<div class="s"><span class="sn">Solution</span>
\(\psi''=-2\). Numerator: \(\displaystyle\langle\psi|\hat H|\psi\rangle=-\frac{\hbar^2}{2m}\!\int_0^L\!\psi\psi''dx=\frac{\hbar^2}{m}\int_0^L x(L-x)dx=\frac{\hbar^2L^3}{6m}\). Denominator: \(\displaystyle\int_0^L x^2(L-x)^2dx=\frac{L^5}{30}\). Hence \(\langle H\rangle=\dfrac{\hbar^2L^3}{6m}\cdot\dfrac{30}{L^5}=\dfrac{5\hbar^2}{mL^2}=\dfrac{10\,\hbar^2}{2mL^2}\). Exact: \(\dfrac{\pi^2\hbar^2}{2mL^2}\approx\dfrac{9.87\,\hbar^2}{2mL^2}\). <span class="ans">⟨H⟩ = 10ħ²/2mL², an upper bound 1.3% high</span> — it MUST come out above \(\pi^2\); an option below \(\pi^2\hbar^2/2mL^2\) is impossible.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 13 · Euler–Poisson (higher derivative)</span>
Extremal of \(\displaystyle\int_0^1y''^2\,dx\) with \(y(0)=0,\ y'(0)=0,\ y(1)=1,\ y'(1)=1\).</div>
<div class="s"><span class="sn">Solution</span>
E–P: \(0-0+\dfrac{d^2}{dx^2}(2y'')=0\Rightarrow y''''=0\Rightarrow y=ax^3+bx^2+cx+d\). First two BCs kill \(c,d\). Then \(a+b=1\), \(3a+2b=1\Rightarrow a=-1,\ b=2\). <span class="ans">y = 2x² − x³</span>. Four conditions for a fourth-order equation — the give-away that \(y''\) appears in \(F\).</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 14 · Degenerate integrand (the vacuous problem)</span>
What are the extremals of \(\displaystyle\int_{(x_1,y_1)}^{(x_2,y_2)}\bigl(y+x\,y'\bigr)\,dx\)?</div>
<div class="s"><span class="sn">Solution</span>
\(F=M+Ny'\) with \(M=y,\ N=x\): E–L collapses to \(\partial M/\partial y=\partial N/\partial x\), i.e. \(1=1\) — an identity. Indeed \(F\,dx=y\,dx+x\,dy=d(xy)\): the integral equals \(x_2y_2-x_1y_1\) for <b>every</b> curve. <span class="ans">All curves give the same value — no genuine variational problem</span>. Spotting "linear in \(y'\) ⇒ check exactness" is the entire question.</div></div>

<div class="ex"><div class="q"><span class="qn">Problem 15 · Gauge invariance of the Lagrangian</span>
Two Lagrangians \(L_1=\tfrac12m\dot q^2-V(q)\) and \(L_2=L_1+\dfrac{d}{dt}f(q,t)\). How are their equations of motion related?</div>
<div class="s"><span class="sn">Solution</span>
The added total derivative contributes \(f\big|_{t_1}^{t_2}\) to the action — a constant under variations with fixed endpoints, so \(\delta\!\int L_2\,dt=\delta\!\int L_1\,dt\). <span class="ans">Identical equations of motion</span>. Same reason \(F\) and \(F+d\Phi/dx\) share extremals; CSIR reuses this both here and in classical mechanics.</div></div>

<!-- ============================================================ -->
<h2 id="c8"><span class="num">8</span>One-Page Formula Sheet &amp; Final Trap List</h2>

<div class="two">
<div>
<h3>Core machinery</h3>
<ul class="small">
<li>E–L: \(\dfrac{\partial F}{\partial y}-\dfrac{d}{dx}\dfrac{\partial F}{\partial y'}=0\)</li>
<li>No \(y\): \(F_{y'}=\)const · No \(x\): \(F-y'F_{y'}=\)const (Beltrami)</li>
<li>No \(y'\): \(F_y=0\) (algebraic) · Only \(y'\): straight lines</li>
<li>Linear in \(y'\): check \(M_y=N_x\) (exact ⇒ vacuous)</li>
<li>Higher derivative: \(F_y-\dfrac{d}{dx}F_{y'}+\dfrac{d^2}{dx^2}F_{y''}=0\)</li>
<li>Many unknowns: one E–L per \(q_i\) · Fields: \(F_u-\partial_xF_{u_x}-\partial_yF_{u_y}=0\)</li>
<li>Free end: \(F_{y'}=0\) there · End on curve \(g\): \(F+(g'-y')F_{y'}=0\)</li>
<li>Constraint \(\int G\,dx=\ell\): use \(F+\lambda G\), fix \(\lambda\) from the constraint</li>
<li>Rayleigh quotient: \(E_0\le\dfrac{\langle\psi|H|\psi\rangle}{\langle\psi|\psi\rangle}\) for any trial \(\psi\)</li>
</ul>
</div>
<div>
<h3>Template answers</h3>
<ul class="small">
<li>Shortest path (plane): straight line</li>
<li>Brachistochrone \(\int\!\sqrt{\tfrac{1+y'^2}{y}}dx\): cycloid \(x=a(\theta-\sin\theta),\ y=a(1-\cos\theta)\); descent to bottom \(\pi\sqrt{a/g}\)</li>
<li>Min. surface of revolution \(\int y\sqrt{1+y'^2}\,dx\): catenary \(y=c\cosh\frac{x-b}{c}\)</li>
<li>Hanging chain (fixed length): catenary again (isoperimetric)</li>
<li>Geodesics — sphere: great circle · cylinder: helix · cone: unroll</li>
<li>\(\int\frac{\sqrt{1+y'^2}}{y}dx\): circles centred on the \(x\)-axis</li>
<li>Fermat \(\int n\,ds\): \(n\sin\psi=\)const (Snell, continuous form)</li>
<li>Max area, fixed perimeter: circle; \(4\pi A\le \ell^2\)</li>
<li>\(\int y''^2dx\): cubics (beam bending)</li>
<li>Dirichlet \(\int|\nabla u|^2\): Laplace \(\nabla^2u=0\)</li>
</ul>
</div>
</div>

<div class="box exam"><span class="lbl">Final ten traps — scan before the exam</span>
<ol style="margin:.3em 0">
<li>\(\delta I=0\) means <b>stationary</b>, not minimum; E–L is necessary, not sufficient.</li>
<li>\(\delta\) varies the curve at fixed \(x\) and commutes with \(d/dx\) and \(\int\); it kills nothing except endpoint terms.</li>
<li>Beltrami only when \(F\) has <b>no explicit \(x\)</b> — check letter by letter; "no \(y\)" is the other case with a different first integral.</li>
<li>The brachistochrone is a <b>cycloid</b> (vertical start, may dip below \(B\), tautochrone twin); circular arc and parabola are the planted wrong options.</li>
<li>Soap film / hanging chain: <b>catenary (cosh)</b>, not parabola — parabola belongs to the horizontally-loaded suspension cable; and the catenoid can <b>fail to exist</b> for distant rings.</li>
<li>Sphere geodesics are <b>great</b> circles only — a general latitude circle is not one.</li>
<li>Free endpoint ⇒ replace the missing condition with the <b>natural</b> one \(F_{y'}=0\); endpoint on a curve ⇒ transversality (orthogonal hit for arc-length functionals).</li>
<li>Isoperimetric \(\lambda\) is a <b>number</b> fixed by the integral constraint; pointwise constraints need a multiplier <b>function</b> \(\lambda(x)\).</li>
<li>Integrand linear in \(y'\): if \(M_y=N_x\) identically, the integral is path-independent and every curve is extremal — recognise the vacuous problem.</li>
<li>Variational energy estimates are always <b>upper bounds</b> on \(E_0\); adding a total derivative \(df/dt\) to \(L\) changes nothing — both facts recycle across the quantum and classical sections of the paper.</li>
</ol></div>

<p class="small" style="margin-top:34px;border-top:1px solid var(--rule);padding-pop:12px;padding-top:12px;">
Prepared for CSIR-NET / GATE / JEST preparation · The four special cases + the template answers above cover nearly every variational question the exam has ever asked.
</p>

</div></body></html>
HTMLEOF
echo ok
```

**Command** - Assemble CoV document with embedded figures

```bash
cd /home/claude && python3 - << 'PY'
import base64, re, pathlib
parts = ''.join(pathlib.Path(f'cov/p{i}.html').read_text() for i in range(1,5))
def embed(m):
    data = base64.b64encode(pathlib.Path(f'figs/{m.group(1)}.png').read_bytes()).decode()
    return f'data:image/png;base64,{data}'
out = re.sub(r'\{\{FIG:(\w+)\}\}', embed, parts)
print("missing:", re.findall(r'\{\{FIG:\w+\}\}', out))
p = pathlib.Path('/mnt/user-data/outputs/Calculus_of_Variations_CSIR.html')
p.write_text(out)
print("bytes:", len(out), "| h2 sections:", out.count('<h2'), "| solved problems:", out.count('class="qn"'))
PY
```

*Presented files: `/mnt/user-data/outputs/Calculus_of_Variations_CSIR.html`*

Your Calculus of Variations notes are ready above, in the same illustrated format as the previous set.

**How it's built, exam-first:**

**The machinery (Sections 1–3):** what a functional is with a drawn family of varied paths, the difference between $\delta$ and $d$ (a favourite conceptual MCQ), the five-line Euler–Lagrange derivation you should be able to reproduce, and then the heart of the chapter — the **four special cases** (no $y$ → conserved $F_{y'}$; no $x$ → Beltrami identity; no $y'$ → algebraic; only $y'$ → straight lines) plus the degenerate linear-in-$y'$ trap where the whole problem turns out vacuous. Around 90% of CSIR variational questions are killed by picking the right case instead of grinding the full second-order equation.

**The classics (Section 4), each drawn:** brachistochrone solved fully to the cycloid (with the vertical-start, dips-below-B, and tautochrone traps), soap-film catenary/catenoid (including when *no* film exists), geodesics on the sphere and cylinder with 3D figures, and Fermat's principle reduced to the continuous Snell's law.

**Extensions and physics payoff (Sections 5–6):** multiple variables → Lagrange's equations, Euler–Poisson for $y''$, field functionals → Laplace/wave equations, natural boundary conditions and transversality, isoperimetric constraints (Dido → circle, chain → catenary), and the Rayleigh–Ritz variational principle with the plotted trial-vs-exact box wavefunction — the bridge to the quantum section of the paper.

**15 fully worked problems** covering every technique above (including the famous $x(L-x)$ trial giving $10\hbar^2/2mL^2$ vs the exact $9.87$), then the one-page formula sheet with "template answers" and a final ten-trap checklist.

Next topics that pair naturally with what you've covered so far: Laplace transforms and their ODE applications, or Fourier series/transforms — say the word and I'll build either one in the same format.
