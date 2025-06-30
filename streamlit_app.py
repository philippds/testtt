import streamlit as st
from collections import Counter

image_pairs = [
    ("https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/491445277_17875663539323055_2680152234481785204_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjExMjZ4MTQwOC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEsUWnLbeJ2XwSkvFKeAOevEpZFGmNj4mQF9cgka14PXK6acnadjpJ3FA6525ST-4Y&_nc_ohc=n8G9YrAupXMQ7kNvwHq9Col&_nc_gid=xGFCLiWne_jlIv85t2xs9g&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzYxOTU0NDg3OTkxMDE0ODQ0MQ%3D%3D.3-ccb7-5&oh=00_AfMOTki86trwG42JaBetkfJn5-IfsLKxC8yLleAcSSw-Pw&oe=68685FA3&_nc_sid=7a9f4b",
     "https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/491445277_17875663539323055_2680152234481785204_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjExMjZ4MTQwOC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEsUWnLbeJ2XwSkvFKeAOevEpZFGmNj4mQF9cgka14PXK6acnadjpJ3FA6525ST-4Y&_nc_ohc=n8G9YrAupXMQ7kNvwHq9Col&_nc_gid=xGFCLiWne_jlIv85t2xs9g&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzYxOTU0NDg3OTkxMDE0ODQ0MQ%3D%3D.3-ccb7-5&oh=00_AfMOTki86trwG42JaBetkfJn5-IfsLKxC8yLleAcSSw-Pw&oe=68685FA3&_nc_sid=7a9f4b"
    ),
    ("https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/491445277_17875663539323055_2680152234481785204_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjExMjZ4MTQwOC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEsUWnLbeJ2XwSkvFKeAOevEpZFGmNj4mQF9cgka14PXK6acnadjpJ3FA6525ST-4Y&_nc_ohc=n8G9YrAupXMQ7kNvwHq9Col&_nc_gid=xGFCLiWne_jlIv85t2xs9g&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzYxOTU0NDg3OTkxMDE0ODQ0MQ%3D%3D.3-ccb7-5&oh=00_AfMOTki86trwG42JaBetkfJn5-IfsLKxC8yLleAcSSw-Pw&oe=68685FA3&_nc_sid=7a9f4b",
     "https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/491445277_17875663539323055_2680152234481785204_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjExMjZ4MTQwOC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEsUWnLbeJ2XwSkvFKeAOevEpZFGmNj4mQF9cgka14PXK6acnadjpJ3FA6525ST-4Y&_nc_ohc=n8G9YrAupXMQ7kNvwHq9Col&_nc_gid=xGFCLiWne_jlIv85t2xs9g&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzYxOTU0NDg3OTkxMDE0ODQ0MQ%3D%3D.3-ccb7-5&oh=00_AfMOTki86trwG42JaBetkfJn5-IfsLKxC8yLleAcSSw-Pw&oe=68685FA3&_nc_sid=7a9f4b"
    ),
    ("https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/491445277_17875663539323055_2680152234481785204_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjExMjZ4MTQwOC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEsUWnLbeJ2XwSkvFKeAOevEpZFGmNj4mQF9cgka14PXK6acnadjpJ3FA6525ST-4Y&_nc_ohc=n8G9YrAupXMQ7kNvwHq9Col&_nc_gid=xGFCLiWne_jlIv85t2xs9g&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzYxOTU0NDg3OTkxMDE0ODQ0MQ%3D%3D.3-ccb7-5&oh=00_AfMOTki86trwG42JaBetkfJn5-IfsLKxC8yLleAcSSw-Pw&oe=68685FA3&_nc_sid=7a9f4b",
     "https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/491445277_17875663539323055_2680152234481785204_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjExMjZ4MTQwOC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_oc=Q6cZ2QEsUWnLbeJ2XwSkvFKeAOevEpZFGmNj4mQF9cgka14PXK6acnadjpJ3FA6525ST-4Y&_nc_ohc=n8G9YrAupXMQ7kNvwHq9Col&_nc_gid=xGFCLiWne_jlIv85t2xs9g&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MzYxOTU0NDg3OTkxMDE0ODQ0MQ%3D%3D.3-ccb7-5&oh=00_AfMOTki86trwG42JaBetkfJn5-IfsLKxC8yLleAcSSw-Pw&oe=68685FA3&_nc_sid=7a9f4b"
    )
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
