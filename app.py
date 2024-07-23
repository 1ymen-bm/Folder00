from datetime import datetime, timedelta
from flask import Flask, request, render_template

app = Flask(__name__)

def count_days_without_fridays(start_date_str, discount_days):
    try:
        start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
        current_date = datetime.now()
        days_count = 0

        while start_date < current_date:
            if start_date.weekday() != 4:  # 4 corresponds to Friday
                days_count += 1
            start_date += timedelta(days=1)

        # Apply the discount
        days_count -= discount_days
        if days_count < 0:
            days_count = 0  # Ensure the count doesn't go negative

        return days_count
    except ValueError:
        return "Invalid date format. Please use DD-MM-YYYY."

@app.route('/', methods=['GET', 'POST'])
def home():
    fixed_start_date = "13-07-2024"
    result = None
    discount_days = 0

    if request.method == 'POST':
        try:
            discount_days = int(request.form['discount_days'])
        except ValueError:
            discount_days = 0
        result = count_days_without_fridays(fixed_start_date, discount_days)

    return render_template('index.html', fixed_start_date=fixed_start_date, discount_days=discount_days, result=result)

if __name__ == '__main__':
    app.run(debug=True)
