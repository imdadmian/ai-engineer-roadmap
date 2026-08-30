import pandas as pd
data = {
    "Machine": ["M001", "M002", "M003", "M004", "M005"],
    "Temperature": [72, 95, None, 67, 89],
    "Vibration": [2.1, 6.8, 3.5, None, 5.1],
    "RPM": [1450, 1520, 1480, 1430, None]
}
print(type(data))
df=pd.DataFrame(data)
print(df)
print(df["Temperature"])
print(type(df))
print(type(df["Temperature"]))
print(df["Temperature"].mean())
print(df["Temperature"].min())
print(df["Temperature"].max())
print(df["Vibration"].mean())
print(df["RPM"].max())
print(df["Temperature"].min())
print("<------------------Filtering a DataFrame---------------------->")
df["Temperature"] > 80
high_temp = df[df["Temperature"] > 80]
print(high_temp)
vibrati=df[df["Vibration"] > 5]
print(vibrati)
filtered=df[(df["Temperature"] >= 80) & (df["Vibration"] >= 5)]
print(filtered)
result = df.loc[
    (df["Temperature"] >= 80) & (df["Vibration"] >= 5),
    ["Machine", "Temperature"]
]

print(result)   
result = df.loc[df["RPM"] >= 1480, ["Machine", "RPM"]]
print(result)
print("<------------------Creating a new column---------------------->")
df["Temperature_Critical"] = df["Temperature"] >= 90
df["High_Vibration"]=df["Vibration"]>=6
print(df)
def classify_temperature(temp):
    if temp>=90:
        return "Critical"
    elif temp>=80:
        return "Warning"
    else:
        return "Normal"
df["Status"]=df["Temperature"].apply(classify_temperature)
print(df)
print(df.isnull())
print(df.isnull().sum())
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())

df["Vibration"] = df["Vibration"].fillna(df["Vibration"].mean())

print(df)
df["RPM"] = df["RPM"].fillna(df["RPM"].median())
print(df.isnull().sum())
sorted_df_temp=df.sort_values(by="Temperature",ascending=False)
print(sorted_df_temp)
sorted_df_vib=df.sort_values(by="Vibration",ascending=True).reset_index(drop=True)
print(sorted_df_vib)    
df["Area"] = ["Filling", "Packing", "Filling", "Packing", "Filling"]  
print(df)
area_avg_temp=df.groupby("Area")["Temperature"].mean()
print(area_avg_temp)
area_max = df.groupby("Area")[["Temperature","RPM"]].max()
print(area_max)
print(df.describe())
print(df.info())
df.info()
print(df.shape[1])
print(df.head(2))
print(df.tail(2))
print (df)
df.to_csv("machine_data.csv",index=False)
loaded_df=pd.read_csv("machine_data.csv")
print(loaded_df.head())
print(loaded_df["Status"].value_counts())

