"""
this file could contain all functions that we want to use  in the project.
e.g.
def function_name(parameter_name):
    local_variable=0
    return
"""
# Please Note that the function name should be in snake case and the parameters , local variables in the same convention 
import re
import pandas as pd
import seaborn as sns


def get_columns_values(text:str) -> dict:
    """ 
    this function takes text and return dictionary of key value based on the given text
    Args:
        text ([str]): the text need to be sliced

    Returns:
        dict: dictionary of all keys and values for the encoding
    """
    pattern = r'(\d+): ([\w\s-]+)[\s$]' # split the data in the shape of number:some_text 
    return dict(re.findall(pattern, text,re.MULTILINE)) # create a dict from the matches of the pattern in the text

def one_hot_encoding(data:pd.DataFrame,column:str,dictionary:dict)->pd.DataFrame:
    """this function does one hot encoding on a given cloumn inside dataframe

    Args:
        data (pd.DataFrame): the dataFrame to work in
        column (str): the column name to work in
        dictionary (dict): the dictionary used to map the values 

    Returns:
        pd.DataFrame: new DataFrame with one hot encoding on it
    """
    try:
        data[column] # if the coulmn name is invalid return the data as it is
    except Exception:
        return data
    data[column] = data[column].astype(str) # convert the coulmn to str type
    data[column] = data[column].map(dictionary) # map each value in the cell to the value on the dict
    one_hot = pd.get_dummies(data[column], prefix=column) # create columns and fill it with 0 and 1 based on the cell value
    data = pd.concat([data, one_hot], axis=1) # merge the two dataframes
    data = data.drop(column, axis=1) # drop the old column
    return data
    
def count_plot_percentage(data, feature):
    """ Plot count(frequency) for feature's values along with their percentage written on each bar

    Args:
        data (pd.DataFrame): data frame
        feature (str): column name
    """
    ax = sns.countplot(x=data[feature])

    # Add count on each plot
    total = data.shape[0]
    for p in ax.patches:
        percentage = f'{(100 * p.get_height()/total):.1f}%'
        x = p.get_x() + p.get_width() / 2 - 0.1
        y = p.get_y() + p.get_height()
        ax.annotate(percentage, (x, y))