from . import embed_celery

@embed_celery.task()
def add_task(a,b):
    return a+b

@embed_celery.task()
def factorial_task(a,b):
    return a*b