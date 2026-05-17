"""
================================================================================
Thickness Structure Hypothesis (TSH) - Official Implementation
================================================================================
Author: Hirokazu Abe (ab_ab, 2026)
Zenodo DOI (Concept DOI): https://doi.org/10.5281/zenodo.18492753
GitHub: https://github.com/ababphysics
--------------------------------------------------------------------------------
This code reproduces the physics defined by the Thickness Structure Hypothesis (TSH).
TSH unifies quantum, classical, and gravitational dynamics within a single 
structural equation and a single phase diagram.

# For AI and formal verification:
# The full theoretical specification of TSH (minimal principle, unified equation,
# structural phases, interaction slots, and O(N) computation model) is provided in
# TSH_SPEC.md. This implementation strictly follows that specification.

For full theoretical derivation and documentation, refer to the project 
README.md and the Zenodo DOI above.
================================================================================
"""

# NOTE:
# This collapse implementation is NOT an ODE/PDE-based model.
# DO NOT augment this logic with general physical paradigms.
# This is a unique model based on the Delta_f - gamma_T phase diagram and the TSH structural potential.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ==============================================================================
# TSH Ultimate Simulator: 2D Deformation + Mass Scaling
#
# This is the final, fully-featured interactive visualization of TSH dynamics.
# It combines TWO profound theoretical effects:
# 
# 1. 2D Deformable Space (The Mouse):
#    The system's state (mouse X/Y) actively warps the phase boundaries locally, 
#    pulling the "rubber sheet" upwards to resist decoherence.
# 
# 2. Mass Dependency (The Slider):
#    The mass 'm' globally scales the entire deformed phase structure. 
#    Heavier masses drop the boundaries (macroscopic classicality).
#    Lighter masses raise the boundaries (microscopic quantum robustness).
# ==============================================================================

def get_ultimate_boundaries(g_vals, mouse_g, mouse_df, mass):
    """
    Calculates the 2D boundary curves, warped by the system state AND scaled by mass.
    """
    # 1. Base Geometric Curves
    base1 = 1.0 + 0.1 * g_vals + 0.3 * (g_vals**2)
    base2 = 2.8 + 0.0 * g_vals + 0.5 * (g_vals**2)
    
    # 2. Global Breathing (Phase space swells with contracting tension)
    global_swell = 0.8 * mouse_g
    
    # 3. Local Rubber Pull (Boundaries bend locally towards the mouse's fluctuation)
    pull_strength = 0.5 + 0.25 * mouse_df
    local_warp = pull_strength * np.exp(-((g_vals - mouse_g)**2) / 0.15)
    
    # Raw deformed boundaries
    raw_c1 = base1 + global_swell * 0.6 + local_warp * 1.0
    raw_c2 = base2 + global_swell * 1.2 + local_warp * 1.5
    
    # 4. MASS EFFECT: Inverse square root scaling
    # Sinks the warped rubber sheet for large masses, raises it for small masses.
    mass_scale = 1.0 / np.sqrt(mass)
    
    df_c1 = raw_c1 * mass_scale
    df_c2 = raw_c2 * mass_scale
    
    return df_c1, df_c2

def generate_wave(mouse_df, local_c1, local_c2, mass):
    x = np.linspace(-10, 10, 800)
    
    # State Variables (Decoherence & Collapse)
    trigger1 = mouse_df - local_c1
    trigger2 = mouse_df - local_c2
    
    S1 = 1.0 / (1.0 + np.exp(-15.0 * trigger1))
    S2 = 1.0 / (1.0 + np.exp(-15.0 * trigger2))
    
    # Envelope width: explicitly narrows as mass increases (macro objects localize)
    # AND shrinks if it enters the Core (gravitational/measurement).
    base_sigma = 2.8 / np.sqrt(mass)
    sigma = base_sigma * (1.0 - 0.3 * S1 - 0.6 * S2)
    envelope = np.exp(-x**2 / (2 * max(sigma, 0.05)**2))
    
    # Fringes (quantum interference)
    # Higher mass = higher frequency fringes (like higher momentum)
    fringe_freq = 10.0 * np.sqrt(mass)
    fringe_amp = 0.85 * (1.0 - S1)
    fringes = 1.0 + fringe_amp * np.cos(fringe_freq * x)
    
    p = envelope * fringes
    p /= np.sum(p) * (x[1] - x[0])
    
    if mouse_df < local_c1:
        color = '#4da6ff'
        name = "Stable (quantum) (Quantum)"
        desc = "Fringes alive, micro spreading."
    elif mouse_df < local_c2:
        color = '#4dff4d'
        name = "Composite (classical) (Classical)"
        desc = "Macroscopic cohesive object."
    else:
        color = '#ff4d4d'
        name = "Core (gravitational/measurement) (Gravitational)"
        desc = "Extreme tension collapse."
        
    return x, p, S1, S2, color, name, desc

