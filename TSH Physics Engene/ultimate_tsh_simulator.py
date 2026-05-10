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
# structural phases, Hierarchical Interaction Slot, and O(N) computation model) is provided in
# TSH_SPEC.md. This implementation strictly follows that specification.

For full theoretical derivation and documentation, refer to the project 
README.md and the Zenodo DOI above.
================================================================================
"""
"""
================================================================================
TSH Physics Engine v1.0 (Official Release)
================================================================================

[Description]
The official version 1.0 of the TSH simulator, implementing the 
Grand Unified Universal OS specification.
Simulates Standard Model, Condensed Matter, and Dark Sector behaviors 
within a single existence thickness field p.

[v1.0 Features]
- Layer 1: Phase Map (Base Heatmap)
- Layer 2: Interaction Map (q1:Cyan, q2:Orange, q3:Pink, q4:White)
- Layer 3: Phase Boundaries (Contour lines)
- Fully Data-Driven Material Dictionary

(C) 2026 TSH Dynamics Research Group.
================================================================================
"""

import pygame
# NOTE:
# This collapse implementation is NOT an ODE/PDE-based model.
# DO NOT augment this logic with general physical paradigms.
# This is a unique model based on the Delta_f - gamma_T phase diagram and the TSH structural potential.
import numpy as np
import random
import math
import sys
from collections import defaultdict

# --- Configuration ---
WIDTH, HEIGHT = 1280, 800
FPS = 60
SUBSTEPS = 8
DT = 1.0 / (FPS * SUBSTEPS)
CELL_SIZE = 120

# --- v1.0 Material Presets ---
MATERIAL_TABLE = {
    "SM_Quark":  {"beta": [35.0, 180.0, 20.0, 0.0], "alpha": 13.5, "color": (255, 200, 50)},
    "SM_Lepton": {"beta": [40.0, 0.0, 15.0, 0.0],   "alpha": 12.8, "color": (100, 180, 255)},
    "DS_Dark":   {"beta": [0.0, 30.0, 0.0, 10.0],   "alpha": 8.0,  "color": (200, 100, 255)},
    "CM_Super":  {"beta": [40.0, 30.0, 0.0, 25.0],   "alpha": 10.5, "color": (255, 255, 255)}
}

class Particle:
    def __init__(self, x, y, mat_key, is_anti=False):
        self.pos = np.array([float(x), float(y)])
        self.vel = np.zeros(2)
        self.acc = np.zeros(2)
        self.is_anti = is_anti
        self.mat = MATERIAL_TABLE[mat_key]
        self.charges = np.array([1.0, 1.0, 0.5, 0.1]) * (-1.0 if is_anti else 1.0)
        self.mass = 1.0 + random.uniform(0.5, 2.0)
        self.sigma = 20.0
        self.p_amp = 1.0
        self.phase = "Stable"
        self.delta_f = 1.0  
        self.gamma_T = 0.0  
        self.tau = 0.0  # [NEW] Proper time
        self.effective_mass = self.mass
        self.structural_potential = 0.0
        self.energy = 0.0
        self.phase_distance = 0.0

    def update_phase(self, lp, grad_p, channel_p):
        # 1. Update Internal Variables (Irreversibility & Relativity)
        self.delta_f = np.linalg.norm(grad_p) / (lp + 1e-7)
        self.gamma_T = min(self.gamma_T + 0.01 * lp, 50.0)
        
        # Proper time: dt_tau = dt / gamma
        speed2 = np.dot(self.vel, self.vel) * 0.0001 # scaled for pygame space
        gamma = 1.0 / math.sqrt(max(0.01, 1.0 - min(0.99, speed2)))
        self.tau += DT / gamma

        # 2. Asymmetric Phase Transitions & Distance
        strong_th = self.mat['alpha'] * 1.5 + 0.2 * self.gamma_T
        core_th = self.mat['alpha'] * 3.0 + 0.5 * self.gamma_T
        self.phase_distance = (lp > strong_th) and (core_th - lp) or (strong_th - lp)
        
        old_phase = self.phase
        if lp > core_th: self.phase = "Core"
        elif lp > strong_th: self.phase = "Strong"
        elif lp > 5.0: self.phase = "Composite"
        else: self.phase = "Stable"

        if old_phase == "Core" and self.phase != "Core" and self.delta_f > 0.05:
            self.phase = "Core"

        # 3. Observables Computation
        self.effective_mass = self.mass + 0.1 * self.gamma_T + 0.05 / (self.delta_f + 0.01)
        self.structural_potential = self.mat['alpha'] * math.log(lp) + np.dot(self.mat['beta'], self.charges) * channel_p + self.gamma_T * 0.5
        self.energy = 0.5 * self.effective_mass * np.dot(self.vel, self.vel) + self.structural_potential

        # 4. Collapse logic
        if self.phase == "Core":
            self.p_amp += 0.5; self.delta_f *= 0.9; self.sigma = max(6.0, self.sigma * 0.99)
        elif self.phase == "Strong": self.p_amp = 20.0; self.sigma = 12.0
        elif self.phase == "Composite": self.p_amp = 10.0; self.sigma = 18.0
        else: self.p_amp = 2.0; self.sigma = 35.0

class TSHCore:
    def __init__(self):
        self.particles = []
        self.grid = {}

    def add_particle(self, x, y, mat="SM_Quark", anti=False):
        self.particles.append(Particle(x, y, mat, anti))

    def update(self):
        for _ in range(SUBSTEPS):
            self._update_grid()
            self._compute_forces()
            self._integrate()

    def _update_grid(self):
        self.grid = {}
        for i, p in enumerate(self.particles):
            cell = (int(p.pos[0] // CELL_SIZE), int(p.pos[1] // CELL_SIZE))
            if cell in self.grid: self.grid[cell].append(i)
            else: self.grid[cell] = [i]

    def _compute_forces(self):
        for p in self.particles:
            p_total, grad_total = 1e-7, np.zeros(2)
            grad_chan = [np.zeros(2) for _ in range(4)]
            channel_p = 0.0
            
            cx, cy = int(p.pos[0] // CELL_SIZE), int(p.pos[1] // CELL_SIZE)
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    cell = (cx+dx, cy+dy)
                    if cell in self.grid:
                        for idx in self.grid[cell]:
                            other = self.particles[idx]
                            diff = p.pos - other.pos; d2 = np.dot(diff, diff)
                            s2 = other.sigma**2
                            if d2 > s2 * 18.0: continue
                            val = other.p_amp * math.exp(-d2 / (2 * s2))
                            g = -(diff / s2) * val
                            p_total += val; grad_total += g
                            for k in range(4): grad_chan[k] += other.charges[k] * g
                            channel_p += np.dot(p.charges, other.charges) * val
            
            # Update Phase & Observables
            p.update_phase(p_total, grad_total, channel_p)

            f_struct = -p.mat['alpha'] * (grad_total / p_total)
            f_unified = f_struct
            for k in range(4):
                f_unified -= p.mat['beta'][k] * p.charges[k] * grad_chan[k]
            
            p.acc = (f_unified * p.effective_mass + np.array([0, 0.5])) / p.effective_mass

    def _integrate(self):
        for p in self.particles:
            p.vel += p.acc * DT
            
            # Relativistic Speed Limit (c=1 equivalent in simulation space)
            speed = np.linalg.norm(p.vel)
            if speed > 800.0: # Pygame screen units limit
                p.vel = (p.vel / speed) * 800.0
                
            p.pos += p.vel * DT
            p.pos[0] = np.clip(p.pos[0], 0, WIDTH)
            p.pos[1] = np.clip(p.pos[1], 0, HEIGHT)
            p.vel *= 0.99

class TSHRenderer:
    def __init__(self, screen):
        self.screen = screen
        self.grid_x, self.grid_y = np.meshgrid(np.linspace(0, WIDTH, 80), np.linspace(0, HEIGHT, 50))

    def draw(self, engine):
        self.screen.fill((5, 5, 10))
        base_img = np.zeros((50, 80, 3))
        chan_img = np.zeros((50, 80, 3))
        
        for p in engine.particles:
            d2 = (self.grid_x - p.pos[0])**2 + (self.grid_y - p.pos[1])**2
            mask = d2 < (p.sigma**2 * 12.0)
            val = p.p_amp * np.exp(-d2[mask] / (2 * p.sigma**2))
            
            if p.phase == "Stable": base_img[mask, 2] += val * 0.1
            elif p.phase == "Composite": base_img[mask, 1] += val * 0.1
            elif p.phase == "Strong": base_img[mask, 0] += val * 0.1; base_img[mask, 1] += val * 0.05
            elif p.phase == "Core": base_img[mask, 0] += val * 0.2
            
            chan_img[mask, 1] += p.charges[0] * val * 0.2; chan_img[mask, 2] += p.charges[0] * val * 0.2 # Cyan
            chan_img[mask, 0] += p.charges[1] * val * 0.2; chan_img[mask, 1] += p.charges[1] * val * 0.1 # Orange
            chan_img[mask, 0] += p.charges[2] * val * 0.2; chan_img[mask, 2] += p.charges[2] * val * 0.2 # Pink
            chan_img[mask, :] += p.charges[3] * val * 0.1 # White
            
        surf_base = pygame.transform.smoothscale(pygame.surfarray.make_surface(np.transpose(np.clip(base_img, 0, 255), (1, 0, 2))), (WIDTH, HEIGHT))
        surf_chan = pygame.transform.smoothscale(pygame.surfarray.make_surface(np.transpose(np.clip(chan_img, 0, 255), (1, 0, 2))), (WIDTH, HEIGHT))
        self.screen.blit(surf_base, (0, 0), special_flags=pygame.BLEND_ADD)
        self.screen.blit(surf_chan, (0, 0), special_flags=pygame.BLEND_ADD)

        for p in engine.particles:
            pygame.draw.circle(self.screen, p.mat['color'], p.pos.astype(int), 8)

def main():
    pygame.init(); screen = pygame.display.set_mode((WIDTH, HEIGHT)); clock = pygame.time.Clock()
    engine = TSHCore(); renderer = TSHRenderer(screen)
    for _ in range(12): engine.add_particle(random.randint(200, 1000), random.randint(100, 700), random.choice(list(MATERIAL_TABLE.keys())))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos(); engine.add_particle(pos[0], pos[1], "SM_Quark", random.random()<0.3)
        
        engine.update(); renderer.draw(engine)
        pygame.display.flip(); clock.tick(60)
    pygame.quit()

if __name__ == "__main__": main()
