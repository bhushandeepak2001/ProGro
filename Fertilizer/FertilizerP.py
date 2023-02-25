import streamlit as st
import pickle

st.title('Crop Prediction !!')
N = st.number_input('Enter Nitrogen value : ', min_value=0.0, max_value=45.0, step=0.1)
P = st.number_input('Enter Phosphorous value : ', min_value=0.0, max_value=42.0, step=0.1)
K = st.number_input('Enter Potassium value : ', min_value=0.0, max_value=19.0, step=0.1)
T = st.number_input('Enter Temperature value : ', min_value=0.0, max_value=38.0, step=0.1)
H = st.number_input('Enter Humidity value : ', min_value=0.0, max_value=72.0, step=0.1)
M = st.number_input('Enter Moisture value : ', min_value=0.0, max_value=65.0, step=0.1)
CT = st.selectbox('Crop Type', ('Select', 'Maize', 'Sugarcane', 'Cotton', 'Tobacco', 'Paddy', 'Barley','Wheat', 'Millets', 'Oil seeds', 'Pulses', 'Ground Nuts'))
# st.button('Predict')

x = [[T, H, M, CT, N ,K, P]]
st.markdown(f'My Values are : {x}')

model = pickle.load(open('fertilizer.pkl', 'rb'))
cv = pickle.load(open('vector.pkl', 'rb'))

def main():
    if st.button('predict'):
        data = x
        pred = model.predict(data)
        st.markdown(f'Predicted Crop is : {pred}')

main()
co = st.text_input('Any Comment : ')
st.write(co)
st.write('Thank You !!')