import glob
import matplot.pyplot as plot
import numpy as np

for name in glob.glob('./outputs/case_*'):
    with open(name) as in_file:
        arr = []
        for line in in_file.readlines():
            arr.append(float(line))

        print(name, 'Avg. time:', np.average(arr))

# Matplot stuff
# plot.plot([100, 1000, 10000, 100000, 1000000, 10000000, 100000000], ['''times here'''], 'b-')
# plot.xscale('log')
# plot.show()
