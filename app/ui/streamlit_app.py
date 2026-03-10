# # # import os
# # # import sys
# # # import streamlit as st
# # # import torch

# # # # Fix Python import path
# # # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# # # if project_root not in sys.path:
# # #     sys.path.append(project_root)

# # # # Import agents
# # # from app.pipelines.ocr_pipeline import extract_text_from_image
# # # from app.agents.parser_agent import parse_math_problem
# # # from app.agents.router_agent import route_problem
# # # from app.agents.solver_agent import solve_calculus
# # # from app.agents.verifier_agent import verify_calculus_solution
# # # from app.agents.explainer_agent import generate_explanation
# # # from app.pipelines.rag_pipeline import retrieve_context
# # # from app.memory.memory_store import search_memory, save_memory


# # # def run():

# # #     st.title("AI Math Mentor")

# # #     st.write("Solve math problems using AI")

# # #     # GPU status
# # #     if torch.cuda.is_available():
# # #         st.success(f"GPU detected: {torch.cuda.get_device_name(0)}")
# # #     else:
# # #         st.warning("Running on CPU")

# # #     mode = st.selectbox(
# # #         "Select Input Mode",
# # #         ["Text", "Image", "Audio"]
# # #     )

# # #     # ---------------- TEXT INPUT ----------------
# # #     if mode == "Text":

# # #         question = st.text_area("Enter math problem")

# # #         if st.button("Solve Problem"):

# # #             parsed = parse_math_problem(question)

# # #             st.subheader("Parsed Problem")
# # #             st.json(parsed)

# # #             route = route_problem(parsed)

# # #             st.subheader("Router Decision")
# # #             st.json(route)

# # #             context = retrieve_context(parsed["problem_text"])

# # #             st.subheader("Retrieved Knowledge")

# # #             if len(context) == 0:
# # #                 st.warning("No knowledge retrieved")

# # #             for doc in context:
# # #                 st.write(doc)

# # #             if route["route"] == "calculus_solver":

# # #                 memory_result = search_memory(parsed["problem_text"])

# # #                 if memory_result:
# # #                     st.subheader("Memory Hit")
# # #                     st.json(memory_result)
# # #                 else:

# # #                     # Run solver
# # #                     solution = solve_calculus(parsed["problem_text"])

# # #                     st.subheader("Solver Output")
# # #                     st.json(solution)

# # #                     verification = verify_calculus_solution(
# # #                         solution["expression"],
# # #                         solution["derivative"]
# # #                     )

# # #                     st.subheader("Verifier Result")
# # #                     st.json(verification)

# # #                     explanation = generate_explanation(
# # #                         parsed["problem_text"],
# # #                         solution["derivative"]
# # #                     )

# # #                     st.subheader("Step-by-Step Explanation")

# # #                     for step in explanation:
# # #                         st.write(step)

# # #                     # Save to memory
# # #                     memory_entry = {
# # #                         "question": parsed["problem_text"],
# # #                         "topic": parsed["topic"],
# # #                         "solution": solution["derivative"],
# # #                         "verified": verification["verified"]
# # #                     }

# # #                     save_memory(memory_entry)

# # #     # ---------------- IMAGE INPUT ----------------
# # #     elif mode == "Image":

# # #         image = st.file_uploader(
# # #             "Upload math problem image",
# # #             type=["png", "jpg", "jpeg"]
# # #         )

# # #         if image is not None:

# # #             st.image(image, caption="Uploaded Image", width=500)

# # #             if st.button("Extract Text"):

# # #                 with st.spinner("Running OCR..."):

# # #                     extracted_text = extract_text_from_image(image)

# # #                 st.session_state["ocr_text"] = extracted_text

# # #         # Show editable OCR text
# # #         if "ocr_text" in st.session_state:

# # #             edited_text = st.text_area(
# # #                 "Edit text if OCR missed something",
# # #                 st.session_state["ocr_text"],
# # #                 height=150
# # #             )

