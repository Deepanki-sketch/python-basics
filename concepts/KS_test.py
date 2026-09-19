from scipy.stats import kstest

data = [10, 12, 11, 13, 9, 15, 10, 12]

# Test whether data follows a normal distribution
statistic, p_value = kstest(data, 'norm')

print("KS statistic =", statistic)
print("p-value =", p_value)