DB_SETTINGS = {
    'host': 'localhost',
    'user': 'webpush',
    'password': 'password',
    'database': 'webpush',
}

WEB_SETTINGS = {
    'host': 'localhost',
    'port': '8080',
    'cors_origins': 'http://localhost:11434',
    'public_address': 'http://localhost:8080',
    'debug': True,
    'use_reloader': False,
}

LOG_SETTINGS = {
    'level': 'DEBUG',
    'path': 'log',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}