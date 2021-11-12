# in your python file
@app.route('/')

def index():
  return "<h1>Mario is my Spanish teacher </h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
