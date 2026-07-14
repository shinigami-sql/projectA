import pandas as pd  # Library for working with DataFrames and Series
import ast  # Abstract Syntax Tree — treats code as a tree object with nodes, puts Python in read/analyze mode instead of execute

figures_df= pd.read_csv('figures_datapoints.csv')
figures_df['Data Points'] = figures_df['Data Points'].apply(ast.literal_eval)  # pandas reads Data Points as plain strings — ast.literal_eval converts each string back into its corresponding Python literal, a list of tuples in this case. 
figures_df.set_index('Figure', inplace=True) # Sets the 'Figure' column as the index. 
