#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import warnings
warnings.filterwarnings('ignore')

# Create world map
fig1, ax1 = plt.subplots(figsize=(14, 8))
ax1.set_xlim(-180, 180)
ax1.set_ylim(-60, 80)
ax1.set_facecolor('#E8F4F8')
ax1.set_aspect('equal')

# Simplified continents
ax1.add_patch(patches.Rectangle((-180, -60), 360, 140, facecolor='#C8E6C9', edgecolor='none'))

# Taiwan
taiwan_box = patches.Rectangle((120, 22), 3, 4, linewidth=2, edgecolor='#E53935', facecolor='#FFCDD2')
ax1.add_patch(taiwan_box)
ax1.text(121.5, 26, 'TAIWAN', ha='center', fontsize=12, fontweight='bold', color='#C62828')

# USA
ax1.text(-115, 40, 'USA\nFab 21 (N5/N3)\nFab 23 (N2)', ha='center', fontsize=9, color='#1565C0')
ax1.add_patch(patches.Circle((-115, 35), 3, facecolor='#BBDEFB', edgecolor='#1565C0'))

# Japan
ax1.text(130, 38, 'Japan\nJASM (N28/N16)', ha='center', fontsize=9, color='#1565C0')
ax1.add_patch(patches.Circle((130, 33), 3, facecolor='#BBDEFB', edgecolor='#1565C0'))

# Germany
ax1.text(10, 52, 'Germany\nESMC (N28)\nPlanned', ha='center', fontsize=9, color='#1565C0')
ax1.add_patch(patches.Circle((10, 47), 3, facecolor='#BBDEFB', edgecolor='#1565C0'))

ax1.set_title('TSMC Global Fab Locations', fontsize=16, fontweight='bold', pad=20)
ax1.axis('off')

legend_elements = [
    patches.Patch(facecolor='#FFCDD2', edgecolor='#E53935', label='Taiwan (Main Fabs)'),
    patches.Patch(facecolor='#BBDEFB', edgecolor='#1565C0', label='Overseas Fabs')
]
ax1.legend(handles=legend_elements, loc='lower left', fontsize=10)

plt.tight_layout()
plt.savefig('/Users/henryt/.openclaw/workspace/tsmc-world-map.png', dpi=150, bbox_inches='tight', facecolor='white')
print("World map saved!")

# Create Taiwan map
fig2, ax2 = plt.subplots(figsize=(10, 12))
ax2.set_xlim(120, 122)
ax2.set_ylim(22.5, 25.5)
ax2.set_facecolor('#E8F4F8')

# Taiwan outline (simplified)
taiwan_outline = patches.Polygon([
    (121.5, 25.3), (121.9, 24.8), (121.5, 24.2), 
    (121.0, 23.5), (120.3, 23.0), (120.2, 22.8),
    (120.3, 22.7), (120.8, 22.9), (121.2, 23.5),
    (121.6, 24.0), (121.9, 24.5), (121.7, 25.2)
], closed=True, facecolor='#C8E6C9', edgecolor='#2E7D32', linewidth=2)
ax2.add_patch(taiwan_outline)

# Hsinchu (Fab 8)
ax2.add_patch(patches.Circle((120.98, 24.80), 0.12, facecolor='#E53935', edgecolor='black', linewidth=1.5))
ax2.text(120.98, 24.55, 'Fab 8\nN7/N5', ha='center', fontsize=8, fontweight='bold')
ax2.text(120.98, 24.40, 'Hsinchu', ha='center', fontsize=7, color='#666')

# Taichung (Fab 15)
ax2.add_patch(patches.Circle((120.65, 24.20), 0.12, facecolor='#E53935', edgecolor='black', linewidth=1.5))
ax2.text(120.65, 23.95, 'Fab 15\nN28/N22', ha='center', fontsize=8, fontweight='bold')
ax2.text(120.65, 23.80, 'Taichung', ha='center', fontsize=7, color='#666')

# Taoyuan/Longtan (Fab 16)
ax2.add_patch(patches.Circle((121.22, 24.85), 0.12, facecolor='#E53935', edgecolor='black', linewidth=1.5))
ax2.text(121.22, 25.10, 'Fab 16\nN16', ha='center', fontsize=8, fontweight='bold')
ax2.text(121.22, 25.25, 'Longtan', ha='center', fontsize=7, color='#666')

# Tainan (Fab 14, 18)
ax2.add_patch(patches.Circle((120.28, 22.98), 0.15, facecolor='#D32F2F', edgecolor='black', linewidth=1.5))
ax2.text(120.28, 22.65, 'Fab 18 ★\nN3/N5/N7', ha='center', fontsize=8, fontweight='bold', color='#B71C1C')
ax2.text(120.28, 22.50, 'Tainan\n(3nm Base)', ha='center', fontsize=7, color='#666')

ax2.add_patch(patches.Circle((120.35, 23.10), 0.10, facecolor='#E53935', edgecolor='black', linewidth=1.5))
ax2.text(120.35, 23.25, 'Fab 14\nN16/N12', ha='center', fontsize=7, fontweight='bold')

ax2.set_title('TSMC Taiwan Fab Locations', fontsize=14, fontweight='bold', pad=15)
ax2.axis('off')

# Legend
info_text = """Process Nodes:
★ N3 (3nm) - Most Advanced
N5 (5nm)
N7 (7nm)
N16/N12 (16nm/12nm)
N22/N28 (22nm/28nm)"""
ax2.text(121.6, 23.5, info_text, fontsize=8, verticalalignment='center',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('/Users/henryt/.openclaw/workspace/tsmc-taiwan-map.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Taiwan map saved!")

print("\n✓ Maps generated!")
print("Files:")
print("  - /Users/henryt/.openclaw/workspace/tsmc-world-map.png")
print("  - /Users/henryt/.openclaw/workspace/tsmc-taiwan-map.png")
