from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    file_type = request.args.get('file_type')
    
    if query:
        google_search_url = f"https://www.google.com/search?q={query}+filetype:{file_type}"
        return redirect(google_search_url)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
