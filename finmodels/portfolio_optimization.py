import numpy as np
import cvxpy as cp

def optimize_portfolio(expected_returns, covariance_matrix):
    num_assets = len(expected_returns)

    # Define the variables for optimization
    weights = cp.Variable(num_assets)
    expected_return = expected_returns @ weights
    risk = cp.quad_form(weights, covariance_matrix)

    # Define the objective function (maximize return, minimize risk)
    objective = cp.Maximize(expected_return - 0.5 * risk)

    # Define the constraints (weights sum to 1, individual weights are non-negative)
    constraints = [cp.sum(weights) == 1, weights >= 0]

    # Formulate and solve the problem
    problem = cp.Problem(objective, constraints)
    problem.solve()

    if problem.status == 'optimal':
        return weights.value
    else:
        print("Optimization problem could not be solved.")
        return None
