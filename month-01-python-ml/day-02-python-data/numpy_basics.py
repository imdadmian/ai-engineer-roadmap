import numpy as np
temperature_list=[72, 95, 81, 67, 89]
temperature_array=np.array(temperature_list)
print(temperature_list)
print(temperature_array)
print(type(temperature_list))
print(type(temperature_array))
print("Python list multiplied by 2:")
print(temperature_list * 2)

print("NumPy array multiplied by 2:")
print(temperature_array * 2)

print("Mean",np.mean(temperature_array))
print("Median",np.median(temperature_array))
print("minimum",np.min(temperature_array))
print("maximum",np.max(temperature_array))
print("sum",np.sum(temperature_array))
print("standard deviation",np.std(temperature_array))
print(temperature_array>80)
print(temperature_array[temperature_array>80])
print(temperature_array[(temperature_array>=75) & (temperature_array<=90)])
sensor_array = np.array([
    [72, 2.1, 1450],
    [95, 6.8, 1520],
    [81, 3.5, 1480]
])

print(sensor_array)
print(sensor_array.shape)
print(sensor_array[1, :])
print(sensor_array[0, :])
print(sensor_array[:, 2])
print("--------------------------------------------")

temperatures = sensor_array[:, 0]
print(np.mean(temperatures))
print(np.mean(sensor_array, axis=0))
print("Column averages:", np.mean(sensor_array, axis=0))
print("Highest temperature",np.max(sensor_array[:,0]))
print("Highest vibration",np.max(sensor_array[:,1]))
print("Highest RPM",np.max(sensor_array[:,2]))
print(sensor_array.dtype)