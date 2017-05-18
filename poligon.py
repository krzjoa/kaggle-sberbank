# -*- coidng: utf-8 -*-

import pandas as pd

from sklearn.preprocessing import StandardScaler
from feat_eng.map import geocode

scaler = StandardScaler()

# Wczytywaie danych
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

raions =  train.sub_area.unique()

rows = []

for r in raions:
    lat, lon = geocode(r)
    print lat, lon
    rows.append(
        {'raion': r, 'latitude': lat, 'longitude':lon}
    )

pd.DataFrame(rows).to_csv("feat_eng/loc.csv")



