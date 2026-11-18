# import numpy as np
# import pandas as pd
#
# product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
# #2d list, similar to 2d array
# indexes=[1,2,3]
# columns_name=['product', 'unit_sold']
# product_df = pd.DataFrame(data=product_data, index=indexes,
# columns=columns_name)
# print(product_df)
#
# product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
# [2000, 5000, 3000]}
# product_df = pd.DataFrame(data=product_data)
# print(product_df)
#
# products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
# [2, 'Plants', 6000], [3, 'Pencil', 3000]])
# product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
# columns=products[0,1:])
# print(product_pf) # output is same as of first case
#
# import pandas as pd
#
# df = pd.read_csv('C:\\Users\\c7741668\\OneDrive - Leeds Beckett University\\PDS\\dirtydata (2).csv')
# print(df.head(10))
#
# df = pd.read_csv('C:\\Users\\c7741668\\OneDrive - Leeds Beckett University\\PDS\\dirtydata (2).csv')
# new_df = df.dropna()
# print(new_df.to_string())
#
# df.fillna(130)
# print(new_df.to_string())
#
# df = pd.read_csv('C:\\Users\\c7741668\\OneDrive - Leeds Beckett University\\PDS\\dirtydata (2).csv')
# df["Calories"].fillna(130)
#
# df = pd.read_csv('C:\\Users\\c7741668\\OneDrive - Leeds Beckett University\\PDS\\dirtydata (2).csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)
#
#
# # df = pd.read_csv('C:\\Users\\c7741668\\OneDrive - Leeds Beckett University\\PDS\\dirtydata (2).csv')
# # x = df["Calories"].median()
# # df["Calories"].fillna(x, inplace = True)
# # df["Calories"].fillna(x, inplace = True)
#
# # df = pd.read_csv('C:\\Users\\c7741668\\OneDrive - Leeds Beckett University\\PDS\\dirtydata (2).csv')
# #
# # df['Date'] = pd.to_datetime(df['Date'])
# #
# # print(df.to_string())
#
# df.dropna(subset=['Date'], inplace = True)
# df.loc[7, 'Duration'] = 45
import pandas as pd

# Define file path safely using a raw string
file_path = r'C:\Users\c7741668\OneDrive - Leeds Beckett University\PDS\dirtydata (2).csv'

# 1. Load and inspect head
df = pd.read_csv(file_path)
print(df.head(10))

# 2. Drop rows with any missing values
df = pd.read_csv(file_path)
new_df = df.dropna()
print(new_df.to_string())

# 3. Fill missing values (best practice: fill numeric columns or assign back)
df = pd.read_csv(file_path)
# If filling the whole dataframe, ensure data types align, or fill specific columns:
df = df.fillna(130)
print(df.to_string())

# 4. Fill a specific column without chained assignment
df = pd.read_csv(file_path)
df["Calories"] = df["Calories"].fillna(130)

# 5. Fill missing values with the mean using direct assignment (No inplace=True)
df = pd.read_csv(file_path)
x = df["Calories"].mean()
df["Calories"] = df["Calories"].fillna(x)

# 6. Drop rows where 'Date' is missing using assignment instead of inplace=True
df = pd.read_csv(file_path)
df = df.dropna(subset=['Date'])

# 7. Safe modification using .loc
df.loc[7, 'Duration'] = 45
print(df.head(10))
df = pd.read_csv(file_path)

# Fill a specific column
df["Calories"] = df["Calories"].fillna(130)