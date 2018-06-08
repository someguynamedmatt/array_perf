import glob
import matplotlib.pyplot as plot
import numpy as np

plot_points = []
iterations = []

def get_iterations(file_name):
    return file_name.split('_')[len(file_name.split('_')) - 1]


for name in glob.glob('./outputs/case_1_count*'):
    iterations.append(int(get_iterations(name)))
    with open(name) as in_file:
        arr = []
        for line in in_file.readlines():
            arr.append(float(line))

        plot_points.append(float(np.average(arr)))
    plot.plot(iterations, plot_points, '.r-')
    plot.xscale('log')
plot_points = []
iterations = []



for name in glob.glob('./outputs/case_2_count*'):
    iterations.append(int(get_iterations(name)))
    with open(name) as in_file:
        arr = []
        for line in in_file.readlines():
            arr.append(float(line))

        plot_points.append(float(np.average(arr)))
    plot.plot(iterations, plot_points, '.y-')
    plot.xscale('log')
plot_points = []
iterations = []


for name in glob.glob('./outputs/case_3_count*'):
    iterations.append(int(get_iterations(name)))
    with open(name) as in_file:
        arr = []
        for line in in_file.readlines():
            arr.append(float(line))

        plot_points.append(float(np.average(arr)))
    plot.plot(iterations, plot_points, '.b-')
    plot.xscale('log')
plot_points = []
iterations = []


for name in glob.glob('./outputs/case_4_count*'):
    iterations.append(int(get_iterations(name)))
    with open(name) as in_file:
        arr = []
        for line in in_file.readlines():
            arr.append(float(line))

        plot_points.append(float(np.average(arr)))
    plot.plot(iterations, plot_points, '.c-')
    plot.xscale('log')
plot_points = []
iterations = []


plot.show()
