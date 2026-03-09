import sympy as sp


def solve_calculus(problem_text):

    try:
        x = sp.symbols('x')

        text = problem_text.lower()

        # remove words
        text = text.replace("find derivative", "")
        text = text.replace("derivative", "")
        text = text.replace(" ", "")

        # convert uppercase X → x
        text = text.replace("X", "x")

        # convert expression
        expr = sp.sympify(text)

        derivative = sp.diff(expr, x)

        return {
            "expression": str(expr),
            "derivative": str(derivative)
        }

    except Exception as e:

        return {
            "error": str(e)
        }