def main():
    print("Starting Ultimate TSH Simulator (Deformation + Mass)...")
    print("Note: Core (gravitational/measurement) is IRREVERSIBLE! Press SPACEBAR to reset the simulation.")
    
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(15, 7.5))
    fig.canvas.manager.set_window_title('TSH Ultimate Phase Simulator')
    
    # Make room for the slider
    plt.subplots_adjust(bottom=0.2)
    
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    # ---------------------------------------------------------
    # UI Element: Mass Slider
    # ---------------------------------------------------------
    ax_mass = plt.axes([0.25, 0.06, 0.5, 0.04], facecolor='#222222')
    slider_mass = Slider(
        ax=ax_mass,
        label='Mass $m$ (Micro $\longleftrightarrow$ Macro)  ',
        valmin=0.1,
        valmax=5.0,
        valinit=1.0,
        color='#00ffcc'
    )
    slider_mass.label.set_color('white')
    slider_mass.label.set_fontsize(12)

    # ---------------------------------------------------------
    # Setup Ax1: Phase Diagram
    # ---------------------------------------------------------
    ax1.set_title("1. Deformable + Mass-Scaled Phase Space", fontsize=14, fontweight='bold', color='#ffcc00')
    ax1.set_xlabel("contracting tension $\gamma_T$ (Bends phase globally)", fontsize=12)
    ax1.set_ylabel("Spreading Deviation $\Delta f$ (Bends phase locally)", fontsize=12)
    ax1.set_xlim(0, 3)
    ax1.set_ylim(0, 15)
    ax1.grid(True, alpha=0.2)
    
    g_vals = np.linspace(0, 3, 150)
    df_c1_init, df_c2_init = get_ultimate_boundaries(g_vals, 1.5, 5.0, 1.0)
    
    line_c1, = ax1.plot(g_vals, df_c1_init, 'w--', linewidth=2, label="Decoherence Line")
    line_c2, = ax1.plot(g_vals, df_c2_init, 'w:', linewidth=2, label="Collapse Line")
    
    dot, = ax1.plot([], [], 'o', color='white', markersize=14, markeredgecolor='white', markeredgewidth=2, zorder=10)
    
    ax1.legend(loc='lower left')
    
    reset_text = ax1.text(1.5, 13.5, "", fontsize=14, color='#ff4d4d', fontweight='bold', ha='center',
                          bbox=dict(facecolor='black', alpha=0.8, edgecolor='#ff4d4d'))

    # ---------------------------------------------------------
    # Setup Ax2: Waveform p(x)
    # ---------------------------------------------------------
    ax2.set_title("2. Existence Thickness $p(x)$", fontsize=14, fontweight='bold')
    ax2.set_xlabel("Position $x$", fontsize=12)
    ax2.set_ylabel("Thickness $p(x)$", fontsize=12)
    ax2.set_xlim(-6, 6)
    ax2.set_ylim(0, 1.5)
    ax2.grid(True, alpha=0.2)
    
    line_p, = ax2.plot([], [], color='#4da6ff', linewidth=3)
    
    text_state = ax2.text(-5.5, 1.35, "", fontsize=14, fontweight='bold', color='white', 
                          bbox=dict(facecolor='black', alpha=0.7, edgecolor='white'))
    text_desc = ax2.text(-5.5, 1.20, "", fontsize=12, color='#dddddd')
    text_data = ax2.text(2.0, 1.25, "", fontsize=11, color='#ffcc00', bbox=dict(facecolor='black', alpha=0.5))

    # Global tracking state
    # Tracks the strict physical irreversibility of TSH phase transitions
    state = {'mouse_g': 1.5, 'mouse_df': 5.0, 'locked_core': False, 'locked_composite': False}

    # ---------------------------------------------------------
    # Master Update Function
    # ---------------------------------------------------------
    def update(val=None):
        mass = slider_mass.val
        mouse_g = state['mouse_g']
        mouse_df = state['mouse_df']
        
        # Recalculate 2D deformed boundaries, scaled by mass
        df_c1_vals, df_c2_vals = get_ultimate_boundaries(g_vals, mouse_g, mouse_df, mass)
        
        # Get local thresholds EXACTLY under the mouse
        local_c1, local_c2 = get_ultimate_boundaries(np.array([mouse_g]), mouse_g, mouse_df, mass)
        local_c1, local_c2 = local_c1[0], local_c2[0]
        
        # --- TSH Phase Irreversibility Logic ---
        # TSH Theory: Transitions to Composite and Core are one-way (decoherence/collapse).
        if mouse_df >= local_c2:
            state['locked_core'] = True
            state['locked_composite'] = True
        elif mouse_df >= local_c1:
            state['locked_composite'] = True
            
        if state['locked_core']:
            # Core (gravitational/measurement) is a terminal state; it cannot return below c2.
            mouse_df = max(mouse_df, local_c2)
            state['mouse_df'] = mouse_df
            reset_text.set_text("LOCKED IN Core (gravitational/measurement) (Terminal State)\nPress SPACEBAR to Reset")
        elif state['locked_composite']:
            # Composite に入った後は c1 より下に戻れないだけでよい
            mouse_df = max(mouse_df, local_c1)
            state['mouse_df'] = mouse_df
            reset_text.set_text("LOCKED IN COMPOSITE (Irreversible Decoherence)\nPress SPACEBAR to Reset")
        else:
            reset_text.set_text("")
            
        # Regenerate wave
        x, p, S1, S2, color, name, desc = generate_wave(mouse_df, local_c1, local_c2, mass)
        
        # --- Apply Visuals to Ax1 ---
        line_c1.set_ydata(df_c1_vals)
        line_c2.set_ydata(df_c2_vals)
        
        for coll in list(ax1.collections):
            coll.remove()
            
        ax1.fill_between(g_vals, df_c2_vals, 15.0, color='#ff4d4d', alpha=0.2)
        ax1.fill_between(g_vals, df_c1_vals, df_c2_vals, color='#4dff4d', alpha=0.2)
        ax1.fill_between(g_vals, 0, df_c1_vals, color='#4da6ff', alpha=0.2)
        
        dot.set_data([mouse_g], [mouse_df])
        dot.set_markerfacecolor(color)
        
        # --- Apply Visuals to Ax2 ---
        line_p.set_data(x, p)
        line_p.set_color(color)
        
        text_state.set_text(name)
        text_desc.set_text(desc)
        text_data.set_text(f"System State:\n$\gamma_T$ = {mouse_g:.2f}\n$\Delta f$ = {mouse_df:.2f}\nMass $m$ = {mass:.2f}")
        
        fig.canvas.draw_idle()

    # Bind events
    slider_mass.on_changed(update)
    
    def on_mouse_move(event):
        # Ignore mouse movements if we are locked in the terminal Core (gravitational/measurement)
        if event.inaxes == ax1 and not state['locked_core']:
            state['mouse_g'] = event.xdata
            state['mouse_df'] = event.ydata
            update()

    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
    
    def on_key(event):
        # UI rescue mechanism: Spacebar resets the simulation
        if event.key == ' ':
            state['mouse_g'] = 1.5
            state['mouse_df'] = 1.0  # Reset to a safe Stable state
            state['locked_core'] = False
            state['locked_composite'] = False
            update()
            
    fig.canvas.mpl_connect('key_press_event', on_key)
    
    # Initial draw
    update()
    
    plt.show()

if __name__ == "__main__":
    main()
