from sdv.tabular import CTGAN
model = CTGAN.load("model/gan.pkl")

fake_data = model.sample(100)
print(fake_data)

fake_data.to_csv("sample/gan.csv", index=False)
