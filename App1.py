#From https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb
# Heroku needs to have a requirements.txt file or setup.py file. Don't forget to add gunicorn to them
#  and then make the procfile "web: gunicorn where_app_lives.py:app"


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def index():
     # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()
    # Increment the count
    count += 1
    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()
    # Render HTML with count variable
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()

