print("VARIABLES IN PYTHON")
name = "imdad"
age = 30
salary = 15000.00
is_active = True

print(name)
print(age)
print(salary)
print(is_active)

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))
print("VARIABLES CONVERSION IN PYTHON")
employees="150"
print(employees)
print(type(employees))
employees_int=int(employees)
print(employees_int)
print(type(employees_int))
new_total=employees_int+10
print(new_total)

price="125.75"
quantity="4"

price_float=float(price)
quantity_int=int(quantity)
total=price_float*quantity_int
print(total)
print(type(total))

print("String and fString in python")
model="Random Forest"
accuracy=0.91234

print(f"Model: {model}")
print(f"Accuracy :{accuracy}")
print(f"Accuracy :{accuracy:.2%}")
print(f"MyName is : {name}")

print(f"i purchased {quantity} items at {price} SAR each. total cost: {total:.2f} SAR")

print("Lists in python")

tempratures=[65.2,67.5,71.3,69.8]
print(tempratures)
print(type(tempratures))
print(tempratures[0])
print(tempratures[1])
print(tempratures[-1])

tempratures.append(74.1)
print(len(tempratures))
ave_tem=sum(tempratures)/len(tempratures)
print(ave_tem)
print(f"Average temprature is : {ave_tem:.2f} F")

print("Dictionaries in python-------------------------------------")

machine={"Id":"M001","temprature":78.5,"vibration":4.2,"status":"Running"}
print(machine)
print(type(machine))
print(machine["Id"])
print(machine["temprature"])
print(machine["status"])
machine["risk"] = "High"
print(machine)
print("List of Dictionaries in python-------------------------------------")
machines=[{"id":"M001","temperature":78.5},
{"id":"M002","temperature":91},
{"id":"M003","temperature":68}]
print(machines[0])
print(machines[1]["id"])
print(machines[2]["temperature"])
print(machines[-1]["id"])
print("For loop in python-------------------------------------")
for machine in machines:
    print(machine["id"])

for machine in machines:
    if machine['temperature']>=90:
        print(f"{machine['id']}: Critical")
    elif machine['temperature']>=75:
        print(f"{machine['id']}: Warning")
    else:
        print(f"{machine['id']}: Normal")

    print(f"Machine {machine['id']} has temperature of {machine['temperature']} F")
print("Functions in python-------------------------------------")

def calculate_average(values):
    return sum(values)/len(values)

readings=[20,25,30,35]
result=calculate_average(readings)
print(result)

def classify_temperature(temperature):

    if temperature >= 90:
        return "Critical"

    elif temperature >= 75:
        return "Warning"

    else:
        return "Normal"
def classify_machine(machine):
    for machine in machines:
        status=classify_temperature(machine['temperature'])
        print(f"Machine {machine['id']} has temperature of {machine['temperature']} F and status is {status}")
sensor_data = [
    {"machine": "M001", "temperature": 72, "vibration": 2.1},
    {"machine": "M002", "temperature": 95, "vibration": 6.8},
    {"machine": "M003", "temperature": 81, "vibration": 3.5},
    {"machine": "M004", "temperature": 67, "vibration": 7.2},
    {"machine": "M005", "temperature": 89, "vibration": 5.1}
]
def calculate_risk(machine):
    score = 0

    if machine["temperature"] >= 90:
        score += 2
    elif machine["temperature"] >= 80:
        score += 1

    if machine["vibration"] >= 6:
        score += 2
    elif machine["vibration"] >= 4:
        score += 1

    if score >= 4:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    else:
        return "LOW"
total_temperature = 0
total_vibration = 0
for machine in sensor_data:
    risk = calculate_risk(machine)
    total_temperature+=machine['temperature']
    total_vibration+=machine['vibration']

    print(
        f"{machine['machine']} | "
        f"Temperature: {machine['temperature']} | "
        f"Vibration: {machine['vibration']} | "
        f"Risk: {risk}"
    )
total_machines = len(sensor_data)
print(f"Total Machines: {total_machines}")

average_temperature = total_temperature / total_machines
average_vibration = total_vibration / total_machines
print(f"Average Temperature: {average_temperature:.2f}")
print(f"Average Vibration: {average_vibration:.2f}")