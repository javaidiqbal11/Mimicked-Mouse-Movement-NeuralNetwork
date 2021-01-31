from sdv.timeseries import PAR
model = PAR.load("model/mact.pkl")

fake_data = model.sample(1, sequence_length=100)
fake_data.to_csv("sample/par.csv", index=False)
# for i in range(10):
#     fake_data = model.sample(1, sequence_length=100)
#
#     print(fake_data)
