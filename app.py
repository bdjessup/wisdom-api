from flask import Flask, jsonify
import requests
import random

def create_app():
    app = Flask(__name__)

    def fetch_wisdom_list():
        url = "https://raw.githubusercontent.com/merlinmann/wisdom/master/wisdom.md"
        response = requests.get(url)
        wisdom_section = response.text.split("## The Wisdom So Far\n")[1].split("\n## ")[0]
        wisdom_list = [line.strip().encode('utf-8').decode('unicode-escape').lstrip('-').strip().strip('"').strip() for line in wisdom_section.split('\n') if line.startswith('-') and "----" not in line]
        return wisdom_list

    @app.route('/wisdom', methods=['GET'])
    def get_wisdom():
        wisdom_list = fetch_wisdom_list()
        return jsonify(wisdom_list)

    @app.route('/wisdom/random', methods=['GET'])
    def get_random_wisdom():
        wisdom_list = fetch_wisdom_list()
        random_wisdom = random.choice(wisdom_list)
        return jsonify(random_wisdom)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
