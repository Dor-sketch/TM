import matplotlib.pyplot as plt
import numpy as np

# Define the figure and axis
fig, ax = plt.subplots()

# Define Turing machines and their behaviors
machines = ['M1', 'M2', 'D', 'D\'']
accepts = [True, False, True, False]  # hypothetical accept/reject behaviors

# Create a color map for accept/reject
colors = ['green' if accept else 'red' for accept in accepts]

# Plotting the Turing machines
y_positions = np.arange(len(machines))
ax.barh(y_positions, [1]*len(machines), color=colors, alpha=0.6)

# Annotate the bars with the accept/reject status
for i, (machine, accept) in enumerate(zip(machines, accepts)):
    ax.text(0.5, i, f"Accepts: {accept}", ha='center', va='center', color='white', weight='bold')

# Highlight the diagonal contradiction for D'
ax.plot([-0.2, 1.2], [2.8, 2.8], color='blue', linestyle='--', linewidth=2, label='D\' input/output')
ax.plot([0.5, 0.5], [1.8, 3.2], color='blue', linestyle='--', linewidth=2)

# Setting labels and title
ax.set_yticks(y_positions)
ax.set_yticklabels(machines)
ax.set_xlabel('Decision by D (assumed decider of K)')
ax.set_title('Diagonalization Proof of Undecidability')

# Add legend and grid
ax.legend()
ax.grid(True)

# Show the plot
plt.show()
