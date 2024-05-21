from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    email = request.form['email']

    # Создаем cookie с данными пользователя
    response = make_response(redirect(url_for('welcome')))
    response.set_cookie('user', value=f'{name},{email}')
    return response


@app.route('/welcome')
def welcome():
    # Проверяем, существует ли cookie с данными пользователя
    user_data = request.cookies.get('user')
    if user_data:
        name, _ = user_data.split(',')
        return render_template('welcome.html', name=name)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # Удаляем cookie с данными пользователя
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
