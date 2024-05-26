import math

# # Constants
# n = 500000  # number of distinct events
# m = 4000000  # number of attempts

# # Calculate probability that a specific event does not occur in m attempts
# p_not_occur = (1 - 1/n)**m

# # Probability that all events occur at least once
# probability_all_events = math.exp(-n * p_not_occur)

# print(probability_all_events)
import numpy as np
import matplotlib.pyplot as plt

# Number of events
n = 500000

# Range of attempts
m_values = np.arange(1000000, 10000001, 1000000)  # from 1,000,000 to 10,000,000 in steps of 1,000,000

# Calculate probabilities for each number of attempts
probabilities = [math.exp(-n * ((1 - 1/n)**m)) for m in m_values]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(m_values, probabilities, marker='o')
plt.title('Probability of All Events Occurring At Least Once vs. Number of Attempts')
plt.xlabel('Number of Attempts')
plt.ylabel('Probability')
plt.yscale('log')  # Log scale for better visualization
plt.grid(True)
plt.show()
print(m_values)
print(probabilities)