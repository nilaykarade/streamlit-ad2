
# import module
import streamlit as st
import pickle
import numpy as np
#import sklearn 
# Title
st.image("car.png",width=100)
#st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)
st.title("Car price prediction")

# Header
st.header("Please enter your car details")

kms=st.number_input('Enter kms', 0,10000000)
car_age=st.number_input('Enter car age', 0,100)
original_price=st.number_input('Enter original price', 1,50000000)
fuel=st.radio("Select fuel type: ", ('Petrol', 'Diesel','CNG'))
transmission=st.selectbox("Select transmission type: ", ['Manual', 'Automatic'])
predict_clicked=st.button("Predict car price")
 
# Create a button, that when clicked, shows a text
if predict_clicked:
    model=pickle.load(open('./models/lr_model.pkl','rb'))
    
    if fuel=='Petrol':
        fuel=list([0,1])
    elif fuel=='Diesel':
        fuel=list([1,0])
    else:
        fuel=list([0,0])

    
    if transmission=='Manual':
        transmission=1
    else:
        transmission=0

    data=[np.array([kms,original_price,car_age,fuel[0],fuel[1],transmission])]
    result=model.predict(data)
    final_prediction=round(result[0],0)
    # success
    st.success("Predicted car price is "+str(final_prediction))
