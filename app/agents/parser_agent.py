# # import re


# # def parse_math_problem(problem_text: str):

# #     problem_text = problem_text.strip()

# #     topic = detect_topic(problem_text)

# #     variables = extract_variables(problem_text)

# #     needs_clarification = detect_ambiguity(problem_text)

# #     parsed_problem = {
# #         "problem_text": problem_text,
# #         "topic": topic,
# #         "variables": variables,
# #         "needs_clarification": needs_clarification
# #     }

# #     return parsed_problem


# # def detect_topic(text):

# #     text = text.lower()

# #     if "derivative" in text or "differentiate" in text:
# #         return "calculus"

# #     elif "probability" in text:
# #         return "probability"

# #     elif "matrix" in text:
# #         return "linear_algebra"

# #     else:
# #         return "algebra"


# # def extract_variables(text):

# #     text = text.lower()

# #     possible_vars = ["x", "y", "z"]

# #     variables = []

# #     for var in possible_vars:
# #         if var in text:
# #             variables.append(var)

# #     return variables


# # def detect_ambiguity(text):

# #     if len(text) < 5:
# #         return True

# #     if "find" not in text.lower():
# #         return True

# #     return False


# # import re

# # def clean_expression(text):

# #     text = text.lower()

# #     text = text.replace("squared", "**2")
# #     text = text.replace("square", "**2")

# #     text = text.replace("cubed", "**3")

# #     text = text.replace("^", "**")

# #     text = text.replace(" ", "")

# #     return text


# # def parse_math_problem(problem):

# #     expression = clean_expression(problem)

# #     return {
# #         "problem_text": expression,
# #         "topic": "calculus",
# #         "variables": ["x"],
# #         "needs_clarification": False
# #     }


# import re


# def normalize_expression(text):

#     text = text.lower()

#     # remove common words
#     text = text.replace("find", "")
#     text = text.replace("derivative", "")
#     text = text.replace("of", "")
#     text = text.replace(" ", "")

#     # math replacements
#     text = text.replace("squared", "**2")
#     text = text.replace("square", "**2")
#     text = text.replace("cubed", "**3")
#     text = text.replace("^", "**")

#     # convert implicit multiplication
#     text = re.sub(r'(\d)x', r'\1*x', text)

#     return text


# def parse_math_problem(problem_text):

#     cleaned = normalize_expression(problem_text)

#     variables = []

#     if "x" in cleaned:
#         variables.append("x")

#     return {
#         "problem_text": cleaned,
#         "topic": "calculus",
#         "variables": variables,
#         "needs_clarification": False
#     }


import re


def normalize_expression(text):

    text = text.lower()

    # remove common instruction words
    remove_words = [
        "find",
        "the",
        "derivative",
        "differentiate",
        "calculate",
        "of"
    ]

    for w in remove_words:
        text = text.replace(w, "")

    text = text.strip()

    # math phrase replacements
    replacements = {
        "squared": "**2",
        "square": "**2",
        "cubed": "**3",
        "cube": "**3",
        "plus": "+",
        "minus": "-",
        "times": "*",
        "multiplied by": "*",
        "divided by": "/",
        "sin ": "sin(",
        "cos ": "cos(",
        "tan ": "tan(",
        "log ": "log("
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    # add closing bracket for trig/log
    if "sin(" in text or "cos(" in text or "tan(" in text or "log(" in text:
        if not text.endswith(")"):
            text = text + ")"

    # implicit multiplication
    text = re.sub(r'(\d)x', r'\1*x', text)

    # replace power symbol
    text = text.replace("^", "**")

    text = text.replace(" ", "")

    return text


def parse_math_problem(problem_text):

    expression = normalize_expression(problem_text)

    variables = []

    if "x" in expression:
        variables.append("x")

    return {
        "problem_text": expression,
        "topic": "calculus",
        "variables": variables,
        "needs_clarification": False
    }