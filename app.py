from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get today's date in format YYYY-MM-DD
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', today=today)

@app.route('/jobs/<date>')
def jobs_by_date(date):
    try:
        return render_template(f'../jobs/{date}.html')
    except:
        return "<h2>Job page not found for this date. Please check again later.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
