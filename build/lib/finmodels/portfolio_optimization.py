# financial_models/portfolio_optimization.py
import numpy as np
import cvxpy as cp

def optimize_portfolio(expected_returns, covariance_matrix):
    """
    Optimize a portfolio using Mean-Variance Optimization.

    Parameters:
    - expected_returns: Expected returns for each asset
    - covariance_matrix: Covariance matrix of asset returns

    Returns:
    - Optimal portfolio weights
    """
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

    return weights.value
