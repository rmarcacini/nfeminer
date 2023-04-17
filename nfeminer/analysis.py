import numpy as np
from sklearn.neighbors import NearestNeighbors
import seaborn as sns
import matplotlib.pyplot as plt
import json
import os

def hist_kde(df_model, output_img='hist_kde.png', price_column = "Valor_unit_prod"):
  sns.histplot(data=df_model, x=price_column, kde=True)
  plt.savefig(output_img)
  print(output_img,': OK')


def graph(df_data, text_column, price_column, output='graph', neighbors=6):

  neigh = NearestNeighbors(n_neighbors=neighbors, metric='cosine')
  neigh.fit(np.array(df_data[['umap_emb_x','umap_emb_y']]))
  _,instances  = neigh.kneighbors(np.array(df_data[['umap_emb_x','umap_emb_y']]))

  nodes = {}
  edges = []

  for v in instances:
    counter = 0
    for id in v:
      price = df_data.iloc[id][price_column]
      title = df_data.iloc[id][text_column]+' | R$ '+str(price)
      size = int(df_data.iloc[id][price_column])+1
      x = df_data.iloc[id]['umap_emb_x']
      y = df_data.iloc[id]['umap_emb_y']
      price_bin = df_data.iloc[id]['price_bin']

      if id not in nodes:
        node_desc = {
          'id': int(id),
          'label': title,
          'title': f'NFe ID: {str(id)}',
          'value': size, 
          'group': int(price_bin),
          'x': float(100*x),
          'y': float(100*y)
        }
        nodes[id] = node_desc
      
      if counter > 0:
        edges.append({'from': int(v[0]), 'to': int(v[counter])})
      
      counter += 1
  data = {'nodes': list(nodes.values()), 'edges': edges}

  json_file = os.path.join('nfeminer', 'util', f'{output}.json') 
  with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)
  print(json_file,': OK')


  js_code = 'var nodes = ' + json.dumps(data['nodes'], indent=4) + ';\n'
  js_code += 'var edges = ' + json.dumps(data['edges'], indent=4) + ';\n'

  js_file = os.path.join('nfeminer', 'util', f'{output}.js')
  with open(js_file, 'w') as f:
    f.write(js_code)
  print(js_file,': OK')
