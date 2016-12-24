from flask import Flask, render_template
app = Flask(__name__)
logger = app.logger

@app.route('/')
def index():
    logger.error("test logging")
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()
