import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Diffusion processes")

st.sidebar.success("Select simulation above.")

st.markdown(
    """
    This app features charts of a symmetric random walk, a scaled
    symmetric random walk, and a Brownian motion, in order to illustrate
    the progression from the first to the last.
    
    ### Random walk

    A symmetric random walk $M_k , k = 0, 1, 2, . . .$ is defined as $M_0 = 0$ and 
    """
)

st.latex(r'''
    M_k = \sum\limits_{j=1}^k X_j, \hspace{0.5cm} k=1, 2, 3, ...
''')

st.markdown(
    """
    where $X$ represents the outcome of a coin toss which can either take 1 or -1 as a value,
    with equal probabilities. 

    ### Scaled random walk

    A scaled symmetric random walk is defined as
    """
)

st.latex(r'''
    W^{(n)}(t) = \frac{1}{\sqrt{n}}M_{nt} = \frac{1}{\sqrt{n}} \sum_{j=1}^{nt}X_j 
''')

st.markdown(
    """
    for a given $n$. 

   ### Brownian motion

   Brownian motion is defined as usual, see for example [here](https://en.wikipedia.org/wiki/Brownian_motion).
    
"""
)