#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

# ストップウォッチクラス
class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0

    # 現在の時刻をstart_timeに記録
    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
        elif self.elapsed_time > 0:
            self.start_time = time.time() - self.elapsed_time
            self.elapsed_time = 0

    # 現在の時刻とstart_timeの差を計算しelapsed_timeに加算
    def stop(self):
        if self.start_time is not None and self.elapsed_time == 0:
            self.elapsed_time = time.time() - self.start_time
        print(f"Elapsed Time: {self.elapsed_time:.2f} seconds")

    # 全てのインスタンス変数を初期状態に戻す
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0

    # 現在までの経過時間を表示
    def show(self):
        if self.start_time is None:
            print("Elapsed Time: 0.00 seconds")
        elif self.elapsed_time == 0:
            print(f"Elapsed Time: {time.time() - self.start_time:.2f} seconds")
        else:
            print(f"Elapsed Time: {self.elapsed_time:.2f} seconds")

# メイン関数
def main():
    stopwatch = Stopwatch()
    while True:
        operation = input('ストップウォッチを操作してください。(start/stop/reset/show/exit): ').strip().lower()
        match operation:
            case 'start':
                stopwatch.start()
            case 'stop':
                stopwatch.stop()
            case 'reset':
                stopwatch.reset()
            case 'show':
                stopwatch.show()
            case 'exit':
                print("ストップウォッチを終了します。")
                break
            case _:
                print("無効な操作です。もう一度試してください。")

if __name__ == "__main__":
    main()
