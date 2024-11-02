from flask import Flask, render_template, request, redirect

from opensearch import get_query, get_doc
from env_manager import get_env_manager

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('q').strip()

    if len(q) == 0:
        return redirect('/', code=307)
    if len(q) > 32:
        return render_template('index.html', error='Query too long'), 400
    
    results = get_query(q, size=32)
    if results['hits']['total']['value'] == 0:
        return render_template('index.html', query=q, error='No results found')
    
    if 'error' in results:
        return render_template('search.html', query=q, error=results['error'])
    
    res = []
    for result in results['hits']['hits']:
        res.append((result['_score'], result['_source']))
    
    return render_template('search.html', query=q, results=results)

@app.route('/doc', methods=['GET'])
def doc():
    index = request.args.get('index')
    id = request.args.get('id')

    if index is None or id is None:
        return redirect('/', code=307)

    try:
        results = get_doc(index=index, id=id)
    except Exception as _:
        return render_template('x404.html', error='No results found'), 404
    return render_template('doc.html', results=results)

def main():
    env = get_env_manager()
    app.run(debug=env.debug, host=env.host, port=env.port)

if __name__ == '__main__':
    main()