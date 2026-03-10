# def generate_explanation(problem_text, derivative):

#     explanation = []

#     explanation.append(f"Problem: {problem_text}")

#     explanation.append("Step 1: Identify the mathematical operation.")
#     explanation.append("The problem asks for the derivative.")

#     explanation.append("Step 2: Rewrite the expression if needed.")

#     explanation.append("Step 3: Apply the derivative rule d(ax)/dx = a.")

#     explanation.append(f"Step 4: Compute the derivative.")

#     explanation.append(f"Final Answer: {derivative}")

#     return explanation


from sympy import symbols, sympify, diff


x = symbols("x")


def generate_explanation(problem, derivative):

    steps = []

    try:

        expr = sympify(problem)

        steps.append(f"Problem: Find derivative of {expr}")

        # Step 1
        steps.append("Step 1: Identify the function.")

        steps.append(f"The function is f(x) = {expr}")

        # Step 2 rule detection
        if "**" in str(expr):

            steps.append("Step 2: Apply the power rule.")

            steps.append("Power rule: d/dx(x^n) = n*x^(n-1)")

        elif "sin" in str(expr):

            steps.append("Step 2: Apply derivative of sin(x).")

            steps.append("d/dx(sin(x)) = cos(x)")

        elif "cos" in str(expr):

            steps.append("Step 2: Apply derivative of cos(x).")

            steps.append("d/dx(cos(x)) = -sin(x)")

        else:

            steps.append("Step 2: Apply derivative rules.")

        # Step 3 calculation
        result = diff(expr, x)

        steps.append("Step 3: Compute the derivative.")

        steps.append(f"d/dx({expr}) = {result}")

        # Final
        steps.append(f"Final Answer: {result}")

        return steps

    except Exception:

        return [
            "Step 1: Understand the problem.",
            "Step 2: Apply derivative rules.",
            f"Final Answer: {derivative}"
        ]