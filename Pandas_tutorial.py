# fun with  data science
# https://www.youtube.com/channel/UCyU1CDYl_NX8nsxCCkKfk3A

import pandas as pd
import numpy as np

print(pd.__version__)

# part06: interpolate function
print("part06: interpolate function\n")
df_1 = pd.DataFrame({"A": [12, 10, 9, None, 1],
                     "B": [None, 16, 24, 2, None],
                     "C": [25, 19, None, 5, 9],
                     "D": [14, 29, None, None, 5]})

print("df:\n", df_1)

print("interpolate_forward:\n", df_1.interpolate(method="linear", limit_direction="forward"))

print("interpotale_backward:\n", df_1.interpolate(method="linear", limit_direction="backward", limit=1))

# part07: Making dataframe using numpy pandas
print("part07: Making dataframe using numpy pandas\n")
values_1 = np.random.randint(10, size=10)
values_2 = np.random.randint(10, size=10)
years = np.arange(2005, 2015)
groups = ['A', 'A', 'B', 'A', 'B', 'B', 'C', 'A', 'C', 'C']
df_2 = pd.DataFrame({'group': groups, 'year': years, 'value_1': values_1, 'value_2': values_2})

print(df_2)

print(df_2.query('value_1 < value_2'))

# part08: functions : insert, cumsum, sample
print("part08: functions : insert, cumsum, sample'\n")

new_col = np.random.randint(10)
df_2.insert(2, 'new_col', new_col)
print(df_2)

df_2['cumsum_2'] = df_2[['value_2', 'group']].groupby('group').cumsum()
print(df_2)

sample1 = df_2.sample(n=3)
print(sample1)

sample2 = df_2.sample(frac=0.5)
print(sample2)

# part09: functions: isin, loc, iloc, rank
print("part09: functions: isin, loc, iloc, rank\n")
years = [2006, 2009, 2013]
print(df_2[df_2.year.isin(years)])

print(df_2.loc[:2, ['group', 'year']])

print(df_2.iloc[:3, :4])
print()
print(df_2.value_2.pct_change())
print()
df_2['rank'] = df_2['value_1'].rank()
print(df_2)

# part10: row and column wise function application| mean function
print("part10: row and column wise function application| mean function\n")
print()
df_3 = pd.DataFrame(np.random.randn(6, 3), columns=['first', 'second', 'third'])
print(df_3)
print('mean\n', df_3.apply(np.mean))
print('axis=1 mean\n', df_3.apply(np.mean, axis=1))

# part11: covariance . relation between two random variables
print("part11: covariance . relation between two random variables\n")
a1 = pd.Series(np.random.randn(8))
a2 = pd.Series(np.random.randn(8))
print("a1\n", a1)
print("a2\n", a2)
print("covariance between a1 and a2: ", a1.cov(a2))
print()
b = pd.DataFrame(np.random.randn(8, 4), columns=["a1", "a2", "a3", "a4"])
print()
print("b\n", b)
print("b['a1'].cov(b['a2'])\n", b['a1'].cov(b['a2']))
print("b.cov()\n", b.cov())

# part12: correlation function. linear relationship between two array of values
print("part12: correlation function. linear relationship between two array of values\n")
print()
a = pd.DataFrame(np.random.rand(10, 5), columns=["a", "b", "c", "d", "e"])
print("a\n", a)
print("a['a'].corr(a['b']))\n", a['a'].corr(a['b']))
print("a.corr()\n", a.corr())
print("b\n", b)
b = pd.DataFrame(np.random.randn(8, 4), columns=['a1', 'a2', 'a3', 'a4'])
print("b['a1'].corr(b['a2'])\n", b['a1'].corr(b['a2']))
print("b.corr()\n", b.corr())

# NOTE: if any non-numeric column is present in DataFrame it is excluded automatically

print("Pandas Tutorial Part:13 | .rolling() function \n")

a = pd.DataFrame(np.random.randn(10, 4),
                 index=pd.date_range('1/1/2000', periods=10),
                 columns=['One', 'Two', 'Three', 'Four'])
print("a\n", a)
print(a.rolling(window=3).mean())

print("Pandas Tutorial Part:14 | .expanding() function |"
      " statistical function using pandas | python pandas\n")

b = pd.DataFrame(np.random.randn(10, 5),
                 index=pd.date_range('2/2/2001', periods=10),
                 columns=['A', 'B', 'C', 'D', 'E'])

print(b.expanding(min_periods=3).mean())

print("Pandas Tutorial Part:15 | .melt() function | "
      "statistical function using pandas | python pandas")

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

print("df\n", df)
print("pd.melt(df, id_vars=['A'], value_vars=['B'])",
      pd.melt(df, id_vars=['A'], value_vars=['B']))
print()
print("pd.melt(df, id_vars=['A'], value_vars=['B'],\
 var_name='MyVarname', value_name='myValuename')\n",
      pd.melt(df, id_vars=['A'], value_vars=['B'],
              var_name='MyVarname', value_name='myValuename'))

print("Pandas Tutorial Part:16 pivot() function |"
      " statistical function using pandas | python pandas")

df = pd.DataFrame({'A':['one','one','one','two','two','two'],
                   'B':['A','B','C','A','B','C'],
                   'C':[1,2,3,4,5,6],
                   'D':['p','q','r','s','t','u']})

print("df\n", df)

print("df.pivot(index='A', columns='B')['C']\n",
      df.pivot(index='A', columns='B')['C'])

print("df.pivot(index='A', columns='B', values=['C','D'])\n",
      df.pivot(index='A', columns='B', values=['C', 'D']))

print("Pandas Tutorial Part:17 unique() function |"
      " statistical function using pandas | python pandas")

values_1 = np.random.randint(10, size=10)
values_2 = np.random.randint(10, size=10)
years = np.arange(2005, 2015)
groups = ['A','A','B','B','C','C','D','D','A','B']
df = pd.DataFrame({'Characters': groups, 'Year': years,
                   'Number_1': values_1, 'Number_2' : values_2})

print('df\n', df)

print('df.Year.nunique()\n', df.Year.nunique())
print('df.Characters.nunique()\n', df.Characters.nunique())
print('df.nunique()\n', df.nunique())

print("Pandas Tutorial Part:18 memory usage() function "
      "| statistical function using pandas | python pandas")

#This is a function that returns how many memory each column uses in bytes.
#It is especially used when we work with large dataframes

df_memory = pd.DataFrame({'One': np.random.randn(100000),
                          'Two': np.random.randint(100, size=100000)})

print(df_memory.shape)
print(df_memory.memory_usage())

print(df_memory.memory_usage().sum()/(1024**2)) #converting into megabytes


print("Pandas Tutorial Part:19 select datatypes function and replace | pandas | python pandas\n")

values_1 = np.random.randint(10, size=10)
values_2 = np.random.randint(10, size=10)
years = np.arange(2005, 2015)
groups = ['A','A','B','B','C','C','D','D','A','B']
df = pd.DataFrame({'Characters': groups, 'Year': years,
                   'Number_1': values_1, 'Number_2': values_2})

print(df)
print()
print(df.select_dtypes(include='int32'))
print()
print(df.select_dtypes(exclude='int32'))

print(df.replace('B', 'second'))

print("Pandas Tutorial Part:20 nsmallest and nlargest functions")

df = pd.DataFrame({'Class': [10,11,12,6,2,9,3],
                   'marks': [54,12,78,92,34,22,67],
                   'name': ['A','B','C','D','E','F','G'],
                   'age': [15,13,17,14,18,12,9]})

print(df.nsmallest(5, 'marks'))

print(df.nlargest(5, 'age'))




