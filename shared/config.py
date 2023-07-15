from decouple import config

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', cast=str)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', cast=str)
