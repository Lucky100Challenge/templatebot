import streamlit as st

# Initialize session state to store tasks, points, and level
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'previous_level' not in st.session_state:
    st.session_state.previous_level = 1

def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append({'task': task, 'completed': False})
        st.session_state.new_task = ''

def delete_task(index):
    del st.session_state.tasks[index]

def toggle_task(index):
    task = st.session_state.tasks[index]
    if not task['completed']:
        st.session_state.points += 10
        task['completed'] = True
    else:
        st.session_state.points -= 10
        task['completed'] = False
    update_level()

def update_level():
    st.session_state.level = st.session_state.points // 100 + 1
    if st.session_state.level > st.session_state.previous_level:
        st.balloons()
        st.session_state.previous_level = st.session_state.level

st.title('Gamified Task List')

# Display points and level
st.markdown(f"**Points**: {st.session_state.points}")
st.markdown(f"**Level**: {st.session_state.level}")

# Input field to add a new task
st.text_input('New Task', key='new_task')
st.button('Add Task', on_click=add_task)

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([1, 5, 1])
    col1.checkbox('', value=task['completed'], on_change=toggle_task, args=(i,), key=f'checkbox_{i}')
    if task['completed']:
        col2.markdown(f"~~{task['task']}~~")
    else:
        col2.markdown(task['task'])
    col3.button('Delete', key=f'delete_{i}', on_click=delete_task, args=(i,))

# Add a progress bar to show the points progress towards the next level
st.progress(st.session_state.points % 100 / 100)
