from collections import abc
import re  # 正規表現モジュールをインポート

# イテレーター　__iter__,__next__メソッドが必要
# イテラブル　　__iter__メソッドが必要


# CountVowelsクラスの定義（イテレーター）


class CountVowels:

    # 単語を見つけるための正規表現パターンをコンパイル
    pat = re.compile(r'\w+')

    # コンストラクタ
    def __init__(self, sentence) -> None:
        # 渡された文をインスタンス変数に格納
        self.sentence = sentence
        # 正規表現パターンを使って文から単語を抽出しリストに格納
        self.words = self.pat.findall(sentence)
        # 現在の単語のインデックスを初期化
        self.index = 0

    # 次の単語とその母音の数を返すメソッド
    def __next__(self):
        # インデックスが単語リストの長さ以上になったらStopIterationを投げる
        if self.index >= len(self.words):
            raise StopIteration

        # 現在の単語を取得し、インデックスを進める
        current_word = self.words[self.index]
        self.index += 1

        # 現在の単語の母音の数をカウント
        vowels = 0
        for c in current_word:
            if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels += 1

        # 現在の単語とその母音の数をタプルとして返す
        return (current_word, vowels)

    # イテレータオブジェクトを返すメソッド
    def __iter__(self):
        return self

# イテラブルオブジェクトとしての動作を持つカスタムクラスMyCountの定義

# MyCountクラスの定義（イテラブル）


class MyCount:

    # コンストラクタ
    def __init__(self, sentence):
        self.sentence = sentence

    # イテレータを返すメソッド
    def __iter__(self):
        return CountVowels(self.sentence)


# CountVowelsクラスのインスタンスを作成
res = CountVowels('"Extremely interesting", he suddenly shouted loudly.')

# CountVowelsインスタンスをforループで反復処理
for c in res:
    print(c)  # 各単語とその母音の数を出力する


print(issubclass(MyCount, abc.Iterable))
print(issubclass(CountVowels, abc.Iterator))


# # resのイテレータを作成
# s_iter = iter(res)

# # 無限ループでイテレータを処理
# while True:
#     try:
#         # イテレータから次の要素を取得して出力
#         print(next(s_iter))
#     except StopIteration:
#         # イテレータが終了したらStopIteration例外が発生する
#         # イテレータを削除してループを終了
#         del s_iter
#         break


# # MyCountインスタンスをforループで反復処理
# for c in res:
#     print(c)  # 各単語とその母音の数を出力する
