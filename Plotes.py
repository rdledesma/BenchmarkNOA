

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
    ax.set_xticklabels(approaches, rotation=45, fontsize=15)
    ax.tick_params(axis='y', labelsize=15)

# Leyenda y ajustes
fig.legend(models, loc='upper center', ncol=len(models), fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

# Datos organizados por región, modelo y enfoque
regions = ['YU', 'SA', 'SCA', 'ERO', 'LQ']
models = ['CAMS', 'LSA-SAF', 'ERA-5', 'MERRA-2']
approaches = ['No Adapt.', 'Approach 1', 'Approach 2', 'Approach 3']

# RMSE (%) para cada modelo, región y enfoque
rmse_data = {
    'CAMS': [
        [25.1, 29.6, 31.8, 37.2, 21.6],
        [24.2, 27.3, 26.9, 30.0, 19.4],
        [24.2, 27.3, 26.9, 30.0, 19.4],
        [25.1, 29.2, 29.8, 21.3, 16.2]
    ],
    'LSA-SAF': [
        [24.7, 34.2, 34.4, 23.8, 17.8],
        [24.1, 29.8, 28.5, 23.7, 17.4],
        [24.7, 27.6, 27.7, 32.4, 20.3],
        [24.0, 30.2, 30.8, 20.4, 16.9]
    ],
    'ERA-5': [
        [34.5, 49.5, 34.6, 26.6, 19.5],
        [34.5, 46.6, 32.9, 24.2, 19.3],
        [25.0, 28.5, 29.6, 35.5, 20.7],
        [33.2, 44.0, 31.2, 21.3, 17.0]
    ],
    'MERRA-2': [
        [52.4, 65.3, 34.1, 21.9, 20.1],
        [45.1, 45.1, 31.1, 21.9, 19.9],
        [24.0, 28.1, 29.6, 32.7, 20.6],
        [45.3, 47.6, 32.0, 20.5, 17.9]
    ]
}

# Colores por modelo
colors = {
    'CAMS': 'royalblue',
    'LSA-SAF': 'darkorange',
    'ERA-5': 'forestgreen',
    'MERRA-2': 'firebrick'
}

# Crear subplots
fig, axs = plt.subplots(1, 4, figsize=(20, 6), sharey=True)
fig.suptitle('RMSE (%) Comparison by Approach and Region', fontsize=16)

for i, approach in enumerate(approaches):
    ax = axs[i]
    for model in models:
        ax.plot(regions, rmse_data[model][i], marker='o', label=model, color=colors[model])
    ax.set_title(approach, fontsize=14)
    #ax.set_xlabel('Region', fontsize=12)
    if i == 0:
        ax.set_ylabel('RMSE (%)', fontsize=14)

    # 🔹 Incrementar tamaño de ticks
    ax.tick_params(axis='both', labelsize=14)

    ax.grid(True)
    if i == 3:
        ax.legend(loc='upper right', fontsize=11)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
