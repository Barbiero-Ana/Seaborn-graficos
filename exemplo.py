import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Requisitos básicos!!


# - Distribuicao de idades -> criar um histograma ou KDE plot da coluna Age FEITO

# - Proporcao por genero -> Criar um countplot para gender com porcentagens nas barras

# Nivel de renda vs Valor gasto -> criar um boxplot de purchase_amount por income_level

# Satisfacao do cliente -> criar um histograma de customer satisfaction (1-10) -> fazer a comparacao entre homens e mulheres
# da pra fazer usando: hue=Gender.



df = pd.read_csv('Ecommerce_Consumer_Behavior_Analysis_Data.csv')


# ex 1
# KDE = True
# sns.histplot(data = df, x='Age', kde=True)
# plt.savefig('00_Histoplot.png')
# plt.close


# ex 2
# graf = sns.countplot(data = df, x='Gender')
# total = len(df)
# for p in graf.patches:
#     valor = p.get_height()
#     porcentagem = f'{100 * valor / total:.1f}%'
#     graf.text(p.get_x() + p.get_width()/2, valor, porcentagem, ha='center')
# plt.savefig('00_teste.png')
# plt.close()


#ex 3
# df['preco_limpo'] = df.apply(lambda x: float(x['Purchase_Amount'][1:]), axis=1)
# sns.boxplot(data=df, x='Income_Level', y = 'preco_limpo')
# plt.savefig('00_boxplotteste.png')
# plt.show()
# plt.close()

# # ex 4
# KDE = True
# sns.histplot(data=df, x='Customer_Satisfaction', hue='Gender', kde=True)
# plt.show()

#ex 4 

filtro = df[df['Gender'].isin(['Female', 'Male'])]
KDE=True
sns.histplot(data=filtro, x='Customer_Satisfaction', hue= 'Gender', kde=True)
plt.show()

# vamos fazer uma alteracao qualquer 