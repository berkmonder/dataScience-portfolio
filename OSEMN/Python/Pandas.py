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

# Subset Observations (rows)

df[df.Length > 7] # Extract rows that meet logical criteria.

df.drop_duplicates() # Remove duplicate rows (only considers columns).

df.sample(frac=0.5) # Randomly select fraction of rows.

df.sample(n=10) # Randomly select n rows.

df.nlargest(n, 'value') # Select and order top entries.

df.nsmallest(n, 'value') # Select and order bottom n entries.

df.head(n) # Select first n rows.

df.tail(n) # Select last n rows.

# --------------------

# Subset Variables (columns)

df[['width', 'length', 'species']] # Select multiple columns with specific names.

df['width'] | df.width # Select single column with specific names.

df.filter(regex='regex') # Select columns whose name matches regular expression regex.

# --------------------

# Subset (rows and columns)

df.iloc[10:20] # Select rows 10-20.

df.iloc[:, [1, 2, 5]] # Select columns in positions 1, 2 and 5 (first column is 0).

df.loc[:, 'x2':'x4'] # Select columns between x2 and x4 (inclusive).

df.loc[df['a'] > 10, ['a', 'c']] # Select rows meeting logical condition, and only the specific columns.

df.iat[1, 2] # Access single value by index

df.at[4, 'A'] # Access single value by label

# --------------------

# Using query

df.query('Length > 7') # query() allows Boolean expressions for filtering rows.
df.query('Length > 7 and Widht < 8')
df.query('Name.str.startswith("abc")', engine='python')

# --------------------

# Logic in Python (and pandas)

<, >, ==, <=, >=, != # Less than, Greater than, Equals, Less than or equals, Greater than or equals, Not equals

df.column.isin(values), pd.isnull(obj), pd.notnull(obj) # Group membership, Is NaN, Is not NaN

&, |, ~, ^, df.any(), df.all() # Logical and, or, not, xor, any, all

# --------------------

# Handling Missing Data

df.dropna() # Drop rows with any column having NA/null data.

df.fillna(value) # Replace all NA/null data with value.

# --------------------

# Summarize Data

df['w'].value_counts() # Count number of rows with each unique value of variable

len(df) # Number of rows in DataFrame

df.shape # Tuple of number of rows, number of columns in DataFrame.

df['w'].nunique() # Number of distinct values in a column.

df.describe() # Basic descriptive and statistics for each column (or GroupBy).

df.sum() # Sum values of each object
df.count() # Count non-NA/null values of each object
df.median() # Median value of each object
df.quantile([0.25, 0.75]) # Quantiles of each object
df.apply(function) # Apply function to each object.
df.min() # Minimum value in each object.
df.max() # Maximum value in each object.
df.mean() # Mean value of each object.
df.var() # Variance of each object.
df.std() # Standard deviation of each object.

print(df)
