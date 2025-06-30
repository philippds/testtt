import streamlit as st
import random
from collections import Counter

all_images = [
    "https://placekitten.com/200/300",
    "https://placebear.com/200/300",
    "https://placekitten.com/210/300",
    "https://placebear.com/210/300"
]

if "pair_counter" not in st.session_state:
    st.session_state.pair_counter = 0
if "shown_pairs" not in st.session_state:
    st.session_state.shown_pairs = []
if "choices" not in st.session_state:
    st.session_state.choices = []

st.title("Image Pair Chooser")

def advance_state():
    st.session_state.pair_counter += 1

def reset_state():
    st.session_state.pair_counter = 0
    st.session_state.shown_pairs = []
    st.session_state.choices = []

if st.session_state.pair_counter < 10:
    while True:
        img1, img2 = random.sample(all_images, 2)
        if (img1, img2) not in st.session_state.shown_pairs and (img2, img1) not in st.session_state.shown_pairs:
            st.session_state.shown_pairs.append((img1, img2))
            break

    col1, col2 = st.columns(2)
    with col1:
        st.image(img1, use_container_width=True)
        if st.button("Select left image"):
            st.session_state.choices.append(img1)
            advance_state()

    with col2:
        st.image(img2, use_container_width=True)
        if st.button("Select right image"):
            st.session_state.choices.append(img2)
            advance_state()
else:
    st.write("## Results after 10 pairs")
    scores = Counter(st.session_state.choices)
    st.bar_chart(scores)
    if st.button("Restart"):
        reset_state()
