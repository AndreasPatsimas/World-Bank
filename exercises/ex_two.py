import wbdata
import pandas as pd

# set up the countries I want
countries = ["GRC", "DEU", "FRA", "ITA"]

# set up the indicator I want (just build up the dict if you want more than one)
indicators = {'NY.GNP.PCAP.CD': 'GNI per Capita', 'MS.MIL.TOTL.TF.ZS': 'Armed forces personnel (% of total labor force)'}

# grab indicators above for countries above and load into data frame
df = pd.DataFrame(wbdata.get_dataframe(indicators, country=countries, convert_date=False))

print(df)