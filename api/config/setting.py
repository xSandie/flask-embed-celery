#celery设置
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/'
CELERY_TIMEZONE = 'Asia/Shanghai'