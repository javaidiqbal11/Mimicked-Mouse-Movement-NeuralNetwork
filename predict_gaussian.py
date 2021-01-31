from sdv.tabular import CTGAN
model = CTGAN.load("model/gaussian.pkl")

fake_data = model.sample(100)
print(fake_data)
fake_data.drop('event_count', 1, inplace=True)

event_count = list(range(100))
fake_data["event_count"] = event_count
fake_data.to_csv("sample/gaussian.csv", index=False)
