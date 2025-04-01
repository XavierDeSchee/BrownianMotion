import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



def create_chart(t, i, w, maxy = 3, v=None):
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, t, i), w, label="Brownian Motion")
    if v is not None:
        ax.plot(np.linspace(0, t, i), v, label="Brownian Motion 2", color='lightblue')
    else:
        ax.fill_between(np.linspace(0, t, i), w, color='lightblue', alpha=0.5)
    ax.axvline(x=t, color='grey', linestyle='--', label=f"t = {t}")
    ax.set_xlim([0, 1])
    ax.set_ylim([-maxy, maxy])
    ax.set_xlabel("Time")
    ax.set_ylabel("W(t)")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().tick_params(axis='both', which='both', length=0)
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.7)
    st.pyplot(fig)