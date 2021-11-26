from flask import Flask, render_template, request, redirect
from threading import Thread

app = Flask('')

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    return redirect(f"https://pl8u5p7v00.execute-api.us-east-2.amazonaws.com/default/ciphey_lambda_api?ctext={request.form.get('mysterytext')}")
  elif request.method == 'GET':
    return render_template('index.html')
  return render_template("index.html")

@app.route('/<qry>')
def redirect_to_api(qry):
  return redirect(f"https://pl8u5p7v00.execute-api.us-east-2.amazonaws.com/default/ciphey_lambda_api?ctext={qry}")


def run():
  app.run(host='0.0.0.0')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    run()