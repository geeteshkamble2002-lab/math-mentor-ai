import re


def parse_math_problem(problem_text: str):

    problem_text = problem_text.strip()

    topic = detect_topic(problem_text)

    variables = extract_variables(problem_text)

    needs_clarification = detect_ambiguity(problem_text)

    parsed_problem = {
        "problem_text": problem_text,
        "topic": topic,
        "variables": variables,
        "needs_clarification": needs_clarification
    }

    return parsed_problem


def detect_topic(text):

    text = text.lower()

    if "derivative" in text or "differentiate" in text:
        return "calculus"

    elif "probability" in text:
        return "probability"

    elif "matrix" in text:
        return "linear_algebra"

    else:
        return "algebra"


def extract_variables(text):

    text = text.lower()

    possible_vars = ["x", "y", "z"]

    variables = []

    for var in possible_vars:
        if var in text:
            variables.append(var)

    return variables


def detect_ambiguity(text):

    if len(text) < 5:
        return True

    if "find" not in text.lower():
        return True

    return False