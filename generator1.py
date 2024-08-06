import re  # 正規表現モジュールをインポート

# イテラブル：__iter__メソッドが必要

# CountVowelsGen関数の定義（ジェネレーター）


def CountVowelsGen(sentence: str):
    # 単語を見つけるための正規表現パターンをコンパイル
    pat = re.compile(r'\w+')
    # 文から単語を抽出してリストに格納
    words = pat.findall(sentence)

    # 各単語ごとに母音の数をカウントして生成する
    for word in words:
        vowels = 0
        for c in word:
            if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels += 1
        # 現在の単語とその母音の数をタプルとして生成
        yield (word, vowels)


# CountVowelsGen関数を使用してイテレータを作成
res = CountVowelsGen('"Extremely interesting", he suddenly shouted loudly.')

# イテレータを作成して使用する
it = iter(res)
print(next(it))  # 最初の単語とその母音の数を出力
print(next(it))  # 次の単語とその母音の数を出力
