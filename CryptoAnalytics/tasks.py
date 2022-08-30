from CryptoAnalytics.celery import app


@app.task
def supper_sum(x, y):
    return x + y

