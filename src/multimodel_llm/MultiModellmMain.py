import os
import logging
from xml.dom.minidom import Document 
from dotenv import load_dotenv

import logging 
import os, json

from util.DictionaryUtil import DictionaryUtil
from llm.LlmMain import LlmMain

from CommonConstants import *

class MultiModelLlmMain(object):

    def __init__(
        self
    ) -> None:
        load_dotenv()
        self._init_config()

    def _init_config(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(os.environ.get('LOGLEVEL', 'INFO').upper())

    def query(self, payload):
        self.logger.info("MultiModelLlmMain : query started ... ")
        
        ### Retrive parameters
        image_url = payload["image_url"]
        question = payload["question"]

        ### Get watsonx model
        llmMain = LlmMain()
        model = llmMain.get_watsonx_model()

        ### query watsonx model
        result = llmMain.callWatsonx_multimodel (model, image_url, question)
        resp = {
            "msg" : "Success",
            "result" : result
        }

        self.logger.info("MultiModelLlmMain : query completed ... ")

        return resp