import json
import os
from waitress import serve


with open('config.json') as json_data_file:
    data = json_data_file.read()

os.environ['settings'] = data;
settings = json.loads(data)

from all_controllers import app


app.secret_key = 'thisIsMySecretKey'


if __name__ == '__main__':

    app.debug = True
    server = settings["server"]
    serve(app, listen='{host}:{port}'.format(port=server["port"], host=server["host"]))

