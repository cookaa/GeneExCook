# TODO add a cool title and text
'''
# geneExCook a project to determine correlation between specific gene expressions


'''


import pandas as pd
from pandas.core import indexing
from pandas.core.frame import DataFrame
import streamlit as st
from sklearn.metrics import r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv




st.set_page_config(page_title="geneExCook", page_icon='🧬', layout="centered", initial_sidebar_state="auto")
def streamlitSettings():
    st.title("geneExCook")
    st.page_icon='🧬'   #'DNA' or 'DNA Double Helix'
    # adding sidbar
    add_selectbox = st.sidebar.selectbox(
        "Run Tests",
        ("Select File", "Run Correlation")
    )
# End of streamlitSettings()


def normalize(data, data_norm):
    st.text('Normalizing Values...')
    #[18.839463	33.366852	620290.36	713592.009	39.8100005	33.6167345	29.1206628	34.7183343] # Normalization factors (A-H)
    HK_A = 18.839463
    HK_B = 33.366852
    HK_C = 620290.36
    HK_D = 713592.009
    HK_E = 39.8100005
    HK_F = 33.6167345
    HK_G = 29.1206628
    HK_H = 34.7183343

    # Calculating normalizations by column
    data_norm = DataFrame # create a copy of data
    data_norm = data        # TODO FIX
    if st.checkbox('Show data before Normalization'): st.write('data before norm',data)
    data_norm.A = HK_A * data.A   # data["A"] = 2 * data["A"] #same result
    data_norm.B = HK_B * data.B 
    data_norm.C = HK_C * data.C 
    data_norm.D = HK_D * data.D
    data_norm.E = HK_E * data.E
    data_norm.F = HK_F * data.F
    data_norm.G = HK_G * data.G
    data_norm.H = HK_H * data.H
    if st.checkbox('Show data after Normalization'): st.write('data_norm after using 10 HK genes average',data_norm)
    return data_norm
# End of normalize()


# TODO
def correlation(data_norm):
    st.text('calculating correlation...')
    #attmept 1
    # rSquare = []
    # # for index, rows in data_norm.iterrows():
    # for rows in data_norm:
    #     # r_val = r2_score(data_norm.index, data_norm.index)
    #     r_val = r2_score(data_norm,data_norm)
    #     # st.write(r_val) #TODO remove
    #     rSquare.index = r_val# End of correlation(data_norm)
    #     print(r_val)
    # st.write('rSquare', rSquare)


    # #attempt 2
    # df = pd.DataFrame({'c1': [10, 11, 12], 'c2': [100, 110, 120]})
    # for i<100, row in df.iterrows():
    #     print(row['c1'], row['c2'])

    #attempt 3
    # for row in data_norm:
    #     r_val = []
    #     st.write(row)
    #     # r_val = [r2_score(data_norm.A,data_norm.B)] # *does not work*
    #     st.write('r_val', r_val)

    # #attempt 4 
    # # convert column into an array, then iterate trough one at a time
    # rSquare = []
    # # data_norm.A = [] # convert to array
    listA = []
    listA = data_norm.A
    # listB = data_norm.B
    # for row in listA:
    #     st.write(row)       # works to iterate through!
    #     data_norm.corr()    # or corr(method='spearman')
    #     st.write(data_norm.corr(method='spearman'))
    #     # a = r2_score(data_norm['listA'],data_norm['listB'])
    #     # rSquare = r2_score(data_norm.A,data_norm.B) # nope
        #     # r_val = [r2_score(data_norm.A,data_norm.B)] # *does not work*

    # # attempt 5 - fix type error
    # data_norm = DataFrame
    # a1 = DataFrame
    # a1 = pd.read_csv('testdata_1.csv')   #'testdata_1.csv'
    # st.write(a1)
    # st.write(data_norm.corr(method='spearman'))
    # df = pd.DataFrame(np.random.randn(1000, 3), columns=['a', 'b', 'c'])
    
    # Attempt 6 - works!!!!
    
    pCoef = data_norm.corr()
    sCoef = data_norm.corr(method='spearman')
    if st.checkbox('Pearson Coefficeint'): st.write( pCoef)
    if st.checkbox('Spearman Coefficeint'): st.write('Spearman Coefficeient', sCoef)

    #TODO try this
#     dataframe.corrwith(series). I.e.: dfb.corrwith(dfa.iloc[0], axis=1)

# End of correlation()


def genHeatmap(data, data_norm):
    st.text('Generating heatmaps...')


    # fixing dataframe for correlation
    # # rotating data by 90% to make it readable for the compare which compares columns
    # st.write(data_norm)   

    # ID's
    index = []
    index = data_norm.ID

    data_norm.set_index(index, drop=False)
    data_norm_r = data_norm.transpose()   # or .T
    # data_norm_rdrop = data_norm_r.drop(index='ID')                        # drop the ID name that was confusing the comparision
    # st.write('after ID', data_norm_r)
    
    
    # data_norm_rdrop = pd.DataFrame(data=data_norm_rdrop,index=index)
    data_norm_rdrop = data_norm_r.set_axis(index, axis=1, inplace=False)      # include index
    # or 
    # data_norm_rdrop = data_norm_r.set_index(index)
    # data_norm_rdrop = data_norm_r
    # or
    # pd.Series(corr2_coeff_rowwise(data_norm.values,data_norm.values))



    # Figure Labels
    # xticklabels = data_norm_r.ID
    # st.write('data_norm_r',data_norm_r, 'data_norm_rdrop',data_norm_rdrop)


    # Correlation
    pCoef = DataFrame
    pCoef = data_norm_rdrop.corr()
    sCoef = data_norm_r.corr(method='spearman')
    

    # Create fig with seaborn
    fig, ax = plt.subplots()

    sns.heatmap(data_norm_r.corr(), vmin=0, vmax=1, linewidth=0.3)               # for labels look at https://seaborn.pydata.org/generated/seaborn.heatmap.html
    # sns.heatmap(pCoef, linewidth=0.3)
    if st.checkbox('Pearson Coerfficeint Heatmap'): st.write('Person Coeffiecent', fig)


    # sns.heatmap(sCoef, vmin=0, vmax=1, linewidth=0.3)
    # if st.checkbox('Spearman Coefficeint Heatmap'):st.write('Spearman Coeffiecent Heatmap', fig2)
    # hm_norm = sns.heatmap(data_norm)
    # st.write(hm_norm)


    # create fig with matplotlib


    # writing to csv file 
    if st.checkbox('Save corrleation data to a csv file'): pCoef.to_csv('pCoef.csv', encoding='utf-8', index=False)
    
# End of genHeatmap()


# @st.cache
def readFile(data):
    filename = 'testdata_1.csv'
    data = pd.read_csv(filename)
    # data = data_norm(10, file)        # *does not work* trying to read in first 10 rows
    # st.write('done readData')
    return data

#end of readFile()
    


if __name__ == '__main__':
    streamlitSettings()   
    
    # TODO find a way to place into readFile()
    #  data = DataFrame
    filename = 'testdata_1.csv'
    data = pd.read_csv(filename)
    data_norm = pd.read_csv(filename)   #'testdata_1.csv'
    # End TODO

    readFile(data)
    # determineHK(data_norm)    #placed into normalize
    normalize(data, data_norm)
    correlation(data_norm)
    genHeatmap(data, data_norm)
    # saveCorrelation(data, data_norm)

# End of main


# Catch
else:
    st.write("Ran into an error!")
    help()
    sys.exit(0)
# End of catch
