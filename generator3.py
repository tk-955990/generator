import re  # 正規表現モジュールをインポート

# イテラブル：__iter__メソッドが必要

# CountVowelsGen関数の定義（ジェネレーター）


def CountVowelsGen(sentence: str):
    # 単語を見つけるための正規表現パターンをコンパイル
    pat = re.compile(r'\w+')
    # 文から単語を抽出し、イテレータを取得
    words_iter = pat.finditer(sentence)

    # 各単語ごとに母音の数をカウントして生成する
    for word_match in words_iter:
        vowels = 0
        # 現在の単語を取得
        word = word_match.group()
        # 単語内の各文字について母音をカウント
        for c in word:
            if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels += 1
        # 現在の単語とその母音の数をタプルとして生成
        yield (word, vowels)


# CountVowelsGen関数を使用してジェネレーターオブジェクトを作成
res = CountVowelsGen('"Extremely interesting", he suddenly shouted loudly.')

# ジェネレーターオブジェクトからイテレータを取得
it = iter(res)
# ジェネレーターから次の値を取得して表示
print(next(it))  # 最初の単語とその母音の数を出力
print(next(it))  # 次の単語とその母音の数を出力
print(next(it))  # 以下同様
print(next(it))
print(next(it))
print(next(it))
