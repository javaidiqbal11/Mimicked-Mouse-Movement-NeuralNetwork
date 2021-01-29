from sdv.tabular import GaussianCopula
import pandas as pd
data = pd.read_csv("data/mact_data.csv")

model = GaussianCopula()
model.fit(data)

model.save("model/gaussian.pkl")