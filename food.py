from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Pre-defined questions and responses
qa_pairs = {
    "what is your name?": "My name is restaurantbot. 😊",
    "how are you?": "I'm doing well, thank you! 💪",
    "hey": "Hey, how can I help you? You may place your orders. 🍽️",
    "thanks": "Enjoy your meal! 😋",
    "what is at the menu?": "Fried rice and Chicken, Fried plantains and Chicken, White rice and Snail sauce, Water fufu or Garry and eru. 🍛",
    "what do you have as drink": "Fruit juice, Heineken, Bavaria, Malta. 🥤🍺",
    "fried rice and chicken": "N5,000. 💰",
    "fried plantains and chicken": "N4,000. 💰",
    "white rice and snail sauce": "N3,000. 💰",
    "water fufu or garry and eru": "N3,000. 💰",
    "sandwish": "N3,000. 💰",
    "cocktails": "N3,000. 💰",
    "Fruit Salad": "N3,000. 💰",
    "hamburger": "N2500",
    "bye": "Thanks for coming, hope you were satisfied. See you next time! 👋",
    "fruit juice": "N1,000. 💰",
    "heineken": "N2,000. 💰",
    "bavaria": "N2,000. 💰",
    "malta": "N1,000. 💰",
    "milk shake": "N1,000. 💰"
    # Add more question-answer pairs as needed
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question'].lower()  # Convert user's question to lowercase
    question_lower = question.lower()  # Convert user's question to lowercase
    answer = qa_pairs.get(question_lower, "Sorry, I don't understand that question. 🤔")
    return jsonify({'answer': answer})

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
