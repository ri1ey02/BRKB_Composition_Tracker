import pandas as pd
import BRKB_Composition_Tracker

df = pd.DataFrame(data=BRKB_Composition_Tracker.getData(), index=["Percentage"])

df = (df.T)

df.to_excel('output/BRKB_composition.xlsx')