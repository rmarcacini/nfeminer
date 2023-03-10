import numpy as np
from sklearn.neighbors import NearestNeighbors
import seaborn as sns
import matplotlib.pyplot as plt

def hist_kde(df_model, output_img='hist_kde.png', price_column = "Valor_unit_prod"):
  sns.histplot(data=df_model, x=price_column, kde=True)
  plt.savefig(output_img)
  print(output_img,': OK')


def graph(df_data, text_column, price_column, output_js='graph.js', neighbors=6):

  neigh = NearestNeighbors(n_neighbors=6, metric='cosine')
  neigh.fit(np.array(df_data[['umap_emb_x','umap_emb_y']]))
  distances,instances  = neigh.kneighbors(np.array(df_data[['umap_emb_x','umap_emb_y']]))

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
        node_desc = '''
          {
              id: '''+str(id)+''',
              label: "'''+title+'''",
              title: "NFe ID: '''+str(id)+'''",
              value: '''+str(size)+''',
              group: '''+str(int(price_bin))+''',
              x: '''+str(x*100)+''',
              y: '''+str(y*100)+''',
          },
          '''
        nodes[id] = node_desc
      
      if counter > 0:
        edges.append('  { from: '+str(v[0])+', to: '+str(v[counter])+' },'+"\n")
      
      counter += 1

  with open(output_js, 'w') as f:
      f.write('var nodes = ['+"\n")  
      for node in nodes:
        f.write(nodes[node])
      f.write('];'+"\n\n")

      f.write('var edges = ['+"\n")
      for edge in edges:
        f.write(edge)
      f.write('];'+"\n")
  print(output_js,': OK')


