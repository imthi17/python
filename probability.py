from scipy.stats import norm, bernoulli

# 1. Normal Distribution
def normal_distribution():
    mu = 0      # mean
    sigma = 1   # standard deviation
    x = 1       # point to evaluate

    probability = norm.pdf(x, mu, sigma)
    print("--- Normal Distribution ---")
    print(f"P(X = {x}) when μ = {mu}, σ = {sigma} is {probability:.4f}")

# 2. Bernoulli Distribution
def bernoulli_distribution():
    p = 0.3  # Probability of success
    x0 = 0
    x1 = 1

    prob_0 = bernoulli.pmf(x0, p)
    prob_1 = bernoulli.pmf(x1, p)

    print("\n--- Bernoulli Distribution ---")
    print(f"P(X = 0): {prob_0:.2f}")
    print(f"P(X = 1): {prob_1:.2f}")

# 3. Bayes' Theorem Example
def bayes_theorem():
    # Given:
    # P(Disease) = 0.01
    # P(No Disease) = 0.99
    # P(Pos | Disease) = 0.99
    # P(Pos | No Disease) = 0.05

    P_D = 0.01
    P_not_D = 0.99
    P_Pos_given_D = 0.99
    P_Pos_given_not_D = 0.05

    # P(Pos) = P(Pos | D) * P(D) + P(Pos | ~D) * P(~D)
    P_Pos = P_Pos_given_D * P_D + P_Pos_given_not_D * P_not_D

    # Bayes' Theorem:
    # P(D | Pos) = (P(Pos | D) * P(D)) / P(Pos)
    P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

    print("\n--- Bayes' Theorem ---")
    print(f"Probability of having disease given a positive test: {P_D_given_Pos:.4f} ({P_D_given_Pos*100:.2f}%)")

# Run all functions
normal_distribution()
bernoulli_distribution()
bayes_theorem()
