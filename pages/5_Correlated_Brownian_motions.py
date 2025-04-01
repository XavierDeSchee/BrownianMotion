import streamlit as st
import numpy as np
from charting import create_chart

st.set_page_config(page_title="Correlated Brownian Motions", page_icon="📈")
st.markdown("# Correlated Brownian Motions")
st.sidebar.header("Simulation of two correlated Brownian Motions between 0 and 1")

# Function to generate Brownian motion
def brownian_motion(T, N):
    dt = T / N
    dW = np.sqrt(dt) * np.random.randn(N)
    W = np.cumsum(dW)
    W = np.insert(W, 0, 0)  # Insert W(0) = 0 at the beginning
    return W

# Number of steps
if 'N' not in st.session_state:
    st.session_state.N = 1000
N = st.session_state.N

# Correlation
if 'rho' not in st.session_state:
    st.session_state.rho = 0.8
rho = st.session_state.rho


def generate_brownian_motion(N, rho):
    w1 = brownian_motion(1, N)
    w2 = brownian_motion(1, N)
    w3 = rho * w1 + np.sqrt(1 - rho**2) * w2  # Correlated Brownian motion
    return w1, w3

# Generate Brownian motion only once
if 'W' not in st.session_state:
    st.session_state.W, st.session_state.V = generate_brownian_motion(N, rho)
    # st.session_state.W = brownian_motion(1, N)
    # st.session_state.V = brownian_motion(1, N)

W = st.session_state.W
V = st.session_state.V

# Create two columns: one for the slider and one for the chart

col1, col2 = st.columns([1, 3]) 

with col1:
    # Slider for time
    t = st.slider("Time", 0.0, 1.0, 1.0, 0.01)
    rho = st.slider("Correlation", 0.0, 1.0, 0.8, 0.01)
    N = st.number_input("Number of steps", min_value=1, max_value=1001, value=1000, step=1)
    if st.session_state.get('N', N) != N:
        st.session_state.N = N
        st.session_state.W, st.session_state.V = generate_brownian_motion(N, rho)
        # st.session_state.W = brownian_motion(1, N)
        # st.session_state.V = brownian_motion(1, N)
        W = st.session_state.W
        V = st.session_state.V
        st.rerun()
    if st.session_state.get('rho', rho) != rho:
        st.session_state.rho = rho
        st.session_state.W, st.session_state.V = generate_brownian_motion(N, rho)
        # st.session_state.W = brownian_motion(1, N)
        # st.session_state.V = brownian_motion(1, N)
        W = st.session_state.W
        V = st.session_state.V
        st.rerun()
    if st.button("Simulate again"):
        st.session_state.W, st.session_state.V = generate_brownian_motion(N, rho)
        # st.session_state.W = brownian_motion(1, N)
        # st.session_state.V = brownian_motion(1, N)
        W = st.session_state.W
        V = st.session_state.V
        st.rerun()

with col2:
    create_chart(t, int(N * t) + 1, W[:int(N * t) + 1], v= V[:int(N * t) + 1])

