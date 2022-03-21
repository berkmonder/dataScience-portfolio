# Imports
import pandas as pd

# Creating Series

s = pd.Series(['a', 'b', 'c'],  index=[1,  2,  3])

# --------------------

# Creating DataFrame

df = pd.DataFrame({
    'a': [4, 5, 6],
    'b': [7, 8, 9],
    'c': [10, 11, 12]},
    index=[1, 2, 3]) # Specify values for each column.

df = pd.DataFrame(
    [[4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]],
    index=[1, 2, 3],
    columns=['a', 'b', 'c']) # Specify values for each row.

df = pd.DataFrame({
    'a': [4, 5, 6],
    'b': [7, 8, 9],
    'c': [10, 11, 12]},
    index=pd.MultipleIndex.from_tuples(
        [('d', 1), ('d', 2),
        ('e', 2)], names=['n', 'v'])) # Create DataFrame with a MultiIndex

# --------------------

# Reshaping Data

pd.melt(df) # Gather columns into rows.

df.pivot(columns'var', values='val') # Spread rows into columns.

# --------------------

pd.concat([df1, df2]) # Append rows of DataFrames.

pd.concat([df1, df2], axis=1) # Append columns of DataFrames.

# --------------------

df.sort_values('mpg') # Order rows by values of a column (low to high).

df.sort_values('mpg', ascending=False) # Order rows by values of a column (high to low).

df.rename(columns={'y': 'year'}) # Rename the columns of a DataFrame.

df.sort_index() # Sort the index of a DataFrame.

df.reset_index() # Reset index of DataFrame to row numbers, moving index to columns.

df.drop(columns=['Length', 'Height']) # Drop columns from DataFrame.

# --------------------



print(df)