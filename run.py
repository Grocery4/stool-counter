from flaskr import app

# __name__ special string returns __main__ if executed directly while not being imported
if '___name__' == '__main__':
    app.run(debug=True)