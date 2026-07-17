import pandas as pd
import matplotlib.pyplot as plt


def load_solar_data(csv_path, panel_area, efficiency, performance_ratio):
    """Load a NASA POWER daily CSV and calculate daily energy output."""
    df = pd.read_csv(csv_path, skiprows=9)
    df['energy_kwh'] = df['ALLSKY_SFC_SW_DWN'] * panel_area * efficiency * performance_ratio
    return df


def calculate_stats(df, electricity_price, number_of_panels, system_cost):
    """Calculate all summary stats for a loaded dataset."""
    total_annual_kwh = df['energy_kwh'].sum()
    winter = df[df['MO'].isin([6, 7, 8])]
    summer = df[df['MO'].isin([12, 1, 2])]
    annual_savings = total_annual_kwh * electricity_price
    system_annual_kwh = total_annual_kwh * number_of_panels
    system_annual_savings = system_annual_kwh * electricity_price
    payback_years = system_cost / system_annual_savings

    return {
        'total_annual_kwh': total_annual_kwh,
        'winter_avg_kwh': winter['energy_kwh'].mean(),
        'summer_avg_kwh': summer['energy_kwh'].mean(),
        'annual_savings': annual_savings,
        'system_annual_kwh': system_annual_kwh,
        'system_annual_savings': system_annual_savings,
        'payback_years': payback_years,
    }


def plot_daily_output(df, label, title=None):
    """Plot a single location's daily output for the year."""
    plt.figure(figsize=(12, 5))
    plt.plot(df['energy_kwh'], label=label)
    plt.title(title or f'{label} Daily Solar Output')
    plt.xlabel('Day of Year')
    plt.ylabel('Energy (kWh)')
    plt.legend()
    plt.show()


def compare_locations(name_a, stats_a, name_b, stats_b):
    """Build a full comparison table covering every calculated stat."""
    return pd.DataFrame({
        'Metric': [
            'Total Annual Energy - Single Panel (kWh)',
            'Winter Avg Daily Output (kWh)',
            'Summer Avg Daily Output (kWh)',
            'Annual Savings - Single Panel ($)',
            'System Annual Output (kWh)',
            'System Annual Savings ($)',
            'Payback Period (Years)',
        ],
        name_a: [stats_a['total_annual_kwh'], stats_a['winter_avg_kwh'], stats_a['summer_avg_kwh'],
                 stats_a['annual_savings'], stats_a['system_annual_kwh'],
                 stats_a['system_annual_savings'], stats_a['payback_years']],
        name_b: [stats_b['total_annual_kwh'], stats_b['winter_avg_kwh'], stats_b['summer_avg_kwh'],
                 stats_b['annual_savings'], stats_b['system_annual_kwh'],
                 stats_b['system_annual_savings'], stats_b['payback_years']],
    })


def plot_comparison(df_a, name_a, df_b, name_b):
    """Plot two locations' daily output on the same chart."""
    plt.figure(figsize=(12, 5))
    plt.plot(df_a['energy_kwh'], label=name_a)
    plt.plot(df_b['energy_kwh'], label=name_b)
    plt.title(f'Daily Solar Output: {name_a} vs {name_b}')
    plt.xlabel('Day of Year')
    plt.ylabel('Energy (kWh)')
    plt.legend()
    plt.show()