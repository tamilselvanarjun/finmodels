import numpy as np
import cvxpy as cp

def optimize_portfolio(expected_returns, covariance_matrix):
    """
    Optimize portfolio weights based on expected returns and covariance matrix.

    Parameters:
    - expected_returns (numpy.ndarray): Array of expected returns for each asset.
    - covariance_matrix (numpy.ndarray): Covariance matrix of asset returns.

    Returns:
    - numpy.ndarray or None: Optimized portfolio weights if successful, None otherwise.
    """
    num_assets = len(expected_returns)

    
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

    if problem.status == cp.OPTIMAL:
        return weights.value
    else:
        print("Optimization problem could not be solved.")
        return None
