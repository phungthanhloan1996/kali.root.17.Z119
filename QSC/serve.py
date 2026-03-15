from waitress import serve
from QSC.wsgi import application
serve(application, host="0.0.0.0", port=9999, threads=8, connection_limit=100, backlog=128)
