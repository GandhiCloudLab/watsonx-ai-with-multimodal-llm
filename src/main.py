
from flask import Flask, request, jsonify, render_template, send_file
import logging
import os

from dotenv import load_dotenv
from api.ApiMultiModelLlm import apiMultimodelLlm


# Initialize Flask app
app = Flask(__name__, static_folder='static')

# Load environment variables
load_dotenv()

#### Logging Configuration
logging.basicConfig(
    format='%(asctime)s - %(levelname)s:%(message)s',
    handlers=[
        logging.StreamHandler(),  # print to console
    ],
)

logger = logging.getLogger(__name__)

app.register_blueprint(apiMultimodelLlm)

@app.route('/')
def index():
    logger.info("main home page")
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "hello", 200

@app.route('/index', methods=['POST'])
def execute_main():
    logger.info("Processing Started")

    # Check if a file was uploaded
    if 'uploadFile' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # Get the uploaded file
    file = request.files['uploadFile']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file to the 'data' folder
    file_path = os.path.join('data', file.filename)
    file.save(file_path)

    logger.info(f"File saved to: {file_path}")

    return {    "message": "Processing completed successfully",
                "file_name":file_path,
                "table_data":{}}


@app.route('/download', methods=['GET'])
def download_file():
    # Get the file path from query parameters
    file_path = request.args.get('file_path')
    
    if file_path:
        # Serve the file for download
        return send_file(file_path, as_attachment=True)
    else:
        return "No file specified", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=False)


### Main method
def main():
    logger.info("main started .....")

    ### Run the app
    app.run(host ='0.0.0.0', port = 3001, debug = False)

if __name__ == '__main__':
    main()