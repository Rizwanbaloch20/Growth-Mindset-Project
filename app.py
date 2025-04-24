import streamlit as st 

st.set_page_config(page_title="Growth Mindset App", page_icon=":🧠:", layout="wide")
st.title("Growth Mindset AI Project ")
st.header(" 🚀Welcome to the Growth Mindset AI Project")

st.write("This is a web application that uses AI to help you develop a growth mindset.")
st.header("Todays Growth Mindset Quote")
st.write("“The only limit to our realization of tomorrow will be our doubts of today.” - Franklin D. Roosevelt")
st.header("What is Your chellange today ?")
user_input = st.text_input(" Describe You are Facing  challenge:")
if user_input:
    st.success(f"Thank you for sharing your challeng: {user_input}. keep pushing forward!")
else:
    st.warning("Please enter your challenge to get started!")

st.header("Reflect on Your Learning?")
reflection_input = st.text_area("Write Your Reflect?")
if reflection_input:
    st.success(f" 😃💖Thank you for sharing your reflection: {reflection_input}. Keep reflecting and growing!")
else:
    st.info("Please enter your reflection on past experince to grow! share your deficulties ")


st.header("🥇Celibrate Your Win!?")
acheivement = st.text_input("Write Your Achievement?")


if acheivement:
    st.success(f"🎉Congratulations on your achievement: {acheivement}! Celebrate your success!")

else:
    st.info("Please share your  achievement here  to celebrate your success!")

st.write("--------")
st.write ("keep blieving in yourself and your ability to grow!")
st.write("Created By Rizwan Ahmed !")