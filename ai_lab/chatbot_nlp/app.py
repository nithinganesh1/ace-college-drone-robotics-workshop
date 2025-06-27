from flask import Flask, request, jsonify, render_template
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

# Initialize the app
app = Flask(__name__)

# Initialize NLTK
nltk.data.path.append('/home/nithin/nltk_data')  # Update this path as needed
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Read and preprocess your data
with open('Machine learning.txt', 'r', errors='ignore') as f:
    raw = f.read().lower()

sentence_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Lemmatization
lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def lem_tokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def lem_normalize(text):
    return lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greeting responses
GREETING_INPUTS = ('hello', 'hi', 'greetings', 'sup', "what's up", 'hey',)
GREETING_RESPONSES = ['hi', 'hey', '*nods*', 'hi there', 'hello', 'I am glad! You are talking to me']

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate chatbot responses
def response(user_response):
    robo_response = ''
    temp_tokens = sentence_tokens + [user_response]
    
    vectorizer = TfidfVectorizer(tokenizer=lem_normalize, stop_words='english')
    tfidf = vectorizer.fit_transform(temp_tokens)

    values = cosine_similarity(tfidf[-1], tfidf[:-1])
    idx = values.argsort()[0][-1]
    flat = values.flatten()
    flat.sort()
    req_tfidf = flat[-1]

    if req_tfidf == 0:
        robo_response = '{} Sorry, I don\'t understand you'.format(robo_response)
    else:
        robo_response = robo_response + sentence_tokens[idx]
    return robo_response

@app.route('/')
def index():
    return render_template('index.html')  # Render the chat interface

@app.route('/chat', methods=['POST'])
def chat():
    user_response = request.json.get('message', '').lower()
    if user_response == 'bye':
        return jsonify(response='BOT: Bye!')
    elif greeting(user_response):
        return jsonify(response=greeting(user_response))
    else:
        return jsonify(response=response(user_response))

if __name__ == "__main__":
#    app.run(debug=True)
     app.run(debug=True, host='0.0.0.0', port=5000)
