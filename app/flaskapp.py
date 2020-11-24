from flask import Flask
from redis import Redis, RedisError
redis = Redis(host= "redis-server", db=0)

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1> Hello world ! </h1>"

@app.route('/visit')
def counter_incr():
    try:
        visits = redis.incr("counter")
    except:
        visits = "<i>cannot connect to redis server </i>"
    html = "<h1> Number of visits: {}</h1>".format(visits)
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 80)