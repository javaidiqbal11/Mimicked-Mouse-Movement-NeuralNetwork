from sdv.tabular import CTGAN
import pandas as pd

data = pd.read_csv("data/mact_data.csv", nrows=100000)
print(data.head(5))

# convert milliseconds to seconds
# data["timestamp"] = data["timestamp"].apply(lambda x: (x/1000) % 60)

data.info()
print(data.head(5))
model = CTGAN()
model.fit(data)
model.save("model/gan.pkl")
