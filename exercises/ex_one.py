import pandas as pd

# convert to csv to load faster

# df = pd.read_excel("C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\WDIEXCEL.xlsx")
# df.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\WDIEXCEL.csv', sep=';')
# df = pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\WDIEXCEL.csv', sep=';')
# df = df.loc[df['Country Code'].isin({"GRC", "DEU", "FRA", "ITA"})]
# df.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\my_countries.csv', sep=';')
# df = pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\my_countries.csv', sep=';')
# df.drop(df.columns[[0, 1]], axis=1, inplace=True)
# df.to_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\countries.csv', sep=';')

df = pd.read_csv('C:\\Users\\andre\\Desktop\\ΣΠΟΥΔΕΣ\\ΠΜΣ ΠΑΠΕΙ\\ΜΑΘΗΜΑΤΑ\PYTHON\\b professor\\εργασιες\\Project3-2020\\countries.csv', sep=';')
df.drop(df.columns[[0]], axis=1, inplace=True)

percent_missing_rows = df.apply(lambda x: x.count(), axis=1) * 100 / 60 # for each row

print("Measuring the percentage of blank entries each line \n", percent_missing_rows)

percent_missing_cols = df.isnull().sum() * 100 / len(df) # for each column

missing_value_df = pd.DataFrame({'column_name': df.columns,
                                 'percent_missing': percent_missing_cols})

missing_value_df.sort_values('percent_missing', inplace=True)

print("larger coherent data set: \n",missing_value_df)