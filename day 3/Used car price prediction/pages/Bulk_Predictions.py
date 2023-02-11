import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Multiple cars price prediction")

model_selection=st.radio("Select model",["Linear Regression","Decision Tree","Random Forest"])


data_file=st.file_uploader("Upload cars data",type=["csv","xlsx"])
predict_clicked=st.button("Predict")
if predict_clicked:
    df=pd.read_csv(data_file)
    st.write()
    #st.dataframe(df)

    model=pickle.load(open('./models/lr_model.pkl','rb'))
        
    result=model.predict(df)
    result=np.round(result,0)
    result_df=pd.DataFrame(result,columns=['Predicted price'])

    df2=pd.concat([result_df,df],axis=1)

    # success
    st.dataframe(df2)

