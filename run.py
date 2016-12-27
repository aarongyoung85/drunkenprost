from flask import Flask, render_template, send_from_directory
from models.homepage_model import HomePage
app = Flask(__name__)
logger = app.logger
app.config.from_object('config')

def get_topics():
    model = HomePage()
    topics = None
    try:
        topics = model.get_topics()
    except Exception, e:
        logger.error("ERROR %s %s"%(type(e), str(e)))

    return topics

@app.route('/cdn/<path:filename>')
def custom_static(filename):
    parts = filename.split('.')
    return send_from_directory(app.config['STATIC_PATHS'][parts[1]], filename)

@app.route('/beers')
def beer_page():
    ret_dict = {}
    ret_dict['topics'] = get_topics()
    return render_template('beers.html', ret_dict=ret_dict)

@app.route('/')
def index():
    ret_dict = {}
    ret_dict['topics'] = get_topics()
    return render_template('index.html', ret_dict=ret_dict)
    
if __name__ == '__main__':
    app.run()
