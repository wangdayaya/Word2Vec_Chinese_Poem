# 使用 gensim 训练 Word2Vec 向量


```
pip3 install jieba
pip3 install -U gensim
```

对 json 目录中的诗词进行分词，分字操作，这一步我已经处理生成了 song_tang.txt 文件，可以跳过。 json 中的诗词都来源于下方的仓库中的宋词和唐诗，这里只是存放了部分展示样例而已
```
python3 segment.py
```
用`gensim` 的 word2vec 模型進行訓練
```
python3 train.py
```
測試我們訓練出的模型
```
python3 demo.py
```

## 感谢诗词贡献者
https://github.com/chinese-poetry/chinese-poetry