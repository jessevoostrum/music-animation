import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(-2, 2)

# Create the line object
line, = ax.plot([], [], 'b-', linewidth=2)

# Initialize function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(frame):
    x = np.arange(0, frame/10, 0.1)  # Gradually increase x range
    y = np.zeros_like(x)  # Create array of zeros for horizontal line
    line.set_data(x, y)
    return line,

# Create the animation
anim = FuncAnimation(fig, animate, init_func=init,
                    frames=1000, interval=10, blit=True)

# Save as GIF
anim.save('animation.gif', writer=PillowWriter(fps=100))

# Alternatively, save as MP4 (requires ffmpeg to be installed)
# anim.save('animation.mp4', writer=FFMpegWriter(fps=20))

# plt.show()
