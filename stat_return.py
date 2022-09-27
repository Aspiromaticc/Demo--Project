import statistics as st
def describe(sample):
    return st.mean(sample), st.median(sample), st.mode(sample)
sample = [8, 12, 4, 6, 21, 14, 13, 4, 23]
mean, median, mode = describe(sample)
print("{:.2f}".format(mean))
print(mode)
print(median)
desc = describe(sample)
print(desc)
