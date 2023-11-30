from flask import Flask, render_template

app = Flask(__name__)

def generate_plot():
    # No plot for now, return an empty string
    return ''

@app.route('/')
def index():
    plot_html = generate_plot()
    return render_template('index.html', plot_html=plot_html)

@app.route('/rates')
def rates():
    return render_template('rates.html')

if __name__ == '__main__':
    app.run(debug=True)
