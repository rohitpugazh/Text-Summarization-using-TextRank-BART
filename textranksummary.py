import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import re
from nltk.corpus import stopwords
import networkx as nx


def generate_textrank(DOCUMENT, sn):
  sentences = []
  sentences.append(sent_tokenize(DOCUMENT)) 
  sentences = [y for x in sentences for y in x] 
  cleaned_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ", regex=True)
  cleaned_sentences = [s.lower() for s in cleaned_sentences]

  stop_words = stopwords.words('english')

  def remove_stopwords(sen):
    new_sent = " ".join([i for i in sen if i not in stop_words])
    return new_sent
  cleaned_sentences = [remove_stopwords(r.split()) for r in cleaned_sentences]

  glove_embeddings = {}
  f = open('glove.6B.100d.txt', encoding='utf-8')
  for line in f:
      values = line.split()
      word = values[0]
      coefs = np.asarray(values[1:], dtype='float32')
      glove_embeddings[word] = coefs
  f.close()

  sentence_vectors = []
  for i in cleaned_sentences:
    if len(i) != 0:
      v = sum([glove_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
    else:
      v = np.zeros((100,))
    sentence_vectors.append(v)
  len(sentence_vectors)

  sim_matrix = np.zeros([len(sentences), len(sentences)])
  from sklearn.metrics.pairwise import cosine_similarity

  for i in range(len(sentences)):
    for j in range(len(sentences)):
      if i != j:
        sim_matrix[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

  nx_graph = nx.from_numpy_array(sim_matrix)
  scores = nx.pagerank(nx_graph)

  ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
  summary = ""
  # Generate summary
  for i in range(sn):
    summary = summary + ranked_sentences[i][1] + " "
  return summary