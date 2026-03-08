import os
import sys
import streamlit as st

# Fix module import path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)


def run():

    st.title("AI Math Mentor")
    st.write("Solve math problems using AI")

    mode = st.selectbox(
        "Select Input Mode",
        ["Text", "Image", "Audio"]
    )

    # TEXT INPUT
    if mode == "Text":

        question = st.text_area("Enter math problem")

        if st.button("Solve"):
            st.write(question)

    # IMAGE INPUT
    elif mode == "Image":

        image = st.file_uploader(
            "Upload math problem image",
            type=["png", "jpg", "jpeg"]
        )

        if image is not None:

            st.image(image, caption="Uploaded Image", width=500)

            if st.button("Extract Text"):

                with st.spinner("Running OCR..."):

                    from app.pipelines.ocr_pipeline import extract_text_from_image

                    extracted_text = extract_text_from_image(image)

                st.subheader("Extracted Text")

                st.text_area(
                    "Edit if needed",
                    extracted_text,
                    height=150
                )

    # AUDIO INPUT
    elif mode == "Audio":

        audio = st.file_uploader(
            "Upload audio",
            type=["wav", "mp3"]
        )

        if audio is not None:
            st.write("Audio uploaded")


if __name__ == "__main__":
    run()