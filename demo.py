# -*- coding: utf-8 -*-
from gensim import models
def main():
	model = models.Word2Vec.load('word2vec.model')

	try:

		for word in ['月','蟾','嫦娥','兔','中秋','赏月','桂花','花灯','饼','桂花']:
			q_list = word.split()
			if len(q_list) == 1:
				topn = 5
				print("相似詞前 %d 排序"%topn)
				res = model.wv.most_similar(q_list[0],topn = topn)

				for item in res:
					print(word,'-->',item[0]+","+str(item[1]))

	except Exception as e:
		print(repr(e))

if __name__ == "__main__":
	main()
