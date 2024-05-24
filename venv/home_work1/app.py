from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', title='Главная')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html', title='Одежда', category_name='Одежда')

@app.route('/shoes')
def shoes():
    return render_template('shoes.html', title='Обувь', category_name='Обувь')

@app.route('/jacket')
def jacket():
    return render_template('jacket.html', title='Куртка', product_name='Куртка')

if __name__ == '__main__':
    app.run(debug=True)