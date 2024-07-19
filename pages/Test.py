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

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 2em;
        color: #333333;
        text-align: center;
        margin-bottom: 20px;
    }
    .task-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .task-completed {
        text-decoration: line-through;
        color: #888888;
    }
    .task {
        flex-grow: 1;
        margin-left: 10px;
    }
    .delete-button {
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .delete-button:hover {
        background-color: #ff0000;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title">Task List</h1>', unsafe_allow_html=True)

# Input field to add a new task
st.text_input('New Task', key='new_task')
st.button('Add Task', on_click=add_task)

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    task_class = 'task-completed' if task['completed'] else 'task'
    task_html = f"""
    <div class="task-container">
        <input type="checkbox" {'checked' if task['completed'] else ''} onclick="window.location.href='?toggle={i}'">
        <div class="{task_class}">{task['task']}</div>
        <button class="delete-button" onclick="window.location.href='?delete={i}'">Delete</button>
    </div>
    """
    st.markdown(task_html, unsafe_allow_html=True)

# JavaScript for handling checkbox and delete button actions
st.markdown("""
    <script>
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const toggle = urlParams.get('toggle');
    const del = urlParams.get('delete');

    if (toggle !== null) {
        fetch(`/toggle_task?index=${toggle}`);
        window.location.href = window.location.href.split('?')[0];
    }

    if (del !== null) {
        fetch(`/delete_task?index=${del}`);
        window.location.href = window.location.href.split('?')[0];
    }
    </script>
    """, unsafe_allow_html=True)

def toggle_task_endpoint(index):
    index = int(index)
    toggle_task(index)

def delete_task_endpoint(index):
    index = int(index)
    delete_task(index)

st.experimental_get_query_params()

st.experimental_set_query_params(toggle_task=toggle_task_endpoint, delete_task=delete_task_endpoint)
