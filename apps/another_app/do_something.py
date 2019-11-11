import time


def slow_function(make_progress_func):
    """裏側で動いている時間のかかる処理"""

    for i in range(100):
        time.sleep(0.1)
        if i % 10 == 0:
            make_progress_func()

    return "処理完了"
