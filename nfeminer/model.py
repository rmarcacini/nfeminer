from nltk.corpus import stopwords
from nltk import download
import numpy as np
import umap
from sklearn.preprocessing import KBinsDiscretizer
import pandas as pd 
from gensim.test.utils import datapath
from gensim.models import KeyedVectors

download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('portuguese')



def preprocess(sentence):
    return [w.upper() for w in sentence.lower().split() if w not in stop_words]

def get_word_ft_embedding(nfe_desc, model_ft):
  tokens = preprocess(nfe_desc)
  L = []
  for token in tokens:
    try:
      L.append(model_ft[token])
    except:
      1
  if len(L) > 0:
    return np.mean(np.array(L),axis=0)
  else:
    return np.array([-1])


def manifold(df_query, text_column, price_column, embeddings='nfe_embeddings.vec', training_size=15, neighbors=6, feedback='auto'):

  model_ft = KeyedVectors.load_word2vec_format(embeddings, binary=False)

  X = []
  Y = []
  I = []

  # feedback = auto 
  # text_column = 'Descricao_do_Produto_ou_servicos' (NFE SAMPLE)
  counter_sampling = 0
  for index,row in df_query.iterrows():
    if counter_sampling < training_size:
      v = get_word_ft_embedding(row[text_column],model_ft)
      if len(v) != 1:
        I.append(index)
        X.append(v)
        Y.append(1)
    else:
      if counter_sampling > len(df_query)-training_size:
          v = get_word_ft_embedding(row[text_column],model_ft)
          if len(v) != 1:
            I.append(index)
            X.append(v)
            Y.append(0)
      else:
          v = get_word_ft_embedding(row[text_column],model_ft)
          if len(v) != 1:
            I.append(index)
            X.append(v)
            Y.append(-1)



    counter_sampling+=1


  umap_nfe_model = umap.UMAP(metric='cosine',n_neighbors=neighbors).fit(X, y=Y)
  embedding_umap = umap_nfe_model.transform(X)
  df_data = df_query.iloc[I]
  df_umap = pd.DataFrame(embedding_umap)
  df_data['umap_emb_x'] = df_umap[0]
  df_data['umap_emb_y'] = df_umap[1]
  df_data['umap_label'] = Y
  df_data['nfe_emb'] = list(X)

  #price_column = 'Valor_unit_prod'
  est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans')
  est.fit(df_data[[price_column]])

  Xt = est.transform(df_data[[price_column]])

  df_data['price_bin'] = pd.DataFrame(Xt)[0]

  return df_data
