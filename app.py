import streamlit as st
import numpy as np
import pickle


model = pickle.load(open("model.pkl",'rb'))
st.title("Hiring Predictor")

def predict_note_authentication(var,var2,var3):
    prediction=model.predict([[var,var2,var3]])
    print(prediction)
    return prediction


def main():

    nav = st.sidebar.radio("Navigation",["Home","Prediction"])
    if nav == "Home":
        
        if st.checkbox("Show Table" , True):
            st.write("Welcome")

        
    if nav == "Prediction":
        st.header("Know your hiring")
        var = st.number_input("Enter you experience")
        #var = np.array(var).reshape(1,-1)
        var2 = st.number_input("Enter you test_score",)
        #var2 = np.array(var2).reshape(1,-1)
        var3 = st.number_input("Enter you interview_score",0.00)
        #var3 = np.array(var3).reshape(1,-1)

    

        if st.button("Predict"):
            result=predict_note_authentication(var,var2,var3)
            st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()