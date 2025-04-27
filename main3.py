import streamlit as st

st.title("Chai Taste poll")

col1, col2 =st.columns(2)

with col1:
  st.header("Masala Chai")
  st.image("https://masalaandchai.com/wp-content/uploads/2021/07/Masala-Chai-Featured.jpg", width=200)
  vote1 = st.button("Vote Masala Chai")
  
with col2:
  st.header("Adrak Chai")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRVponKrEcjd0HTGdOeWlFmY63qJi-FSKhYA&s", width=200)
  vote2 = st.button("Vote Adrak Chai")


if vote1:
  st.success("Thanks for voting masala chai")
elif vote2:
  st.success("Thanks for voting adrak chai")
  
name =st.sidebar.text_input("Enter your name")
tea =st.sidebar.selectbox("Choose your chai",["Masala","Kesar","Adrak"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.markdown("""
    - **1.** Boil the water and add tea leaves
    - **2.** Add sugar and masala
    - **3.** Add milk and boil
    - **4.** Strain and serve hot
    """)
