from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
from werkzeug.utils import secure_filename
from model import initialize_model, create_agent, data_mining_assistant
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 MB max size

# Initialize model and default DataFrame
llm = initialize_model()
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZNoKMJ9rssJn-QbJ49kOzA/student-mat.csv")
agent = create_agent(llm, df)

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['csv']

# Route to render the HTML page with file upload form
@app.route('/')
def index():
    global df  # Ensure df is accessible globally
    return render_template('index.html', df=df)

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    global df, agent  # Ensure df and agent are accessible globally
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Read the uploaded file
        df = pd.read_csv(filepath)
        agent = create_agent(llm, df)
        
        return jsonify({"message": "File uploaded successfully"})
    
    else:
        return jsonify({"error": "Invalid file type"})

# Route to handle queries
@app.route('/query', methods=['POST'])
def query():
    global agent
    query = request.json.get('query')
    response = data_mining_assistant(agent, query)
    output = response['output']
    
    if 'plot' in query.lower():
        code = response['intermediate_steps'][0][0].tool_input.replace('; ', '\n')
        
        # Execute code to generate plot
        exec(code)
        
        # Save plot image to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        
        # Encode plot image to base64
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        
        # Return response with output and plot URL
        return jsonify({"output": output, "plot_url": f"data:image/png;base64,{plot_url}"})
    
    return jsonify({"output": output})

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
