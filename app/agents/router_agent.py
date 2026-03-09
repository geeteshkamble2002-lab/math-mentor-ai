def route_problem(parsed_problem):

    topic = parsed_problem["topic"]

    if topic == "calculus":
        return {"route": "calculus_solver"}

    elif topic == "algebra":
        return {"route": "algebra_solver"}

    elif topic == "probability":
        return {"route": "probability_solver"}

    elif topic == "linear_algebra":
        return {"route": "linear_algebra_solver"}

    else:
        return {"route": "general_solver"}