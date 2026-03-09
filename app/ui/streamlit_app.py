import os
import sys
import streamlit as st
import torch

# Fix Python import path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

# Import agents
from app.pipelines.ocr_pipeline import extract_text_from_image
from app.agents.parser_agent import parse_math_problem
from app.agents.router_agent import route_problem
from app.agents.solver_agent import solve_calculus
from app.agents.verifier_agent import verify_calculus_solution
from app.agents.explainer_agent import generate_explanation
from app.pipelines.rag_pipeline import retrieve_context


def run():

    st.title("AI Math Mentor")

    st.write("Solve math problems using AI")

    # GPU status
    if torch.cuda.is_available():
        st.success(f"GPU detected: {torch.cuda.get_device_name(0)}")
    else:
        st.warning("Running on CPU")

    mode = st.selectbox(
        "Select Input Mode",
        ["Text", "Image", "Audio"]
    )

    # ---------------- TEXT INPUT ----------------
    if mode == "Text":

        question = st.text_area("Enter math problem")

        if st.button("Solve Problem"):

            parsed = parse_math_problem(question)

            st.subheader("Parsed Problem")
            st.json(parsed)

            route = route_problem(parsed)

            st.subheader("Router Decision")
            st.json(route)

            context = retrieve_context(parsed["problem_text"])

            st.subheader("Retrieved Knowledge")

            if len(context) == 0:
                st.warning("No knowledge retrieved")

            for doc in context:
                st.write(doc)

            if route["route"] == "calculus_solver":

                solution = solve_calculus(parsed["problem_text"])

                st.subheader("Solver Output")
                st.json(solution)

                verification = verify_calculus_solution(
                    solution["expression"],
                    solution["derivative"]
                )

                st.subheader("Verifier Result")
                st.json(verification)

                explanation = generate_explanation(
                    parsed["problem_text"],
                    solution["derivative"]
                )

                st.subheader("Step-by-Step Explanation")

                for step in explanation:
                    st.write(step)

    # ---------------- IMAGE INPUT ----------------
    elif mode == "Image":

        image = st.file_uploader(
            "Upload math problem image",
            type=["png", "jpg", "jpeg"]
        )

        if image is not None:

            st.image(image, caption="Uploaded Image", width=500)

            if st.button("Extract Text"):

                with st.spinner("Running OCR..."):

                    extracted_text = extract_text_from_image(image)

                st.session_state["ocr_text"] = extracted_text

        # Show editable OCR text
        if "ocr_text" in st.session_state:

            edited_text = st.text_area(
                "Edit text if OCR missed something",
                st.session_state["ocr_text"],
                height=150
            )

            if st.button("Solve OCR Problem"):

                parsed = parse_math_problem(edited_text)

                st.subheader("Parsed Problem")
                st.json(parsed)

                route = route_problem(parsed)

                st.subheader("Router Decision")
                st.json(route)

                context = retrieve_context(parsed["problem_text"])

                st.subheader("Retrieved Knowledge")

                if len(context) == 0:
                    st.warning("No knowledge retrieved")

                for doc in context:
                    st.write(doc)

                if route["route"] == "calculus_solver":

                    solution = solve_calculus(parsed["problem_text"])

                    st.subheader("Solver Output")
                    st.json(solution)

                    verification = verify_calculus_solution(
                        solution["expression"],
                        solution["derivative"]
                    )

                    st.subheader("Verifier Result")
                    st.json(verification)

                    explanation = generate_explanation(
                        parsed["problem_text"],
                        solution["derivative"]
                    )

                    st.subheader("Step-by-Step Explanation")

                    for step in explanation:
                        st.write(step)

    # ---------------- AUDIO INPUT ----------------
    elif mode == "Audio":

        audio = st.file_uploader(
            "Upload audio question",
            type=["wav", "mp3"]
        )

        if audio is not None:
            st.write("Audio uploaded successfully (Speech-to-text coming next)")


if __name__ == "__main__":
    run()