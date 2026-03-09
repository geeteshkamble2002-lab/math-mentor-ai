import sympy as sp


def verify_calculus_solution(expression, derivative):

    try:
        x = sp.symbols('x')

        expr = sp.sympify(expression)
        true_derivative = sp.diff(expr, x)

        if str(true_derivative) == derivative:

            return {
                "verified": True,
                "message": "Solution verified successfully"
            }

        else:

            return {
                "verified": False,
                "message": "Solver result may be incorrect"
            }

    except Exception as e:

        return {
            "verified": False,
            "error": str(e)
        }