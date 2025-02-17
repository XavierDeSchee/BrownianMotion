import streamlit as st
import numpy as np
from charting import create_chart

# Multi page config
st.set_page_config(page_title="Scaled random walk", page_icon="📈")
st.markdown("# Scaled random walk")
st.sidebar.header("Simulation of a symmetric scaled random walk between 0 and 1")

# Function to generate Brownian motion
def scaled_random_walk(T, N):
    dt = T / N
    dW = np.random.choice([-1, 1], size=N) / np.sqrt(N)
    W = np.cumsum(dW)
    W = np.insert(W, 0, 0)  # Insert W(0) = 0 at the beginning
    return W

# Number of steps
if 'N' not in st.session_state:
    st.session_state.N = 100
N = st.session_state.N

# Generate Brownian motion only once
if 'W' not in st.session_state:
    st.session_state.W = scaled_random_walk(1, N)
W = st.session_state.W

# Create two columns: one for the slider and one for the chart

col1, col2 = st.columns([1, 3]) 

with col1:
    # Slider for time
    t = st.slider("Time", 0.0, 1.0, 1.0, 0.01)
    N = st.selectbox("Number of steps", options=[10, 100, 1000], index=1)
    if st.session_state.get('N', N) != N:
        st.session_state.N = N
        st.session_state.W = scaled_random_walk(1, N)
        W = st.session_state.W
        st.rerun()
    if st.button("Simulate again"):
        st.session_state.W = scaled_random_walk(1, N)
        W = st.session_state.W
        st.rerun()

with col2:
    create_chart(t, int(N * t) + 1, W[:int(N * t) + 1])

