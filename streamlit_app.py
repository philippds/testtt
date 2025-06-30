import streamlit as st
from collections import Counter

# define explicit pairs
image_pairs = [
    ("https://placekitten.com/200/300", "https://placebear.com/200/300"),
    ("https://placekitten.com/210/300", "https://placebear.com/210/300"),
    ("https://placekitten.com/220/300", "https://placebear.com/220/300")
]

if "pair_counter" not in st.session_state:
    st.session_state.pair_counter = 0
if "choices" not in st.session_state:
    st.session_state.choices = []

st.title("Image Pair Chooser")

st.progress(st.session_state.pair_counter / len(image_pairs))

if st.button("Start Over"):
    st.session_state.pair_counter = 0
    st.session_state.choices = []
    st.experimental_rerun()

if st.session_state.pair_counter < len(image_pairs):
    img1, img2 = image_pairs[st.session_state.pair_counter]

    col1, col2 = st.columns(2)
    with col1:
        st.image(img1, use_container_width=True)
        if st.button("Select left image"):
            st.session_state.choices.append(img1)
            st.session_state.pair_counter += 1

    with col2:
        st.image(img2, use_container_width=True)
        if st.button("Select right image"):
            st.session_state.choices.append(img2)
            st.session_state.pair_counter += 1
else:
    st.write("## Results after viewing pairs")
    scores = Counter(st.session_state.choices)
    st.bar_chart(scores)
    if st.button("Restart"):
        st.session_state.pair_counter = 0
        st.session_state.choices = []
        st.experimental_rerun()
