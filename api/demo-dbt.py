import decimal
import os
import openai
import psycopg
import simplejson

from dotenv import load_dotenv
from flask import Flask, json, jsonify, request
from flask_cors import CORS
from psycopg.rows import dict_row
from urllib.parse import urlparse

class MyJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/api/question", methods=["POST"])
def api_query():
    # demo query: curl --header "Content-Type: application/json"   --request POST --data '{"question": "how many customers are there?"}' https://acolyte-api.herokuapp.com/api/question
    question = request.get_json()['question']
    return jsonify(run(question))

def run(question, schema_path="examples/schema.yml"):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    for i in range(10):
        completion = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"""
            /* 
            example tables and columns:
            {get_table_info()}
            */

            /*
            examples:
            {get_examples()}
            */

            /* tables and columns:
            {get_table_info(schema_path)}
            */

            -- question: {question} 
            SELECT""",
            stop=[';', '"""'],
            max_tokens=250,
            temperature=0.5,
            frequency_penalty=1
        )

        query = f"SELECT {completion.choices[0].text}"
        has_error = False
        res = None
        try:
            res = run_query(query)
        except psycopg.Error as e:
            if i == 9:
                has_error = True
                print(e)
                res = [{'error': "Hmm, we couldn't figure that one out. Try asking a different way."}]
        if res is not None:
            return {"query": query, "res": res, "has_error": has_error}


def get_table_info(schema_path="examples/schema.yml"):
    return open(schema_path, 'r').read()

def get_examples():
    return open("examples/example_questions_and_answers.sql", 'r').read()

def run_query(codex_sql):
    if os.getenv('DATABASE_URL'):
        result = urlparse(os.getenv('DATABASE_URL'))
        USER = result.username
        PASSWORD = result.password
        DBNAME = result.path[1:]
        HOST = result.hostname
        PORT = result.port
    
    else:
        load_dotenv()

        HOST = os.getenv('DB_HOST')
        USER = os.getenv('DB_USER')
        DBNAME = os.getenv('DB_NAME')
        PASSWORD = os.environ.get('DB_PASSWORD')
        PORT = os.environ.get('DB_PORT')

    with psycopg.connect(f"host={HOST} user={USER} dbname={DBNAME} password={PASSWORD} port={PORT}", row_factory=dict_row) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute(codex_sql)
            return cur.fetchall()

#  main thread of execution to start the server
if __name__=='__main__':
   app.run(debug=True)