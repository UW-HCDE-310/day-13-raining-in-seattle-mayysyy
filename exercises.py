from flask import Flask
import urllib.request

app = Flask(__name__)

def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    return is_it_raining_in_seattle == "true"

@app.route('/')
def check_weather():
    if is_it_raining_in_seattle():
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    app.run(debug=True)