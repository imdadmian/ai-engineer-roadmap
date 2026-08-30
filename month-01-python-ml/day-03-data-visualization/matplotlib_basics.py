import matplotlib.pyplot as plt
# %% Bar Chart
machines = ["M001", "M002", "M003", "M004", "M005"]
temperatures = [72, 95, 81, 67, 89]

plt.bar(machines, temperatures)
plt.title("Machine Temperatures")
plt.xlabel("Machines")
plt.ylabel("Temperature (°C)")
plt.savefig("machine_temperatures.png")

plt.show()


# %% Line Chart
hours = [8, 9, 10, 11, 12, 13]
temperature = [65, 68, 72, 78, 85, 93]

plt.plot(hours, temperature)
plt.xlabel("Hours")
plt.ylabel("Temperature (°C)")
plt.title("M001 Temperature Trend")
plt.savefig("m001_temperature_trend.png")
plt.show()


# %% Histogram
temperatures = [
    68, 70, 71, 72, 72,
    73, 74, 75, 76, 77,
    78, 79, 80, 81, 82,
    84, 86, 89, 92, 96,120
]

plt.hist(temperatures, bins=10, edgecolor='black')
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.savefig("temperature_distribution.png")
plt.show()

# %% Box Plot
plt.boxplot(temperatures)
plt.title("Temperature Box Plot")
plt.ylabel("Temperature (°C)")
plt.savefig("temperature_box_plot.png")
plt.show()

#%% Multiple Line Chart
hours = [8, 9, 10, 11, 12, 13]

m001_temp = [65, 68, 72, 78, 85, 93]
m002_temp = [66, 67, 69, 70, 72, 73]
plt.plot(hours, m001_temp, label="M001")
plt.plot(hours, m002_temp, label="M002")

plt.xlabel("Hour")
plt.ylabel("Temperature (°C)")
plt.title("Machine Temperature Comparison")
plt.axhline(y=85, label="Warning Threshold", color='r', linestyle='--')
plt.legend()
plt.grid()
plt.savefig("machine_temperature_comparison.png")
plt.show()

#%% Line Chart with Threshold for vibration 
hours = [8, 9, 10, 11, 12, 13]
vibration = [2.1, 2.4, 2.8, 3.6, 4.9, 6.7]
plt.plot(hours, vibration, label="M001 Vibration")
plt.xlabel("Hour")
plt.ylabel("Vibration (mm/s)")
plt.title("M001 Vibration Trend")
plt.axhline(y=5, label="Warning Threshold", color='r', linestyle='--')
plt.legend()
plt.grid()
plt.savefig("m001_vibration_trend.png")
plt.show()
