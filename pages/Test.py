import streamlit as st

# Initialize session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append({'task': task, 'completed': False})
        st.session_state.new_task = ''

def delete_task(index):
    del st.session_state.tasks[index]

def toggle_task(index):
    st.session_state.tasks[index]['completed'] = not st.session_state.tasks[index]['completed']

st.title('Task List')

# Input field to add a new task
st.text_input('New Task', key='new_task')
st.button('Add Task', on_click=add_task)

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([1, 5, 1])
    col1.checkbox('', value=task['completed'], on_change=toggle_task, args=(i,))
    if task['completed']:
        col2.markdown(f"~~{task['task']}~~")
    else:
        col2.markdown(task['task'])
    col3.button('Delete', key=f'delete_{i}', on_click=delete_task, args=(i,))
