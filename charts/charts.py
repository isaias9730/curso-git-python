import matplotlib.pyplot as plt

def  generate_chart():
    labels = ['a', 'b', 'c']
    values = [13, 24, 33]

    fig, ax = plt.subplots()
    ax.bar(labels, values)

    plt.savefig('chart.png')
    plt.close()