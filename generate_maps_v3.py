#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# Create world map - cleaner design
fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.set_facecolor('#f5f5f5')

# Title
ax.text(7, 8.5, 'TSMC Global Fab Locations', ha='center', fontsize=18, fontweight='bold')
ax.text(7, 8.2, '台湾半导体制造公司全球工厂分布', ha='center', fontsize=12, color='#666')

# Simple continent boxes (stylized)
# North America
ax.add_patch(FancyBboxPatch((1, 5), 3, 2.5, boxstyle="round,pad=0.05", facecolor='#e8f5e9', edgecolor='#2E7D32', linewidth=1))
ax.text(2.5, 7, 'Americas', ha='center', fontsize=10, color='#2E7D32')

# Europe/Africa
ax.add_patch(FancyBboxPatch((5.5, 4.5), 3, 3, boxstyle="round,pad=0.05", facecolor='#e8f5e9', edgecolor='#2E7D32', linewidth=1))
ax.text(7, 7, 'Europe/Africa', ha='center', fontsize=10, color='#2E7D32')

# Asia/Australia
ax.add_patch(FancyBboxPatch((9, 4), 4.5, 4, boxstyle="round,pad=0.05", facecolor='#e8f5e9', edgecolor='#2E7D32', linewidth=1))
ax.text(11.25, 7.5, 'Asia/Australia', ha='center', fontsize=10, color='#2E7D32')

# TAIWAN - Main location (highlighted)
ax.add_patch(patches.Circle((11.5, 5.5), 0.4, facecolor='#ff1744', edgecolor='#b71c1c', linewidth=2))
ax.text(11.5, 5.1, 'TAIWAN', ha='center', fontsize=9, fontweight='bold', color='#b71c1c')
ax.text(11.5, 4.9, 'Main Fabs', ha='center', fontsize=7, color='#666')

# USA - Arizona
ax.add_patch(patches.Circle((2.5, 6), 0.35, facecolor='#2979ff', edgecolor='#0d47a1', linewidth=2))
ax.text(2.5, 6.5, 'USA - Arizona', ha='center', fontsize=8, fontweight='bold', color='#0d47a1')
ax.text(2.5, 6.35, 'Fab 21 (N5/N3)', ha='center', fontsize=7, color='#333')

# Japan - Kumamoto  
ax.add_patch(patches.Circle((10.5, 5.3), 0.3, facecolor='#2979ff', edgecolor='#0d47a1', linewidth=2))
ax.text(10.5, 5.7, 'Japan - Kumamoto', ha='center', fontsize=8, fontweight='bold', color='#0d47a1')
ax.text(10.5, 5.55, 'JASM (N28/N16)', ha='center', fontsize=7, color='#333')

# Germany - Dresden
ax.add_patch(patches.Circle((7, 6.2), 0.3, facecolor='#2979ff', edgecolor='#0d47a1', linewidth=2))
ax.text(7, 6.6, 'Germany - Dresden', ha='center', fontsize=8, fontweight='bold', color='#0d47a1')
ax.text(7, 6.45, 'ESMC (N28) Planned', ha='center', fontsize=7, color='#333')

# Legend
ax.add_patch(FancyBboxPatch((0.5, 0.3), 4, 1.8, boxstyle="round,pad=0.05", facecolor='white', edgecolor='#ccc', linewidth=1))
ax.add_patch(patches.Circle((1, 1.5), 0.15, facecolor='#ff1744', edgecolor='#b71c1c'))
ax.text(1.4, 1.55, 'Taiwan - Main Fabs', fontsize=8)
ax.add_patch(patches.Circle((1, 1.1), 0.15, facecolor='#2979ff', edgecolor='#0d47a1'))
ax.text(1.4, 1.15, 'Overseas Fabs', fontsize=8)

# Info box
ax.add_patch(FancyBboxPatch((5, 0.3), 8.5, 2.5, boxstyle="round,pad=0.05", facecolor='white', edgecolor='#ccc', linewidth=1))
ax.text(5.3, 2.5, 'Taiwan Fabs (制程节点):', fontsize=10, fontweight='bold')
ax.text(5.3, 2.15, '• Fab 18 (台南) - N3/N5/N7 ★ 3nm量产基地', fontsize=9)
ax.text(5.3, 1.85, '• Fab 14 (台南) - N16/N12 | Fab 15 (台中) - N28/N22 | Fab 16 (龙潭) - N16 | Fab 8 (新竹) - N7/N5', fontsize=8, color='#666')
ax.text(5.3, 1.4, 'Overseas: Fab 21 Arizona (N5/N3) | JASM Japan (N28/N16) | ESMC Germany (N28,规划)', fontsize=8, color='#666')

ax.axis('off')
plt.tight_layout()
plt.savefig('/Users/henryt/.openclaw/workspace/tsmc-world-map.png', dpi=150, bbox_inches='tight', facecolor='white')
print("World map saved!")

# Create Taiwan map
fig2, ax2 = plt.subplots(figsize=(10, 12))
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 12)
ax2.set_facecolor('#f5f5f5')

