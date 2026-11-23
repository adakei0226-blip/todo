def main():
    while True:
        print("1: あいさつ  0: 終了  2:さようなら")
        choice = input("番号を選んでください > ")

        if choice == "1":
            print("こんにちは！")
        elif choice == "0":
            print("終了します")
        elif choice == "2":
            print("さようでございますか")
            break
        else:
            print("その番号はありません")