from kata_api_entreprise import app


@app.route('/entreprise', methods=['GET'])
def entreprise():
    return 'Hello World!'
