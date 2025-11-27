import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig, ax = plt.subplots(figsize=(6,8))
blocks = [
("Input Vector (Q, K, V)", 0.88),
("Multi-Head Attention", 0.72),
("Add & Norm", 0.56),
("Feed Forward", 0.40),
("Add & Norm", 0.24),
("Block Output", 0.08)

]
# Draw blocks
for text, y in blocks:
ax.add_patch(patches.Rectangle((0.25, y), 0.5, 0.1, fill=False, linewidth=2))
ax.text(0.5, y+0.05, text, ha='center', va='center', fontsize=11)
# Vertical arrows
for i in range(len(blocks)-1):
_, y1 = blocks[i]
_, y2 = blocks[i+1]
ax.annotate("", xy=(0.5, y2+0.1), xytext=(0.5, y1),
arrowprops=dict(arrowstyle="->", linewidth=1.8))

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
plt.title("Transformer Block", fontsize=14, fontweight='bold')
plt.show()
