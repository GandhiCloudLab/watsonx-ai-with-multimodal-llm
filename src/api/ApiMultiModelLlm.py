from flask import Blueprint, jsonify, request, current_app, send_file
import logging, os

from multimodel_llm.MultiModellmMain import MultiModelLlmMain

apiMultimodelLlm = Blueprint('api_multimodel_llm', __name__)

logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get('LOGLEVEL', 'INFO').upper())

@apiMultimodelLlm.route('/api/query', methods=['POST'])
def query():
    logger.info("apiMultimodelLlm  : /api/query ...")

    payload = request.get_json()

    ### Call the main function to get the response
    multiModelLlmMain = MultiModelLlmMain()
    resp = multiModelLlmMain.query(payload)

    return resp, 200

@apiMultimodelLlm.route('/api/welcome', methods=['GET'])
def welcome_message():
    resp = {"msg" : "welcome"}
    return resp, 200