# # #             if st.button("Solve OCR Problem"):

# # #                 parsed = parse_math_problem(edited_text)

# # #                 st.subheader("Parsed Problem")
# # #                 st.json(parsed)

# # #                 route = route_problem(parsed)

# # #                 st.subheader("Router Decision")
# # #                 st.json(route)

# # #                 context = retrieve_context(parsed["problem_text"])

# # #                 st.subheader("Retrieved Knowledge")

# # #                 if len(context) == 0:
# # #                     st.warning("No knowledge retrieved")

# # #                 for doc in context:
# # #                     st.write(doc)

# # #                 if route["route"] == "calculus_solver":

# # #                     memory_result = search_memory(parsed["problem_text"])

# # #                     if memory_result:
# # #                         st.subheader("Memory Hit")
# # #                         st.json(memory_result)
# # #                     else:

# # #                         # Run solver
# # #                         solution = solve_calculus(parsed["problem_text"])

# # #                         st.subheader("Solver Output")
# # #                         st.json(solution)

# # #                         verification = verify_calculus_solution(
# # #                             solution["expression"],
# # #                             solution["derivative"]
# # #                         )

# # #                         st.subheader("Verifier Result")
# # #                         st.json(verification)

# # #                         explanation = generate_explanation(
# # #                             parsed["problem_text"],
# # #                             solution["derivative"]
# # #                         )

# # #                         st.subheader("Step-by-Step Explanation")

# # #                         for step in explanation:
# # #                             st.write(step)

# # #                         # Save to memory
# # #                         memory_entry = {
# # #                             "question": parsed["problem_text"],
# # #                             "topic": parsed["topic"],
# # #                             "solution": solution["derivative"],
# # #                             "verified": verification["verified"]
# # #                         }

# # #                         save_memory(memory_entry)

# # #     # ---------------- AUDIO INPUT ----------------
# # #     elif mode == "Audio":

# # #         audio = st.file_uploader(
# # #             "Upload audio question",
# # #             type=["wav", "mp3"]
# # #         )

# # #         if audio is not None:
# # #             st.write("Audio uploaded successfully (Speech-to-text coming next)")


# # # if __name__ == "__main__":
# # #     run()


# # import os
# # import sys
# # import streamlit as st
# # import torch

# # # Fix import path
# # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# # if project_root not in sys.path:
# #     sys.path.append(project_root)

# # # Pipelines
# # from app.pipelines.ocr_pipeline import extract_text_from_image
# # from app.pipelines.speech_pipeline import transcribe_audio
# # from app.pipelines.rag_pipeline import retrieve_context

# # # Agents
# # from app.agents.parser_agent import parse_math_problem
# # from app.agents.router_agent import route_problem
# # from app.agents.solver_agent import solve_calculus
# # from app.agents.verifier_agent import verify_calculus_solution
# # from app.agents.explainer_agent import generate_explanation

# # # Memory
# # from app.memory.memory_store import search_memory, save_memory


# # def run_pipeline(question):

# #     if not question.strip():
# #         st.warning("Please enter a math problem")
# #         return

# #     # Parser
# #     parsed = parse_math_problem(question)

# #     st.subheader("Parsed Problem")
# #     st.json(parsed)

# #     # Router
# #     route = route_problem(parsed)

# #     st.subheader("Router Decision")
# #     st.json(route)

# #     # Memory Check
# #     memory = search_memory(parsed["problem_text"])

# #     if memory:

# #         st.subheader("Memory Hit")
# #         st.json(memory)
# #         return

# #     # RAG Retrieval
# #     context = retrieve_context(parsed["problem_text"])

# #     st.subheader("Retrieved Knowledge")

# #     if context:
# #         for doc in context:
# #             st.write(doc)
# #     else:
# #         st.write("No knowledge retrieved.")

# #     # Solver
# #     solution = solve_calculus(parsed["problem_text"])

