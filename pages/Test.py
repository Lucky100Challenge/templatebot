import streamlit as st

# Initialize session state to store tasks, points, level, and balloons
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'balloons' not in st.session_state:
    st.session_state.balloons = False

def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append({'task': task, 'completed': False})
        st.session_state.new_task = ''

def delete_task(index):
    if index < len(st.session_state.tasks):
        if st.session_state.tasks[index]['completed']:
            st.session_state.points -= 10
        del st.session_state.tasks[index]
        update_level()

def toggle_task(index):
    if index < len(st.session_state.tasks):
        task = st.session_state.tasks[index]
        if not task['completed']:
            st.session_state.points += 10
        else:
            st.session_state.points -= 10
        task['completed'] = not task['completed']
        update_level()

def update_level():
    new_level = st.session_state.points // 100 + 1
    if new_level > st.session_state.level:
        st.session_state.balloons = True
    st.session_state.level = new_level

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

# Falling balloons effect
if st.session_state.balloons:
    st.session_state.balloons = False
    st.markdown(
        """
        <style>
        .balloons {
            position: fixed;
            top: -50px;
            width: 100%;
            height: 100%;
            z-index: 9999;
            overflow: hidden;
        }
        .balloon {
            position: absolute;
            bottom: -150px;
            width: 50px;
            height: 70px;
            background-color: #FF5E7D;
            border-radius: 50%;
            opacity: 0.7;
            animation: rise 4s ease-in infinite;
        }
        .balloon::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            width: 2px;
            height: 20px;
            background-color: #FF5E7D;
        }
        @keyframes rise {
            0% {
                transform: translateY(0) translateX(0);
                opacity: 0.7;
            }
            100% {
                transform: translateY(-110vh) translateX(calc(100vw * 1.2 - 50px));
                opacity: 0.3;
            }
        }
        </style>
        <div class="balloons">
            <div class="balloon" style="left: 10%; animation-delay: 0s;"></div>
            <div class="balloon" style="left: 20%; animation-delay: 1s;"></div>
            <div class="balloon" style="left: 30%; animation-delay: 2s;"></div>
            <div class="balloon" style="left: 40%; animation-delay: 3s;"></div>
            <div class="balloon" style="left: 50%; animation-delay: 4s;"></div>
            <div class="balloon" style="left: 60%; animation-delay: 5s;"></div>
            <div class="balloon" style="left: 70%; animation-delay: 6s;"></div>
            <div class="balloon" style="left: 80%; animation-delay: 7s;"></div>
            <div class="balloon" style="left: 90%; animation-delay: 8s;"></div>
        </div>
        """, unsafe_allow_html=True
    )
