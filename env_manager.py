from os import environ

class EnvManager:
    def __init__(self):
        # Flask
        self.debug = environ.get('DEBUG') == 'True'
        self.host = environ.get('HOST')
        self.port = int(environ.get('PORT').strip('"'))

        # OpenSearch
        self.opensearch_host = environ.get('OPENSEARCH_HOST')
        self.opensearch_port = int(environ.get('OPENSEARCH_PORT').strip('"'))
        self.opensearch_username = environ.get('OPENSEARCH_USERNAME')
        self.opensearch_password = environ.get('OPENSEARCH_PASSWORD')

default_env_manager = EnvManager()

def get_env_manager():
    return default_env_manager
