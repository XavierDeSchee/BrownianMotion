import streamlit as st
import numpy as np
from charting import create_chart

# Multi page config
st.set_page_config(page_title="Random walk", page_icon="📈")
st.markdown("# Random walk")
st.sidebar.header("Simulation of a symmetric random walk between 0 and 1")

# Function to generate Brownian motion
def random_walk(T, N):
    dt = T / N
    dW = np.random.choice([-1, 1], size=N)
    W = np.cumsum(dW)
    W = np.insert(W, 0, 0)  # Insert W(0) = 0 at the beginning
    return W

# Number of steps
N = 10

# Generate Brownian motion only once
if 'W' not in st.session_state:
    st.session_state.W = random_walk(1, N)
W = st.session_state.W

# Create two columns: one for the slider and one for the chart

col1, col2 = st.columns([1, 3]) 

with col1:
    # Slider for time
    t = st.slider("Time", 0.0, 1.0, 1.0, 0.01)
    if st.button("Simulate again"):
        st.session_state.W = random_walk(1, N)
        W = st.session_state.W
        st.rerun()

with col2:
    create_chart(t, int(N * t) + 1, W[:int(N * t) + 1])

