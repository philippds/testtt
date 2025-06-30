import streamlit as st
from collections import Counter

image_pairs = [
    ("https://www.instagram.com/p/CxyzImage1/media/?size=l", "https://www.instagram.com/p/CabcImage2/media/?size=l"),
    ("https://www.instagram.com/p/CdefImage3/media/?size=l", "https://www.instagram.com/p/CghiImage4/media/?size=l"),
    ("https://www.instagram.com/p/CjklImage5/media/?size=l", "https://www.instagram.com/p/CmnoImage6/media/?size=l")
]

if "pair_counter" not in st.session_state:
    st.session_state.pair_counter = 0
if "choices" not in st.session_state:
    st.session_state.choices = []

st.title("Image Pair Chooser")

st.progress(st.session_state.pair_counter / len(image_pairs))

if st.button("Start Over"):
    st.session_state.clear()
    st.session_state.pair_counter = 0
    st.session_state.choices = []

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
        st.session_state.clear()
        st.session_state.pair_counter = 0
        st.session_state.choices = []
