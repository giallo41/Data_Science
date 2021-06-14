import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_feature_importance(clf, column_names):
    '''
    Plot feature importance graph using classifier 
    '''
    feature_imp = pd.DataFrame(sorted(zip(clf.feature_importances_,column_names)), columns=['Importance','Feature'])

    plt.figure(figsize=(8, 6))
    sns.barplot(x="Importance", y="Feature", data=feature_imp.sort_values(by="Importance", ascending=False))
    plt.title("Features Importance")
    plt.tight_layout()
    plt.show()
    

class LabelEncoding():
    '''
    LabelEncoding Class 
    Encoding the categorical value to numerical number 
    Use : fit() -> trainsform() or fit_transform() 
    Can take inverse_transform from the data 
    '''
    def __init__ (self):
        pass

    def fit(self, data, columns):

        self.columns = columns
        col_dic = {}
        inverse_dic = {}
        for col in columns:
            col_unique = data[col].unique()
            col_unique_dic = {}
            item_to_idx = {}
            for idx, item in enumerate(col_unique):
                col_unique_dic[item] = idx
                item_to_idx[idx] = item
            col_dic[col] = col_unique_dic
            inverse_dic[col] = item_to_idx

        self.item_to_idx = col_dic
        self.idx_to_item = inverse_dic

    def transform(self, data):
        df = data.copy()
        for col in self.columns:
            df[col] = df[col].map(self.item_to_idx[col])

        return df

    def inverse_transform(self, data):
        df = data.copy()
        for col in self.columns:
            df[col] = df[col].map(self.idx_to_item[col])

        return df

    def fit_transform(self, data, columns):
        df = data.copy()
        self.fit(df, columns)
        df = self.transform(df)

        return df
