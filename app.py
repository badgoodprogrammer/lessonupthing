from flask import Flask, render_template, request
import lessonupbots
import threading

app = Flask(__name__)

# Functie die de taak in een nieuwe thread start
def run_spam(user_input):
    print("Starting the bot task...")
    names = ["bot_bot_bot_bot_bot_bot"]
    pin = user_input
    much = 999999  # Je kunt hier variabelen aanpassen
    thread_spawner1 = threading.Thread(target=lessonupbots.spawn_player, args=(pin, much, names))
    thread_spawner1.start()
    print("Bot task started in a new thread.")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        user_input = request.form['pincode_userinput']
        run_spam(user_input)  # Start de bot task in de achtergrond
        result = "Bot task started, check je console voor output!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
