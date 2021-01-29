from sdv.timeseries import PAR
import pandas as pd

data = pd.read_csv("data/mact_data.csv", nrows=100000)
context_columns = ["x", "y"]
entity_columns = ["event_type"]
sequence_index = "event_count"

model = PAR(
    entity_columns=entity_columns,
    sequence_index=sequence_index,)

model.fit(data)
model.save('model/par.pkl')
