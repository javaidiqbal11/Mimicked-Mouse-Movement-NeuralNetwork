import pandas as pd
import json

data = open("data/mact_data.txt").readlines()

timestamp = []
x = []
y = []
count = []
event_type = []
for row in data:
    arr = json.loads(row)
    values = arr["mact"].split(";")[:-1]
    for value in values:
        count.append(value.split(",")[0])
        event_type.append(value.split(",")[1])
        timestamp.append(value.split(",")[2])
        x.append(value.split(",")[3])
        y.append(value.split(",")[4])


data_df = pd.DataFrame({"event_count": count, "event_type": event_type, "timestamp": timestamp, "x": x, "y": y})
data_df["event_type"].replace(3, 1, inplace=True)
data_df.to_csv("data/mact_data.csv", index=False)

"""millis = int(millis)
seconds=(millis/1000)%60
"""
