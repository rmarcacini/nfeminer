import urllib.request, json
import pandas as pd

def search(q,host='localhost',port=9200,columns=[]):

  query = urllib.parse.quote_plus(q)
  L = []
  with urllib.request.urlopen("http://"+host+":"+str(port)+"/_search/?q="+query+"&size=10000") as url:
      data = json.loads(url.read().decode())
      for item in data['hits']['hits']:
        try:
          item['_source']['score'] = item['_score']
          L.append(item['_source'])
        except:
          1
      #print(data)

  df_query = pd.DataFrame(L)
  # columns form nfe sample ['Numero','Data_de_emissao','CEP_emit', 'Municipio_emit','Descricao_do_Produto_ou_servicos', 'Quant_prod', 'Valor_unit_prod','Valor_total_prod','NCM_prod','score']
  if len(columns) > 0: df_query = df_query[columns]

  return df_query
