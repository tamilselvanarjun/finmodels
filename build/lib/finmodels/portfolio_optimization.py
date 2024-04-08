

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

<<<<<<< HEAD
    # Initialize weights with equal distribution
    weights = [1 / num_assets] * num_assets

    # Calculate expected return and risk
    expected_return = sum(expected_returns[i] * weights[i] for i in range(num_assets))
    risk = sum(sum(weights[i] * weights[j] * covariance_matrix[i][j] for j in range(num_assets)) for i in range(num_assets))

    # Maximize return and minimize risk
    objective_value = expected_return - 0.5 * risk
=======
    
    weights = cp.Variable(num_assets)
    expected_return = expected_returns @ weights
    risk = cp.quad_form(weights, covariance_matrix)

    
    objective = cp.Maximize(expected_return - 0.5 * risk)

    
    constraints = [cp.sum(weights) == 1, weights >= 0]
>>>>>>> d7d41825fdf14ed26ae59f330531795bb2c7f6d9

    # Check if weights sum to 1 and individual weights are non-negative
    weights_sum_to_one = sum(weights) == 1
    non_negative_weights = all(weight >= 0 for weight in weights)

    if weights_sum_to_one and non_negative_weights:
        return weights
    else:
        print("Optimization problem could not be solved.")
        return None
