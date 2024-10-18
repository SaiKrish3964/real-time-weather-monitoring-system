import matplotlib.pyplot as plt

def plot_weather_summary(summary):
    summary.set_index('date', inplace=True)
    summary.groupby('city')['avg_temp'].plot(legend=True)
    plt.title('Average Daily Temperature by City')
    plt.ylabel('Temperature (°C)')
    plt.show()