# #     st.subheader("Solver Output")
# #     st.json(solution)

# #     # Verifier
# #     verification = verify_calculus_solution(
# #         solution["expression"],
# #         solution["derivative"]
# #     )

# #     st.subheader("Verifier Result")
# #     st.json(verification)

# #     # Explanation
# #     explanation = generate_explanation(
# #         parsed["problem_text"],
# #         solution["derivative"]
# #     )

# #     st.subheader("Step-by-Step Explanation")

# #     for step in explanation:
# #         st.write(step)

# #     # Save Memory
# #     save_memory({
# #         "question": parsed["problem_text"],
# #         "topic": parsed["topic"],
# #         "solution": solution["derivative"],
# #         "verified": verification["verified"]
# #     })

# #     st.success("Stored in memory")


# # def main():

# #     st.title("AI Math Mentor")

# #     st.write("Solve math problems using AI")

# #     # GPU detection
# #     if torch.cuda.is_available():
# #         st.success(f"GPU detected: {torch.cuda.get_device_name(0)}")
# #     else:
# #         st.warning("Running on CPU")

# #     mode = st.selectbox(
# #         "Select Input Mode",
# #         ["Text", "Image", "Audio"]
# #     )

# #     question = ""

# #     # TEXT MODE
# #     if mode == "Text":

# #         question = st.text_area("Enter math problem")

# #     # IMAGE MODE
# #     elif mode == "Image":

# #         image = st.file_uploader(
# #             "Upload math problem image",
# #             type=["png", "jpg", "jpeg"]
# #         )

# #         if image:

# #             st.image(image)

# #             if st.button("Extract Text"):

# #                 text = extract_text_from_image(image)

# #                 st.session_state["ocr_text"] = text

# #         if "ocr_text" in st.session_state:

# #             question = st.text_area(
# #                 "Edit OCR result if needed",
# #                 st.session_state["ocr_text"]
# #             )

# #     # AUDIO MODE
# #     elif mode == "Audio":

# #         audio = st.file_uploader(
# #             "Upload audio question",
# #             type=["wav", "mp3"]
# #         )

# #         if audio:

# #             st.audio(audio)

# #             if st.button("Transcribe Audio"):

# #                 text = transcribe_audio(audio)

# #                 st.session_state["audio_text"] = text

# #         if "audio_text" in st.session_state:

# #             question = st.text_area(
# #                 "Edit transcription if needed",
# #                 st.session_state["audio_text"]
# #             )

# #     # Solve button
# #     if st.button("Solve Problem"):

# #         run_pipeline(question)


# # if __name__ == "__main__":
#     main()



import os
import sys
import streamlit as st
import torch

# Fix import path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

# Pipelines
from app.pipelines.ocr_pipeline import extract_text_from_image
from app.pipelines.speech_pipeline import transcribe_audio
from app.pipelines.rag_pipeline import retrieve_context

# Agents
from app.agents.parser_agent import parse_math_problem
from app.agents.router_agent import route_problem
from app.agents.solver_agent import solve_calculus
from app.agents.verifier_agent import verify_calculus_solution
from app.agents.explainer_agent import generate_explanation

# Memory
from app.memory.memory_store import search_memory, save_memory


