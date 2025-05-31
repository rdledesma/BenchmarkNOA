

import matplotlib.pyplot as plt

# Datos del MBE(%)
mbe_data = {
    'YU': {
        'W/O Adapt.': [0, 7.3, 0.7, 24.7],
        'Approach 1': [-0.6, -5.4, 2.4, -3],
        'Approach 2': [-0.6, -0.5, -1.1, -0.4],
        'Approach 3': [-1.5, -5.5, 0.2, -5],
    },
    'SA': {
        'W/O Adapt.': [3.6, 16.1, 7.9, 44.6],
        'Approach 1': [-0.9, -1.4, 0.8, 3.7],
        'Approach 2': [-0.9, -0.9, -1.1, -1.7],
        'Approach 3': [-1.6, -2.4, 1.0, 3.2],
    },
    'SCA': {
        'W/O Adapt.': [3.6, 16.4, 4.4, 10.5],
        'Approach 1': [0.1, 5.2, -4.3, -2.8],
        'Approach 2': [0.1, -1.4, 1.3, 1.0],
        'Approach 3': [7.6, 9.8, 4.6, 5.1],
    },
    'ERO': {
        'W/O Adapt.': [-20.2, -5.1, -12.2, -1.5],
        'Approach 1': [8.4, 5.5, 5.1, 3.2],
        'Approach 2': [8.4, 9.2, 9.2, 9],
        'Approach 3': [6.2, 5.4, 5.3, 4.2],
    },
    'LQ': {
        'W/O Adapt.': [-6, 3.4, -3.1, 0.2],
        'Approach 1': [2.1, -0.6, 1, 0.5],
        'Approach 2': [2.1, 2.6, 2.4, 2.4],
        'Approach 3': [0.5, -0.9, -0.1, -0.6],
    },
}

regions = list(mbe_data.keys())
models = ['CAMS', 'LSA-SAF', 'ERA-5', 'MERRA-2']
approaches = ['W/O Adapt.', 'Approach 1', 'Approach 2', 'Approach 3']

# Plot
fig, axes = plt.subplots(1, len(regions), figsize=(20, 6), sharey=True)
for idx, region in enumerate(regions):
    ax = axes[idx]
    for model_idx, model in enumerate(models):
        mbe_values = [mbe_data[region][approach][model_idx] for approach in approaches]
        ax.plot(approaches, mbe_values, marker='o', label=model)
    ax.set_title(region, fontsize=18)
    #ax.set_xlabel('Approach', fontsize=12)
    ax.grid(True)
    if idx == 0:
        ax.set_ylabel('MBE (%)', fontsize=18)
    ax.set_xticklabels(approaches, rotation=45, fontsize=14)
    ax.tick_params(axis='y', labelsize=12)

# Leyenda y ajustes
fig.legend(models, loc='upper center', ncol=len(models), fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()