# Title
ax2.text(5, 11.5, 'TSMC Taiwan Fab Locations', ha='center', fontsize=18, fontweight='bold')
ax2.text(5, 11.1, '台湾制程工厂分布', ha='center', fontsize=12, color='#666')

# Taiwan shape (simplified)
taiwan = patches.Polygon([
    (4.5, 10), (5, 9), (5.2, 8), (5, 7), (4.8, 6), (4.5, 5),
    (4.2, 4), (3.8, 3), (3.5, 2.5), (3.8, 2), (4.2, 1.5),
    (4.5, 1), (5, 0.8), (5.5, 1), (6, 1.5), (6.2, 2.5),
    (6, 3.5), (5.5, 5), (5.2, 7), (5, 8), (4.8, 9), (4.5, 10)
], closed=True, facecolor='#e8f5e9', edgecolor='#2E7D32', linewidth=2)
ax2.add_patch(taiwan)

# Hsinchu - Fab 8
ax2.add_patch(patches.Circle((4.8, 8.5), 0.35, facecolor='#ff1744', edgecolor='#b71c1c', linewidth=2))
ax2.text(4.8, 9.0, 'Fab 8', ha='center', fontsize=9, fontweight='bold', color='#b71c1c')
ax2.text(4.8, 8.7, 'N7/N5', ha='center', fontsize=7)
ax2.text(4.8, 9.3, 'Hsinchu', ha='center', fontsize=8, fontweight='bold')

# Taichung - Fab 15
ax2.add_patch(patches.Circle((4.6, 5.8), 0.3, facecolor='#ff6b6b', edgecolor='#b71c1c', linewidth=2))
ax2.text(4.6, 6.2, 'Fab 15', ha='center', fontsize=8, fontweight='bold')
ax2.text(4.6, 6.0, 'N28/N22', ha='center', fontsize=6)
ax2.text(4.6, 5.4, 'Taichung', ha='center', fontsize=8, fontweight='bold')

# Longtan - Fab 16
ax2.add_patch(patches.Circle((5.3, 8.2), 0.25, facecolor='#ff6b6b', edgecolor='#b71c1c', linewidth=2))
ax2.text(5.3, 8.5, 'Fab 16', ha='center', fontsize=7, fontweight='bold')
ax2.text(5.3, 8.35, 'N16', ha='center', fontsize=6)
ax2.text(5.3, 7.9, 'Longtan', ha='center', fontsize=7)

# Tainan - Fab 18 (3nm) - STAR
ax2.add_patch(patches.Circle((4.5, 2.5), 0.5, facecolor='#ff0000', edgecolor='#990000', linewidth=3))
ax2.text(4.5, 3.2, '★ Fab 18', ha='center', fontsize=10, fontweight='bold', color='#990000')
ax2.text(4.5, 2.9, 'N3/N5/N7', ha='center', fontsize=8, fontweight='bold')
ax2.text(4.5, 2.0, 'Tainan (3nm Base)', ha='center', fontsize=9, fontweight='bold', color='#990000')

# Tainan - Fab 14
ax2.add_patch(patches.Circle((5.0, 3.0), 0.2, facecolor='#ff6b6b', edgecolor='#b71c1c', linewidth=2))
ax2.text(5.0, 3.3, 'Fab 14', ha='center', fontsize=7, fontweight='bold')
ax2.text(5.0, 3.15, 'N16/N12', ha='center', fontsize=6)

# Legend / Info
ax2.add_patch(FancyBboxPatch((6.5, 8), 3.2, 3.5, boxstyle="round,pad=0.05", facecolor='white', edgecolor='#ccc', linewidth=1))
ax2.text(6.7, 11.2, 'Process Nodes:', ha='left', fontsize=10, fontweight='bold')
ax2.add_patch(patches.Circle((7, 10.5), 0.15, facecolor='#ff0000'))
ax2.text(7.3, 10.55, 'N3 (3nm) - Most Advanced', ha='left', fontsize=8)
ax2.add_patch(patches.Circle((7, 9.8), 0.15, facecolor='#ff6b6b'))
ax2.text(7.3, 9.85, 'N5/N7 (5nm/7nm)', ha='left', fontsize=8)
ax2.add_patch(patches.Circle((7, 9.1), 0.15, facecolor='#ffaaaa'))
ax2.text(7.3, 9.15, 'N16/N12 (16nm/12nm)', ha='left', fontsize=8)
ax2.add_patch(patches.Circle((7, 8.4), 0.15, facecolor='#ffcccc'))
ax2.text(7.3, 8.45, 'N22/N28 (22nm/28nm)', ha='left', fontsize=8)

ax2.text(0.5, 1.5, 'Key: ★ = 3nm Production Base', ha='left', fontsize=9, style='italic', color='#990000')

ax2.axis('off')
plt.tight_layout()
plt.savefig('/Users/henryt/.openclaw/workspace/tsmc-taiwan-map.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Taiwan map saved!")

print("\n✓ Maps generated successfully!")
