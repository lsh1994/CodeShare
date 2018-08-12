from flask import Flask, render_template,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!', 400
    return render_template('index.html')

@app.route('/dataanalyse')
def data_analyse():
    return render_template('dataanalyse.html')

@app.route('/dataanalyse/loccounts')
def loc_counts():
    import data_analyse
    dic,uknow=data_analyse.loc_counts()

    ary=[]
    for i in dic.keys():
        ary.append({"name":i,"value":dic[i]})

    # ary.append({"name": "未知地名", "value": uknow})
    return jsonify(ary)

if __name__ == '__main__':
    app.run(debug=True)
