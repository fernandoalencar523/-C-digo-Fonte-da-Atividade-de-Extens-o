# data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Carrega dados de um arquivo CSV.
    """
    return pd.read_csv(file_path)

def plot_data(data):
    """
    Plota um gráfico simples dos dados.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Value'], marker='o', linestyle='-')
    plt.title('Gráfico de Dados')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data_plot.png')
    plt.show()

if __name__ == "__main__":
    file_path = 'data.csv'  # Nome do arquivo CSV com os dados
    data = load_data(file_path)
    plot_data(data)
