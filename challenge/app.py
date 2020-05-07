from flask import Flask, render_template, request

app = Flask(__name__)
# is the name of the file

# route handler index
@app.route('/')
def index():
    #return a html file
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        num = request.form['num']
        nums = range(1,int(num)+1)
        return render_template('results.html', num=num, nums=nums)
    
    return render_template('index.html')

# if __name__ == '__main__':
    # app.run(debug=True)
