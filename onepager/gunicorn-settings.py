#bind = "0.0.0.0:8000"
bind = "unix:/tmp/gunicorn_onepager.sock"

workers = 2
proc_name = "onepager"
#loglevel = 'debug'
