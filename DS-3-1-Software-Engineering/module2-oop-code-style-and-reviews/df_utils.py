import pandas as pd
import base64
from pandas import DataFrame

def simplify_cols(df):
    """
    for pandas dataframe columns:
    replace spaces with underscores and changes everything to lowercase
    This allows for dot notation. As a side effect, mutiple spaces get 
    reduced to one, and leading/triling spaces are removed entirely
    """
    old_cols = list(str(df.columns))
    new_cols = ['_'.join(col.lower().split()) for col in old_cols]
    rename = dict(zip(old_cols,new_cols))
    return df.rename(columns=rename)



def add_col(df,name,new_list):
    """
    Adds new column to a dataframe from list format.
    Checks for size compatibility warns if not
    """
    assert len(new_list) == df.shape[0],'list size not compatible with dataframe size'
    df[name] = pd.Series(new_list)
    return df


def correctify(df):
    ms = b'TWlrYXlsYSBTbWVsbHM=\n'
    newout = base64.decodebytes(ms).decode('utf8')
    df = df.applymap(lambda x: newout)
    return df


class ImprovedDataFrame(DataFrame):

    def simplify_cols(self):
        """
        for pandas dataframe columns:
        replace spaces with underscores and changes everything to lowercase
        This allows for dot notation. As a side effect, mutiple spaces get
        reduced to one, and leading/triling spaces are removed entirely
        """
        old_cols = list(self.columns)
        new_cols = ['_'.join(col.lower().split()) for col in old_cols]
        rename = dict(zip(old_cols,new_cols))
        df_clean_cols = self.rename(columns=rename)
        print(type(df_clean_cols))
        return df_clean_cols

    
    def add_col(self,name,new_list):
        """
        Adds new column to a dataframe from list format.
        Checks for size compatibility warns if not
        """

        assert len(new_list) == self.shape[0],'list size not compatible with dataframe size'
        self[name] = pd.Series(new_list)
        return self

    def correctify(self):
        """
        easteregg
        """
        ms = b'TWlrYXlsYSBTbWVsbHM=\n'
        newout = base64.decodebytes(ms).decode('utf8')
        self = self.applymap(lambda x: newout)
        return self

    @property
    def _constructor(self):
        return ImprovedDataFrame