def run_pipeline(question):

    trace = []

    if not question.strip():
        st.warning("Please enter a math problem")
        return

    # Parser Agent
    parsed = parse_math_problem(question)
    trace.append("✔ Parser Agent")

    st.subheader("Parsed Problem")
    st.json(parsed)

    # Router Agent
    route = route_problem(parsed)
    trace.append("✔ Router Agent")

    st.subheader("Router Decision")
    st.json(route)

    # Memory Check
    memory = search_memory(parsed["problem_text"])
    trace.append("✔ Memory Check")

    if memory:

        st.subheader("Memory Hit")
        st.json(memory)

        st.subheader("Agent Trace")
        for step in trace:
            st.write(step)

        return

    # RAG Retrieval
    context = retrieve_context(parsed["problem_text"])
    trace.append("✔ RAG Retrieval")

    st.subheader("Retrieved Knowledge")

    if context:
        for doc in context:
            st.write(doc)
    else:
        st.write("No knowledge retrieved.")

    # Solver Agent
    solution = solve_calculus(parsed["problem_text"])
    trace.append("✔ Solver Agent")

    if "error" in solution:
        st.error(solution["error"])
        return

    st.subheader("Solver Output")
    st.json(solution)

    # Verifier Agent
    verification = verify_calculus_solution(
        solution["expression"],
        solution["derivative"]
    )
    trace.append("✔ Verifier Agent")

    st.subheader("Verifier Result")
    st.json(verification)

    # Explainer Agent
    explanation = generate_explanation(
        parsed["problem_text"],
        solution["derivative"]
    )
    trace.append("✔ Explainer Agent")

    st.subheader("Step-by-Step Explanation")

    for step in explanation:
        st.write(step)

    # Save to Memory
    save_memory({
        "question": parsed["problem_text"],
        "topic": parsed["topic"],
        "solution": solution["derivative"],
        "verified": verification["verified"]
    })

    st.success("Stored in memory")

    # Show Agent Trace
    st.subheader("Agent Trace")

    for step in trace:
        st.write(step)


def main():

    st.title("AI Math Mentor")

    st.write("Solve math problems using AI")

    # GPU detection
    if torch.cuda.is_available():
        st.success(f"GPU detected: {torch.cuda.get_device_name(0)}")
    else:
        st.warning("Running on CPU")

    mode = st.selectbox(
        "Select Input Mode",
        ["Text", "Image", "Audio"]
    )

    question = ""

    # TEXT INPUT
    if mode == "Text":

        question = st.text_area("Enter math problem")

    # IMAGE INPUT
    elif mode == "Image":

        image = st.file_uploader(
            "Upload math problem image",
            type=["png", "jpg", "jpeg"]
        )

        if image:

            st.image(image)

            if st.button("Extract Text"):

                text = extract_text_from_image(image)

                st.session_state["ocr_text"] = text

        if "ocr_text" in st.session_state:

            question = st.text_area(
                "Edit OCR result if needed",
                st.session_state["ocr_text"]
            )

    # AUDIO INPUT
    elif mode == "Audio":

        audio = st.file_uploader(
            "Upload audio question",
            type=["wav", "mp3"]
        )

        if audio:

            st.audio(audio)

            if st.button("Transcribe Audio"):

                text = transcribe_audio(audio)

                st.session_state["audio_text"] = text

        if "audio_text" in st.session_state:

            question = st.text_area(
                "Edit transcription if needed",
                st.session_state["audio_text"]
            )

    # Solve button
    if st.button("Solve Problem"):

        run_pipeline(question)


if __name__ == "__main__":
    main()


# import os
# import sys
# import streamlit as st
# import torch

# # Fix import path
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# if project_root not in sys.path:
#     sys.path.append(project_root)

# # Pipelines
# from app.pipelines.ocr_pipeline import extract_text_from_image
# from app.pipelines.speech_pipeline import transcribe_audio
# from app.pipelines.rag_pipeline import retrieve_context

# # Agents
# from app.agents.parser_agent import parse_math_problem
# from app.agents.router_agent import route_problem
# from app.agents.solver_agent import solve_calculus
# from app.agents.verifier_agent import verify_calculus_solution
# from app.agents.explainer_agent import generate_explanation

# # Memory
# from app.memory.memory_store import search_memory, save_memory


# def run_pipeline(question):

#     trace = []

#     if not question.strip():
#         st.warning("Please enter a math problem")
#         return

#     # Parser
#     parsed = parse_math_problem(question)
#     trace.append("Parser Agent")

#     # Router
#     route = route_problem(parsed)
#     trace.append("Router Agent")

