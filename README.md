# BRKB_Composition_Tracker
This project intends to track the famous Warren Buffett Stock, Berkshire Hathaway Inc Class B (BRKB)

# Tracking: track the SEC Filling (quarterly report)
Using Web Scrapping to extract BRKB Filling details (every holding)

# Analysis
In BRKB_Composition_Tracker, the corresponding value and percentage of each holdings are calculated.

# Visualizaiton
`python .\Visualizer.py`
Visualize the composition of BRKB in a pie chart. Percentages are rounded to 2 decimal places.

# Save data to excel
`python .\ToExcel.py`
Save the data in pandas dataframe format to excel. Data includes the share's company name and the percentage of that share over BRKB.