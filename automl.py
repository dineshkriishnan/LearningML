import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO, StringIO
import seaborn as sns
import base64

def read_data(file):
    return pd.read_csv(file.stream)

def heatmap(corr):

    img = BytesIO()
    sns.heatmap(corr, annot= True)
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64, {}'.format(plot_url)
