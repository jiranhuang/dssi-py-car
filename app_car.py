import streamlit as st
from src.inference_car import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Car Details')
    fueltype_options = ['CNG','Diesel','Petrol']
    fueltype = st.sidebar.selectbox("Fuel Type", fueltype_options)
    age = st.sidebar.slider('Age', 0, 100, 10, 1)
    km = st.sidebar.text_input("KM '000s", placeholder="in '000s")
    hp = st.sidebar.slider('Horse Power', 50, 250, 100, 1)
    cc = st.sidebar.slider('CC', 1000, 2500, 1500, 50)
    doors = st.sidebar.slider('Doors', 2, 5, 5, 1)
    weight = st.sidebar.slider('Weight', 1000, 1800, 1200, 5)
    #loan_amnt = st.sidebar.text_input('Loan Amount')
    def get_input_features():
        input_features = {'fueltype': fueltype,
                          'age': age,
                          'km': int(km)*1000,
                          'hp': hp,
                          'cc': cc,
                          'doors': doors,
                          'weight': weight
                          #'loan_amnt': int(loan_amnt)
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Estimate", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 20px;"><b> Welcome to DSSI Car Price Estimation Workshop </b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment estimates:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(fueltype=st.session_state['input_features']['fueltype'],
                                    age=st.session_state['input_features']['age'],
                                    km=st.session_state['input_features']['km'],
                                    hp=st.session_state['input_features']['hp'],
                                    cc=st.session_state['input_features']['cc'],
                                    doors=st.session_state['input_features']['doors'],
                                    weight=st.session_state['input_features']['weight'],
                                    )
        #if assessment.lower() == 'yes':
        #    st.success(default_msg.format('Approved'))
        #else:
        #    st.warning(default_msg.format('Rejected'))
        if assessment > 0 :
            st.success(default_msg.format(assessment))
        else:
            st.warning(default_msg.format("Can't estimate with these parameters"))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()