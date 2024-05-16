import streamlit as st
import functions as fc
todos=fc.read_todos()
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_todos(todos)

st.title("My todo webapp")
st.subheader("Lists")
st.write("This app is makes your productivity")
st.text_input(label="Enter a todo:  ",placeholder="Add a todo",on_change=add_todo,key="new_todo")

for index,todo in enumerate(todos):
    check_box=st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        fc.write_todos(todos)
        del st.session_state[todo]
        st.rerun
st.session_state

