from flask import Flask,request,jsonify,json
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def processjson():
    with open('temp.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True,host= '0.0.0.0',port='7000')
