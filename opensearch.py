import sys

from opensearchpy import OpenSearch

from env_manager import get_env_manager

env = get_env_manager()

host = env.opensearch_host
port = env.opensearch_port
auth = (env.opensearch_username, env.opensearch_password)

client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,

    http_compress = True
)

if client.ping():
    print('Connection successful')
else:
    print('Connection failed')
    print(client.info())
    sys.exit(1)

def get_query(query: str, size: int = 20):
    # TODO: Add pagination
    # TODO: Add filters - filter the results, e.g. by language
    # TODO: Add sorting - to show most-accurate results first
    # TODO: Fix hardcoded fields
    return client.search(
        index='c_docs',
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": [],
                    "type": "best_fields"
                }
            },
            "size": size,
        }
    )

def get_doc(index: str, id: str):
    return client.get(index=index, id=id)