import alpha
from alpha import Alpha
from alpha import scheduler

if __name__ == "__main__":
    alpha.client = Alpha

    scheduler.start()

    Alpha.run()
