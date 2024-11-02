
import matplotlib.pyplot as plt

# Assuming you've parsed your stats into Python lists
cache_sizes = [64, 256, 1024]  # Example cache sizes
miss_rates = [0.15, 0.10, 0.05]  # Example miss rates

plt.figure()
plt.plot(cache_sizes, miss_rates, marker='o')
plt.title('Cache Size vs Miss Rate')
plt.xlabel('Cache Size (kB)')
plt.ylabel('Miss Rate')
plt.grid(True)
plt.savefig('cache_miss_rates.png')
plt.show()


"""
import pandas as pd
import matplotlib.pyplot as plt

# Example of reading and plotting cache miss rates
data = pd.read_csv('stats_simple.txt', delim_whitespace=True)  # Adjust based on how data is formatted
plt.figure()
plt.plot(data['time'], data['miss_rate'])
plt.title('Cache Miss Rate Over Time')
plt.xlabel('Time')
plt.ylabel('Miss Rate')
plt.show()
"""