import numpy as np
import matplotlib.pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages


def graph(x, y, label, title='Graph'):
    page = PdfPages('plot.pdf')

    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
            }

    # x = np.linspace(0.0, 5.0, 100)
    # y = np.cos(2 * np.pi * x) * np.exp(-x)

    plot.plot(x, y, 'k')
    plot.title(title, fontdict=font)
    plot.text(2, 0.65, label, fontdict=font)
    plot.xlabel('time (s)', fontdict=font)
    plot.ylabel('count', fontdict=font)

    # Tweak spacing to prevent clipping of ylabel
    plot.subplots_adjust(left=0.15)

    plot.savefig(page, format='pdf')

    plot.show()
    page.close()
