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

# filtro = df[df['Gender'].isin(['Female', 'Male'])]
# KDE=True
# sns.histplot(data=filtro, x='Customer_Satisfaction', hue= 'Gender', kde=True)
# plt.show()

# ex intermediarios ---------------–---------------------

# ex 5 : Scatterplot de Time_Spent_on_Product_Research(hours) vs Product_Rating, colorido por Purchase_Category.

# sns.scatterplot(data=df, x='Time_Spent_on_Product_Research(hours)', y='Product_Rating', hue='Purchase_Category')
# plt.savefig('00_Scatterplot_TimeSpent.png')
# plt.show()



# ex 6: Violinplot de Brand_Loyalty por Purchase_Channel, dividido por Discount_Used (split=True).

# sns.violinplot(data=df, x='Brand_Loyalty', y='Purchase_Channel', hue='Discount_Used', split=True)
# plt.show()


# ex: 7: Compare Frequency_of_Purchase entre membros e não membros do programa (Customer_Loyalty_Program_Member) usando um barplot agrupado.

# sns.barplot(data=df, y='Frequency_of_Purchase',hue='Customer_Loyalty_Program_Member',palette='rocket')
# plt.title('Frequencia de compra entre membros e não membros do programa de lealdade')
# plt.ylabel('Frequência de compra')
# plt.show()


# ex 8: Heatmap da frequência cruzada entre Payment_Method e Device_Used_for_Shopping.

tabela = df.groupby(['Device_Used_for_Shopping', 'Payment_Method']).size().unstack(fill_value=0)
sns.heatmap(data=tabela, annot=True, cmap='plasma', fmt='d')
plt.savefig('00_heatmap.png')
plt.show()

# o annot = True -> anota os valores dentro dos quadrados no gráfico, o  'YlOrRd' refere-se a cor da table, o fmt = 'd' - > faz com que os numeros que aparecem no annot sejam decimais nao quebrados (sem ser de virgula)


# exercicios avancados ---------------------------------------

#ex 9: FacetGrid de Purchase_Amount vs Age, separado por Location (use col_wrap=3).