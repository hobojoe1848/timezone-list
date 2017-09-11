#!python3
# This is the application script for launching
# a Python Timezone List Flask Web App.

from flask import Flask, render_template, request

from tz.timezones import create_list, get_tz_time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    tz_list = create_list()
    choice = ''
    tz_time = ''
    if request.method == 'POST' and 'tz_menu' in request.form:
        choice = request.form.get('tz_menu')
        tz_time = get_tz_time(choice)
    return render_template('index.html',
                           tz_list=tz_list,
                           choice=choice,
                           tz_time=tz_time)


if __name__ == "__main__":
    app.run()
