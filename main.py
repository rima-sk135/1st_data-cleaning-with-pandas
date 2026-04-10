import pandas as pd
import numpy as np
from functools import reduce

df = pd.read_csv(r"C:\Users\user\Documents\test-julia\BL-Flickr-Images-Book.csv")
print(df.head())
print(df.describe())
print(df.info())

# now dropping the columns unnecessary for this analysis
to_drop=["Edition Statement",
         "Corporate Author",
         "Corporate Contributors",
         "Former owner",
         "Engraver",
         "Contributors",
         "Issuance type",
         "Shelfmarks"]
df.drop(to_drop, inplace=True, axis=1)
print(df.head())

df.set_index("Identifier", inplace=True)
print(df.head())

unwanted_characters =["[", ",", "-"]
def clean_dates(item):
    dop = str(item.loc["Date of Publication"])

    if dop == "nan" or dop[0] == "[":
        return np.NaN
    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]
    return dop
df["Date of Publication"]=df.apply(clean_dates, axis=1)
print(df["Date of Publication"].head(15))
print(df["Date of Publication"][667])