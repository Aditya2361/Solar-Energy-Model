# Solar Energy Output Model

A Python tool that calculates how much electricity a solar panel system would generate at any location, based on real historical solar radiation data — no physical panel needed.

## What This Project Does

This tool takes real satellite-measured solar data for a location and calculates:
- Daily and annual energy output for a solar panel system
- Seasonal differences (summer vs winter output)
- Calculated dollar savings on electricity bills, based on historical output
- Payback period for an installed system
- Side-by-side comparisons between two different locations

## Key Terms Explained

- **Irradiance** — the amount of solar energy hitting one square metre of ground, measured in kWh/m²/day. This is the raw "fuel" a solar panel converts into electricity.
- **Efficiency** — the percentage of that solar energy a panel actually converts into usable electricity (modern panels: ~18–22%).
- **Performance Ratio** — a real-world derating factor accounting for losses from wiring, inverters, and dust (~0.75–0.8 is typical).
- **Payback Period** — how many years of electricity savings it takes to pay off the upfront cost of installing a system.

## Data Source

Solar irradiance data comes from **NASA POWER** (Prediction Of Worldwide Energy Resources), a free public dataset built from satellite observations — meaning it has coverage anywhere on Earth, not just near weather stations.

- Data Access Viewer: https://power.larc.nasa.gov/data-access-viewer/
- Parameter used: `ALLSKY_SFC_SW_DWN` (All Sky Surface Shortwave Downward Irradiance), daily resolution, kWh/m²/day

## Pros, Cons, and Limitations

**Pros:**
- Uses real, verifiable satellite data rather than assumptions
- Works for any location on Earth by coordinates
- Fully reusable — swap in your own CSV, panel specs, and pricing

**Cons / Limitations:**
- Assumes 100% self-consumption at full retail electricity rate — in reality, unused solar power exported to the grid earns a much lower feed-in tariff, so real payback periods are typically longer than this model estimates
- Does not account for panel degradation over time (real panels lose ~0.5%/year output)
- Does not model shading, roof angle/orientation, or temperature-based efficiency loss
- Uses a single flat efficiency and performance ratio rather than manufacturer-specific panel data
- Because of these simplifications, results here should be treated as a simplified educational calculation based on past data, not a substitute for a professional solar quote

## Files in This Repo

| File | Description |
|---|---|
| `solar_model.py` | Core reusable functions — load data, calculate stats, and generate plots for any location |
| `demo.ipynb` | Worked example comparing Sydney vs Alice Springs, using the functions above |
| `SydneyData.csv` | Sample NASA POWER daily irradiance data for Sydney, 2025 |
| `AliceSpringsData.csv` | Sample NASA POWER daily irradiance data for Alice Springs, 2025 |

## How to Use It

1. Download your own location's daily irradiance data from [NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/) (Single Point → Renewable Energy community → Daily → parameter: All Sky Surface Shortwave Downward Irradiance → CSV)
2. Open `demo.ipynb` in Google Colab or Jupyter
3. Upload your CSV file(s) alongside the notebook
4. Edit the settings section with your own panel specs, electricity price, and system details:

```python
panel_area = 1.7            # m² per panel
efficiency = 0.20           # panel efficiency (decimal)
performance_ratio = 0.78    # real-world system losses
electricity_price = 0.315   # $ per kWh
number_of_panels = 16       # panels in a full system
system_cost = 5500          # installed system cost ($)
```

5. Update the filenames to match your uploaded CSVs, then run all cells
6. Use `compare_locations()` and `plot_comparison()` to compare any two locations' results side by side
