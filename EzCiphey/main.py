from flask import Flask, render_template, request
import requests
import base64

app = Flask('')
ciphey_api = 'https://pl8u5p7v00.execute-api.us-east-2.amazonaws.com/default/ciphey_lambda_api'
sorrytxt = "Sorry, this text could not be decoded with this tool:"

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    c_result = ciphey_api_query(request.form.get('mysterytext'))
    return render_template('result.html', cresult=c_result)
  elif request.method == 'GET':
    return render_template('index.html')
  else: return "I... Literally don't even know how to respond to that." 

@app.route('/<qry>')
def redirect_to_api(qry):
  c_result = ciphey_api_query(qry)
  return c_result

def ciphey_api_query(querytext) -> str:
  query_bytes = querytext.encode('ascii')
  base64_bytes = base64.b64encode(query_bytes)
  base64_query = base64_bytes.decode('ascii')
  try:
    rslt = requests.get(f"{ciphey_api}?ctext={base64_query}")
    if rslt.status_code == 200:
      return rslt.text
    else: return f"{sorrytxt} (raw: {querytext}) (as_b64: {base64_query})"
  except Exception as e:
    print(e)
    return "Whoops! Sorry! An error occurred, please try again later."

def run():
  app.run(host='0.0.0.0')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    run()