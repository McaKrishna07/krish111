from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Must match the frontend HTML filename

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_to_csv(data)
        return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for applying! We will contact you soon.</h2>"

def save_to_csv(data):
    file_exists = os.path.isfile('submissions.csv')
    with open('submissions.csv', mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'email', 'phone', 'linkedin', 'github', 'portfolio', 'resume', 'cover', 'interest']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

if __name__ == '__main__':
    app.run(debug=True)
