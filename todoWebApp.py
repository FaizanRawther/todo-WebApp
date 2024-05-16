import streamlit as st
import functions as fc
todos=fc.read_todos()
st.title("My todo webapp")
st.subheader("Lists")
st.write("This app is makes your productivity")
st.text_input(label="Enter a todo:  ",placeholder="Add a todo")
st.checkbox("Buy grocery")

for todo in todos:
    st.checkbox(todo)

