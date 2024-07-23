from datetime import datetime, timedelta
from flask import Flask, request, render_template_string

app = Flask(__name__)

def count_days_without_fridays(start_date_str):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        days_count = 0

        while start_date < current_date:
            if start_date.weekday() != 4:  # 4 corresponds to Friday
                days_count += 1
            start_date += timedelta(days=1)

        return days_count
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

@app.route('/')
def home():
    return '''
        <h1>Count Days Excluding Fridays</h1>
        <form action="/result" method="post">
            <label for="start_date">Start Date (YYYY-MM-DD):</label><br><br>
            <input type="text" id="start_date" name="start_date"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result', methods=['POST'])
def result():
    start_date_str = request.form['start_date']
    result = count_days_without_fridays(start_date_str)
    return render_template_string('''
        <h1>Result</h1>
        <p>Days between {{ start_date_str }} and today (excluding Fridays): {{ result }}</p>
        <a href="/">Back</a>
    ''', start_date_str=start_date_str, result=result)

if __name__ == '__main__':
    app.run(debug=True
