import matplotlib.pyplot as plt

def my_matplotlib_pyplot_standards_setup():
    plt.rc('figure', figsize=(14, 10))
    plt.rc('font', size = 14)
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['axes.grid'] = False
    return

if __name__ == '__main__':
    print(f"Please only import this 'my_matplotlib_standards.py' module.")