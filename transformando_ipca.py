import pandas as pd

ipca_hist = pd.read_csv('ipca_historico.csv',
                        index_col='Ano',
                        decimal = ',',
                        dtype={'Jan': float,
                               'Fev': float, 
                               'Mar': float,
                               'Abr': float,
                               'Mai': float,
                               'Jun': float,
                               'Jul': float,
                               'Ago': float,
                               'Set': float,
                               'Out': float,
                               'Nov': float,
                               'Dez': float,
                              }
                       )

ipca_hist_mes = ipca_hist.drop(columns = 'Acumulado no ano').loc[ipca_hist.index >= 2013]

df_final = pd.DataFrame([], columns = ['percentual IPCA', 'Mes','Ano'])

for ano in list(ipca_hist_mes.index):
    valores = pd.DataFrame(list(ipca_hist_mes.loc[ipca_hist_mes.index == ano].transpose().values[:, 0]), columns = ['percentual IPCA'])
    mes = pd.DataFrame(list(ipca_hist_mes.loc[ipca_hist_mes.index == ano]), columns = ['Mes'])
    df_temp = pd.concat([valores, mes], axis = 1)
    df_temp['Ano'] = ano

    df_final = pd.concat([df_final, df_temp], axis = 0)

df_final = df_final.reset_index(drop = True)

df_final.to_csv('ipca_tratado.csv', index = False, encoding = 'utf-8')