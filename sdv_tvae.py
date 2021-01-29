from sdv.tabular import TVAE
import pandas as pd

data = pd.read_csv("data/mact_data.csv")
model = TVAE(field_names=["timestamp", "x", "y"])

model.fit(data)

model.save("model/tvae.pkl")