import numpy as np 
import matplotlib.pyplot as plt

def makeplot(slope, intercept, title):
    print('Setting up data for plotting...')

    x = np.linspace(-10,10)
    y = slope * x + intercept

    print('Making plot...')

    plt.figure()
    plt.plot(x,y, 'H', c='purple')
    plt.title(title)

    print('All done!')