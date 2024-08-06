def my_gen():
    # ジェネレーター関数の開始
    print("start")
    # 最初のyieldで"A"を生成
    yield "A"
    # "A"が消費された後、次のyieldへ進む
    print("continue")
    # 次のyieldで"B"を生成
    yield "B"
    # "B"が消費された後、終了の準備
    print("end")
    return  # ジェネレーター関数の終了


# ジェネレーター関数のインスタンスを作成
it = my_gen()
print(it)  # ジェネレーターオブジェクトを表示

# ジェネレーターから次の値を取得して表示
print(f"1: {next(it)}")  # "start" が表示された後、"A" が生成され、表示される
print(f"2: {next(it)}")  # "continue" が表示された後、"B" が生成され、表示される
print(f"3: {next(it)}")  # "end" が表示された後、StopIteration例外が発生し、表示されない
