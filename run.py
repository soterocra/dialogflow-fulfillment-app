import os
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "A nossa API está <span style='color: green; font-size: 30px'>online</span> em /api/"

@app.route('/api/', methods=['POST'])
def api():
    if request.headers.get('Authorization') == 'Basic bWV1dXN1YXJpbzptaW5oYXNlbmhh':
        rq_body = request.get_json()

        if rq_body['result']['metadata']['intentName'] == 'Consultar_Hora':
            response = rq_body['result']['parameters']['date-time'][11:19]
                if response == '':
                    response = datetime.now().strftime('%H:%M:%S')
                    response = "Sem parametro " + response
                else:
                    response = "Com parametro " + response

            return jsonify(
                {
                    "speech": "Falar " + response,
                    "displayText": "Mostrar " + response,
                    "data": {
                        "facebook": {
                            "text": "Facebook " + response
                        },
                        "slack": {
                            "text": "Slack " + response
                        },
                        "telegram": {
                            "text": "Telegram " + response
                        }
                    }
                }
            )

        negativeResponse = "nao entendi"
        return jsonify(
            {
                "speech": "Falar " + negativeResponse,
                "displayText": "Mostrar " + negativeResponse,
                "data": {
                    "facebook": {
                        "text": "Facebook " + negativeResponse
                    },
                    "slack": {
                        "text": "Slack " + negativeResponse
                    },
                    "telegram": {
                        "text": "Telegram " + negativeResponse
                    }
                }
            }
        )

    return jsonify(
        {
            "message": "Nao foi possivel te autenticar"
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
