import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())
#
# print(df.columns.tolist())

def cria_graficos (df):
    # plt.figure(figsize=(15, 10))
    # plt.subplot(3, 3, 1)
    # plt.hist(df['Nota'], bins=100, color='green' , alpha=0.8)
    # plt.title('Quantidade de Vendas vs Avaliacao/Nota do produto')
    # plt.xlabel('Nota')
    # plt.xticks(ticks=range(0 , int(df['Nota'].max()), 1))
    # plt.ylabel('Qtd_Vendidos_Cod')
    # plt.grid(True)

    fig1 = px.histogram(df, x='Nota', nbins=100, title='Quantidade de Vendas vs Avaliacao/Nota do produto')


    # plt.subplot(3, 3, 2)
    # plt.scatter(df['Nota'], df['Qtd_Vendidos_Cod'], color='#98FB98', alpha=0.6,s=30)
    # plt.title('Dipersao - Notas vs Quantidade de Vendas')
    # plt.xticks(ticks=range(0 , int(df['Nota'].max())+1, 1))
    # plt.xlabel('Nota')
    # plt.ylabel('Qtd_Vendidos_Cod')

    fig3 = px.scatter(df, x='Nota', y='Qtd_Vendidos_Cod', size='Nota', color='Nota', hover_name='Nota', size_max=60)
    fig3.update_layout(title='Avaliação por Quantidade de Vendas')


    # Mapa de Calor
    # plt.subplot(3, 3, 3)
    # corr = df[['Temporada_Cod','Qtd_Vendidos_Cod']].corr()
    # sns.heatmap(corr, annot=True, cmap='coolwarm')
    # plt.title('Correlacao Vendas por Temporada')

    # Grafico de Barra
    # x1 = df['Desconto'].value_counts().index
    # y1 = df['Desconto'].value_counts().values
    #
    # plt.subplot(3,3, 4)
    # plt.bar(x1, y1, color='#98FB98')
    # plt.title('Distribuicao de Desconto')
    # plt.xlabel('Desconto')
    # plt.ylabel('Quantidade')

    x1 = df['Desconto']
    y1 = df['Desconto']
    fig4 = px.bar(df, x=x1, y=y1, color='Desconto', barmode='group')
    fig4.update_layout(
        title='Distribuicao de Desconto', xaxis_title='Desconto', yaxis_title='Quantidade', legend_title='% vs Qtd'
    )

    # Grafico de Pizza
    # plt.subplot(3, 3, 5)
    # x2 = df['Temporada'].value_counts().index
    # y2 = df['Temporada'].value_counts().values
    # plt.pie(y2, labels=x2, autopct='%.1f%%', startangle=90)
    # plt.title('Representatividade de vendas vs Temporada')

    fig2 = px.pie(df, names='Temporada', color='Temporada', hole=0.2)

    # Grafico de Densidade
    # plt.subplot(3, 3, 6)
    # sns.kdeplot(df['Preço'], fill=True, color='#98FB98')
    # plt.title('Densidade de Preço')
    # plt.xlabel('Preço')


    #Grafico de Regressão
    # plt.subplot(3,3,7)
    # sns.regplot(x='Preço', y='N_Avaliações', data=df, color='#98FB98', scatter_kws={'alpha':0.5, 'color': '#000000'})
    # plt.title('Regressão de N° de Avaliações vs Preço')
    # plt.xlabel('Preço')
    # plt.ylabel('N_Avaliações')
    return fig1, fig2, fig3, fig4

# plt.tight_layout()
# plt.show()

def cria_app(df):
    app = Dash(__name__)

    fig1, fig2, fig3, fig4 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
    ])
    return app

df = pd.read_csv('ecommerce_estatistica.csv')

if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)

