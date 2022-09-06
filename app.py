import pickle
import streamlit as st

model = pickle.load(open('/home/sharon/Documents/Desktop/final year project folder/model/sarima_original.pkl', 'rb'))

def main():
    st.title('water prediction')

#input variable
Timestamp = st.text_input('Timestamp')

#prediction code
if st.button('predict'):
   makeprediction = model.forecast([[Timestamp]])
   output = round(makeprediction[0],4)
   st.success('your water prediction is {}'.format(output))
   
   
if __name__=='__main__':
    main()