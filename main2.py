import streamlit as st   

st.title("Tea Maker App")

if st.button("Make Tea"):
  st.success("Tea is being made!")
  
add_masala = st.checkbox("Add Masala")


if add_masala:
  st.write("Masala is added to your Tea")
 
tea_type = st.radio("Pick your Tea type",["Black Tea","Green Tea", "Herbal Tea"])
st.write(f"{tea_type} is aded")

flavour = st.selectbox("Choose flavour:",["Mint","Lemon","Ginger"])
st.write(f"Selected flavour {flavour}" )

sugar = st.slider("Sugar Level(spoon)", 0, 5 ,2)
st.write(f"Selected sugar level is {sugar}")

cups = st.number_input("How many cup", min_value=1,max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

name=st.text_input("Enter your name")
if name:
  st.write(f"Welcome, {name}! your Tea is on the way")
  
dob=st.date_input("Enter your date of birth")
st.write(f"Your date of birth is {dob}")