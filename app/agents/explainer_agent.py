def generate_explanation(problem_text, derivative):

    explanation = []

    explanation.append(f"Problem: {problem_text}")

    explanation.append("Step 1: Identify the mathematical operation.")
    explanation.append("The problem asks for the derivative.")

    explanation.append("Step 2: Rewrite the expression if needed.")

    explanation.append("Step 3: Apply the derivative rule d(ax)/dx = a.")

    explanation.append(f"Step 4: Compute the derivative.")

    explanation.append(f"Final Answer: {derivative}")

    return explanation