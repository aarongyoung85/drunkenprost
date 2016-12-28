from flask import Flask, render_template, send_from_directory
from models.homepage_model import HomePage
app = Flask(__name__)
logger = app.logger
app.config.from_object('config')

def get_topics(homepage_model):
    topics = None
    try:
        topics = homepage_model.get_topics()
    except Exception, e:
        logger.error("Something went wrong getting topics %s %s"%(type(e), str(e)))

    return topics

@app.route('/cdn/<path:filename>')
def custom_static(filename):
    parts = filename.split('.')
    return send_from_directory(app.config['STATIC_PATHS'][parts[1]], filename)

@app.route('/beer')
def beer_page():
    model = HomePage()
    ret_dict = {}
    ret_dict['topics'] = get_topics(model)
    return render_template('beer.html', ret_dict=ret_dict)

@app.route('/wine')
def wine_page():
    model = HomePage()
    ret_dict = {}
    ret_dict['topics'] = get_topics(model)
    return render_template('wine.html', ret_dict=ret_dict)

@app.route('/')
def index():
    model = HomePage()
    ret_dict = {}
    ret_dict['topics'] = get_topics(model)

    try:
        ret_dict['recent_entries'] = model.get_recent_entries_by_topic()
    except Exception, e:
        ret_dict['recent_entries'] = None
        logger.error("Something went wrong getting recent entries %s %s"%(type(e), str(e)))
        
    return render_template('index.html', ret_dict=ret_dict)
    
if __name__ == '__main__':
    app.run()
