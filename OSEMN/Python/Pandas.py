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

sum() # Sum values of each object
count() # Count non-NA/null values of each object
median() # Median value of each object
quantile([0.25, 0.75]) # Quantiles of each object
apply(function) # Apply function to each object.
min() # Minimum value in each object.
max() # Maximum value in each object.
mean() # Mean value of each object.
var() # Variance of each object.
std() # Standard deviation of each object.

# --------------------

# Make New Columns

df.assign(Area=lambda df: df.Length*df.Height) # Compute and append one or more new columns.

df['Volume'] = df.Length*df.Height*df.Depth # Add single column.

pd.qcut(df.col, n, labels=False) # Bin column into n buckets.

# --------------------

df.max()

max(axis=1) # Element-wise max.
min(axis=1) # Element-wise min.
clip(lower=-10, upper=10) # Trim values at input tresholds
abs() # Absolute value.

# --------------------

# Combine Data Sets

pd.merge(adf, bdf, how='left', on='x1') # Join matching rows from bdf to adf.

pd.merge(adf, bdf, how='right', on='x1') # Join matching rows from adf to bdf.

pd.merge(adf, bdf, how='inner', on='x1') # Join data. Retain only rows in both sets.

pd.merge(adf, bdf, how='outer', on='x1') # Join data. Retain all values, all rows.

# --------------------

adf[adf.x1.isin(bdf.x1)] # All rows in adf that have a match in bdf.

adf[~adf.x1.isin(bdf.x1)] # All rows in adf that do not have a match in bdf.

# --------------------

pd.merge(ydf, zdf) # Rows that appear in both ydf and zdf (Intersection).

pd.merge(ydf, zdf, how='outer') # Rows that appear in either or both ydf and zdf (Union).

pd.merge(ydf, zdf, how='outer', indicator=True).query('_merge == "left_only"').drop(columns=['_merge']) # Rows that appear in ydf but not zdf (Setdiff).

# --------------------

# Group Data

df.groupby(by='col') # Return a GroupBy object, grouped by values i column named "col".

df.groupby(level='ind') # Return a GroupBy object, grouped by values in index level named 'ind'.

# --------------------

df.groupby().size()

size() # Size of each group.
agg(function) # Aggregate group using function.

shift(1) # Copy with values shifted by 1.
shift(-1) # Copy with values lagged by 1.
rank(method='dense') # Ranks with no gaps.
rank(method='min') # Ranks. Ties get min rank.
rank(method='first') # Ranks. Ties go to first value.
rank(pct=True) # Ranks rescaled to interval [0, 1].
cumsum() # Cumulative sum.
cummax() # Cumulative max.
cummin() # Cumulative min.
cumprod() # Cumulative product.