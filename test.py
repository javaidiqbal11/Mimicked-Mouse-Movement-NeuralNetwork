import pandas as pd

print("Gan")
data = pd.read_csv("sample/gan.csv")
# convert back to milliseconds
# data["timestamp"] = data["timestamp"].apply(lambda x: int(x*1000))
etype = data["event_type"].astype(str).values.tolist()
timestamp = data["timestamp"].astype(str).values.tolist()
x = data["x"].astype(str).values.tolist()
y = data["y"].astype(str).values.tolist()

count = [str(i) for i in range(len(x))]

mact = ''
for i in range(len(x)):
    mact += count[i] + "," + etype[i] + "," + timestamp[i] + "," + x[i] + "," + y[i] + ";"
print(mact)

print("Gausian")
data = pd.read_csv("sample/gaussian.csv")
# convert back to milliseconds
# data["timestamp"] = data["timestamp"].apply(lambda x: int(x*1000))
etype = data["event_type"].astype(str).values.tolist()
timestamp = data["timestamp"].astype(str).values.tolist()
x = data["x"].astype(str).values.tolist()
y = data["y"].astype(str).values.tolist()

count = [str(i) for i in range(len(x))]

mact = ''
for i in range(len(x)):
    mact += count[i] + "," + etype[i] + "," + timestamp[i] + "," + x[i] + "," + y[i] + ";"
print(mact)

print("PAR")
data = pd.read_csv("sample/par.csv")
# convert back to milliseconds
# data["timestamp"] = data["timestamp"].apply(lambda x: int(x*1000))
etype = data["event_type"].astype(str).values.tolist()
timestamp = data["timestamp"].astype(str).values.tolist()
x = data["x"].astype(str).values.tolist()
y = data["y"].astype(str).values.tolist()

count = [str(i) for i in range(len(x))]

mact = ''
for i in range(len(x)):
    mact += count[i] + "," + etype[i] + "," + timestamp[i] + "," + x[i] + "," + y[i] + ";"
print(mact)
