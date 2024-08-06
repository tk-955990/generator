# Countdownクラスの定義（イテレーター）
class Countdown:
    def __init__(self, start):
        self.number = start  # 初期カウントの値をインスタンス変数に格納

    def __iter__(self):
        return self  # イテレーター自身を返す

    def __next__(self):
        if self.number <= 0:  # カウントが0以下になったらStopIterationを投げる
            raise StopIteration
        r = self.number  # 現在のカウントの値を一時変数に格納
        self.number -= 1  # カウントを1減らす
        return r  # 現在のカウントの値を返す


# Countdownクラスのインスタンスを作成
countdown = Countdown(10)

# forループを使用してカウントダウンを出力
for i in countdown:
    print(i)  # 現在のカウントの値を出力
