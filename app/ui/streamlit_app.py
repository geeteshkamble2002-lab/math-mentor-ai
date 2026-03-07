import streamlit as st

def run():
    st.title("AI Math Mentor")

    st.write("Solve math problems using AI")

    mode = st.selectbox(
        "Select Input Mode",
        ["Text", "Image", "Audio"]
    )

    if mode == "Text":
        question = st.text_area("Enter math problem")

    elif mode == "Image":
        image = st.file_uploader("Upload image", type=["png", "jpg"])

    elif mode == "Audio":
        audio = st.file_uploader("Upload audio", type=["wav", "mp3"])

    st.button("Solve")

if __name__ == "__main__":
    run()