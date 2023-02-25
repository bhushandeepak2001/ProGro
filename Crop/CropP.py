import streamlit as st
import pickle

st.title('Crop Prediction !!')
N = st.number_input('Enter Nitrogen value : ', min_value=0.0, max_value=140.0, step=0.1)
P = st.number_input('Enter Phosphorus value : ', min_value=0.0, max_value=140.0, step=0.1)
K = st.number_input('Enter Potassium value : ', min_value=0.0, max_value=200.0, step=0.1)
T = st.number_input('Enter Temperature value : ', min_value=0.0, max_value=44.0, step=0.1)
H = st.number_input('Enter Humidity value : ', min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input('Enter pH value : ', min_value=0.0, max_value=9.9, step=0.1)
ra = st.number_input('Enter Rainfall value : ', min_value=0.0, max_value=299.0, step=0.1)
# st.button('Predict')

x = [[N, P, K, T, H,ph, ra]]
st.markdown(f'My Values are : {x}')

model = pickle.load(open('crop.pkl', 'rb'))
cv = pickle.load(open('vect.pkl', 'rb'))

def main():
    if st.button('predict'):
        data = x
        pred = model.predict(data)
        st.markdown(f'Predicted Crop is : {pred}')
        speak(f'Predicted Crop is : {pred}')

main()
co = st.text_input('Any Comment : ')
st.write(co)
st.write('Thank You !!')