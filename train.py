# -*- coding: utf-8 -*-

import logging
from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("poem.txt")
    model = word2vec.Word2Vec(sentences, vector_size=250, epochs=100)

    #保存模型，供日後使用
    model.save("word2vec.model")

if __name__ == "__main__":
    main()
