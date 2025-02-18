import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="2D Brownian Motion", page_icon="📈")
st.markdown("# 2D Brownian Motion")
st.sidebar.header("Simulation of a 2-dimensional Brownian Motion between 0 and 1")


# Number of steps
if 'N' not in st.session_state:
    st.session_state.N = 1000
N = st.session_state.N


# Function to generate 2D Brownian motion
def brownian_motion_2d(T, N):
    dt = T / N
    dW_x = np.sqrt(dt) * np.random.randn(N)
    dW_y = np.sqrt(dt) * np.random.randn(N)
    W_x = np.cumsum(dW_x)
    W_y = np.cumsum(dW_y)
    W_x = np.insert(W_x, 0, 0)  # Insert W_x(0) = 0 at the beginning
    W_y = np.insert(W_y, 0, 0)  # Insert W_y(0) = 0 at the beginning
    return W_x, W_y

# Generate 2D Brownian motion only once
if 'W_x' not in st.session_state or 'W_y' not in st.session_state:
    st.session_state.W_x, st.session_state.W_y = brownian_motion_2d(1, N)
W_x = st.session_state.W_x
W_y = st.session_state.W_y

def create_chart_2d(t, i, w_x, w_y):
    fig, ax = plt.subplots()
    ax.plot(w_x[:i], w_y[:i], label="2D Brownian Motion")
    ax.scatter(w_x[i-1], w_y[i-1], color='red')  # Mark the last point
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_xlabel("W_x(t)")
    ax.set_ylabel("W_y(t)")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().tick_params(axis='both', which='both', length=0)
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    st.pyplot(fig)

col1, col2 = st.columns([1, 3]) 
with col1:
    # Slider for time
    t = st.slider("Time", 0.0, 1.0, 1.0, 0.01)
    N = st.number_input("Number of steps", min_value=1, max_value=1001, value=1000, step=1)
    if st.session_state.get('N', N) != N:
        st.session_state.N = N
        st.session_state.W_x, st.session_state.W_y = brownian_motion_2d(1, N)
        W_x = st.session_state.W_x
        W_y = st.session_state.W_y
        st.rerun()
    if st.button("Simulate again"):
        st.session_state.W_x, st.session_state.W_y = brownian_motion_2d(1, N)
        W_x = st.session_state.W_x
        W_y = st.session_state.W_y
        st.rerun()

with col2:
    create_chart_2d(t, int(N * t) + 1, W_x, W_y)