#     # Memory Check
#     memory = search_memory(parsed["problem_text"])
#     trace.append("Memory Check")

#     if memory:
#         st.subheader("Memory Hit")
#         st.json(memory)

#         show_trace(trace)
#         return

#     # RAG Retrieval
#     context = retrieve_context(parsed["problem_text"])
#     trace.append("RAG Retrieval")

#     # Solver
#     solution = solve_calculus(parsed["problem_text"])
#     trace.append("Solver Agent")

#     if "error" in solution:
#         st.error(solution["error"])
#         return

#     # Verifier
#     verification = verify_calculus_solution(
#         solution["expression"],
#         solution["derivative"]
#     )
#     trace.append("Verifier Agent")

#     # Explanation
#     explanation = generate_explanation(
#         parsed["problem_text"],
#         solution["derivative"]
#     )
#     trace.append("Explainer Agent")

#     # Save Memory
#     save_memory({
#         "question": parsed["problem_text"],
#         "topic": parsed["topic"],
#         "solution": solution["derivative"],
#         "verified": verification["verified"]
#     })

#     # Dashboard Results
#     col1, col2 = st.columns(2)

#     with col1:

#         st.subheader("Parsed Problem")
#         st.json(parsed)

#         st.subheader("Solver Output")
#         st.json(solution)

#     with col2:

#         st.subheader("Verifier Result")
#         st.json(verification)

#         st.subheader("Step-by-Step Explanation")

#         for step in explanation:
#             st.write(step)

#     # Knowledge
#     st.subheader("Retrieved Knowledge")

#     if context:
#         for doc in context:
#             st.write(doc)
#     else:
#         st.write("No knowledge retrieved.")

#     # Trace panel
#     show_trace(trace)


# def show_trace(trace):

#     st.subheader("Agent Pipeline")

#     for step in trace:

#         st.progress(100)

#         st.write(f"✔ {step}")


# def main():

#     st.set_page_config(
#         page_title="AI Math Mentor",
#         layout="wide"
#     )

#     st.title("AI Math Mentor")

#     col_main, col_status = st.columns([3, 1])

#     with col_status:

#         st.subheader("System Status")

#         if torch.cuda.is_available():
#             st.success(f"GPU: {torch.cuda.get_device_name(0)}")
#         else:
#             st.warning("Running on CPU")

#         st.info("Whisper Model: Loaded")
#         st.info("RAG Database: Active")

#     with col_main:

#         st.subheader("Solve Math Problems")

#         mode = st.selectbox(
#             "Select Input Mode",
#             ["Text", "Image", "Audio"]
#         )

#         question = ""

#         # TEXT MODE
#         if mode == "Text":

#             question = st.text_area("Enter math problem")

#         # IMAGE MODE
#         elif mode == "Image":

#             image = st.file_uploader(
#                 "Upload math problem image",
#                 type=["png", "jpg", "jpeg"]
#             )

#             if image:

#                 st.image(image)

#                 if st.button("Extract Text"):

#                     text = extract_text_from_image(image)

#                     st.session_state["ocr_text"] = text

#             if "ocr_text" in st.session_state:

#                 question = st.text_area(
#                     "Edit OCR result if needed",
#                     st.session_state["ocr_text"]
#                 )

#         # AUDIO MODE
#         elif mode == "Audio":

#             audio = st.file_uploader(
#                 "Upload audio question",
#                 type=["wav", "mp3"]
#             )

#             if audio:

#                 st.audio(audio)

#                 if st.button("Transcribe Audio"):

#                     text = transcribe_audio(audio)

#                     st.session_state["audio_text"] = text

#             if "audio_text" in st.session_state:

#                 question = st.text_area(
#                     "Edit transcription if needed",
#                     st.session_state["audio_text"]
#                 )

#         # Solve
#         if st.button("Solve Problem"):

#             run_pipeline(question)


# if __name__ == "__main__":
#     main()