# 📡 Site Adaptation of Satellite-Derived and Reanalysis-Based Global Horizontal Irradiance Estimates in Northwestern Argentina

## Overview

This repository contains Python scripts developed for the adaptation and evaluation of global horizontal irradiance (GHI) estimates from multiple satellite and reanalysis sources using measured ground data. The methodology implements several linear regression approaches to reduce bias and improve accuracy in solar irradiance forecasting.

The work includes the preprocessing of satellite-derived and reanalysis-based GHI datasets, adaptation through statistical modeling, and performance evaluation via multiple metrics. This process supports enhanced solar resource assessment across five distinct regions in South America.

## 🧠 Methodology

### Data Sources

* **Measured GHI**: Hourly GHI data collected from ground stations in regions: YU, SA, SCA, ERO, and LQ.
* **Satellite Estimates**:

  * LSA-SAF (Land Surface Analysis Satellite Application Facility)
  * CAMS (Copernicus Atmosphere Monitoring Service)
* **Reanalysis Data**:

  * ERA5
  * MERRA-2

### Models and Adaptation

Linear regression models are trained using different configurations:

* **Approach 1**: Regression from satellite GHI to measured GHI.
* **Approach 2**: Predicting residuals between satellite and measured GHI.
* **Approach 3**: Residual-based regression anchored to clear-sky GHI baseline.

Scripts implement these models and generate adapted GHI estimates (`FitSLR.py`), which are subsequently evaluated using metrics defined in `Metrics.py`.

### Evaluation Metrics

Defined in `Metrics.py`, including:

* **Relative Mean Bias Error (rMBE)**
* **Relative Mean Absolute Error (rMAE)**
* **Relative Root Mean Square Deviation (rRMSD)**
* **Kolmogorov–Smirnov Integral (KSI)**
* **Skill Score (SS4)**

## 📁 Project Structure

```bash
.
├── FitSLR.py               # Trains and applies linear regression models for GHI adaptation
├── Metrics.py              # Statistical and skill score evaluation metrics
├── mergeLSA-SAF.py         # Preprocessing of LSA-SAF GHI data
├── mergeMERRA.py           # Preprocessing of MERRA-2 GHI data
├── Plotes.py               # Comparative visualizations of model performance
├── validateModels-*.py     # Data preparation per region (e.g., validateModels-yu.py for YU region)
└── Procesed/               # Contains preprocessed train/val/test datasets
```

## 🔍 How to Use

1. **Prepare Data**: Use `validateModels-*.py` scripts to align and format raw datasets.
2. **Merge External Sources**: Preprocess LSA-SAF and MERRA using `mergeLSA-SAF.py` and `mergeMERRA.py`.
3. **Train & Adapt**: Run `FitSLR.py` to train regression models and produce adapted GHI.
4. **Evaluate**: Statistical results are printed to console and can be visualized with `Plotes.py`.

## 📊 Results

Results show significant reduction in bias and RMSE across regions using adaptation approaches. `Plotes.py` generates region-specific plots comparing different adaptation strategies and models (CAMS, ERA5, MERRA, LSA-SAF).

## 🛠️ Requirements

* Python ≥ 3.7
* Libraries:

  * `pandas`
  * `numpy`
  * `matplotlib`
  * `scikit-learn`

## 📄 Citation

If you use this code in your research, please cite it as follows:

```
[1] Author(s), "Adaptive Correction of GHI Satellite Estimates using Linear Regression," *IEEE Xplore*, Year. [Online]. Available: <repository-url>
```

## 📬 Contact

For questions or collaboration inquiries, please contact:
**Author** – *Rubén D. Ledesma*
✉️ [email@example.com](mailto:rdledesma@exa.unsa.edu.ar)

