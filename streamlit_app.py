import streamlit as st
from collections import Counter

st.title("Image Pair Chooser")

st.markdown("""
Welcome to the Image Pair Chooser! In this app, you will see pairs of images side by side after you click **Start**. 
Your task is to select which image you prefer from each pair. After you have finished viewing all pairs, you will see a summary chart showing which images were chosen most often. Feel free to restart at any time.
""")

image_pairs = [
    ("https://www.pedigree.in/files/styles/webp/public/2023-09/Puppy-Nutrition-Image-list.png.webp", "https://img.joomcdn.net/715c960d40c12669b2038bf00cd139b564c7548b_original.jpeg"),
    ("https://www.pedigree.in/files/styles/webp/public/2023-09/Puppy-Nutrition-Image-list.png.webp", "https://img.joomcdn.net/715c960d40c12669b2038bf00cd139b564c7548b_original.jpeg"),
    ("https://www.pedigree.in/files/styles/webp/public/2023-09/Puppy-Nutrition-Image-list.png.webp", "https://img.joomcdn.net/715c960d40c12669b2038bf00cd139b564c7548b_original.jpeg")
]

if "pair_counter" not in st.session_state:
    st.session_state.pair_counter = 0
if "choices" not in st.session_state:
    st.session_state.choices = []
if "started" not in st.session_state:
    st.session_state.started = False

total_pairs = len(image_pairs)
choices_made = st.session_state.pair_counter
choices_remaining = total_pairs - st.session_state.pair_counter

if not st.session_state.started:
    if st.button("Start"):
        st.session_state.started = True
else:
    st.progress(choices_made / total_pairs)
    st.write(f"You have made {choices_made} choices so far.")
    st.write(f"You have {choices_remaining} pairs left to view.")

    if st.button("Start Over"):
        st.session_state.clear()
        st.session_state.pair_counter = 0
        st.session_state.choices = []
        st.session_state.started = False

    if st.session_state.pair_counter < total_pairs:
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
        st.write(f"Total choices made: {choices_made}")
