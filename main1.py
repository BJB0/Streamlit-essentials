import streamlit as st


st.title("Bjb Streamlit App")
st.subheader("Brewed with Streamlit")
st.text("Welcome to the very first interactive App")
st.write("This is a simple streamlit app that demonstrates the use of streamlit.")

bjb = st.selectbox("Your fav programming language:", ["C++", "python", "javascript", "C","Java"])

st.write(f"You chose {bjb}.Excellent choice!")

st.success("your app is running successfully")