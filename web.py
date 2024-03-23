import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

completed_todos = []

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=str(index))
    if checkbox:
        completed_todos.append(index)
        if str(index) in st.session_state:
            del st.session_state[str(index)]

for index in completed_todos[::-1]:
    todos.pop(index)

if completed_todos:
    function.write_todos(todos)

st.text_input(label = "Enter a todo task: ", placeholder="Add a new entry.",
              on_change=add_todo, key='new_todo')

#st.session_state
#completed_todos