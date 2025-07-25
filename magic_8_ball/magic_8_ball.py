"""
Simple Magic 8 Ball Chatbot

A Magic 8 Ball that judges you.
Remember to ask nicely!


Adda Weathers
May 31, 2025
"""

import gradio as gr
import random
import string

# Magic 8 Ball Responses
# Categorized based on yes, neutral, and no

positive_responses = ["It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes – definitely.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes."]

neutral_responses =  ["Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again."]

negative_responses =  ["Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

# Determine if user enters profanity
# Non-exhaustive list, just for illustrative purposes
profanity = ["shit", "fuck", "fucking", "asshole", "damn", "hell", "bitch", "slut", "skank", "crap", "ass", "bastard", "cunt", "dumbass"]

def has_profanity(text):
    # Finds the bad words and handles punctuation 
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    # Will return True if the user sends a message containing profanity
    return any(word in profanity for word in words)

# Determine if the user is asking nicely
# Again, non-exhaustive 
kind_words = ["please", "thanks", "thank you", "grateful", "kind", "kindly"]

def has_kind_words(text):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    # Will return True if the user sends a message containing nice words
    return any(word in kind_words for word in words)

# The Magic 8 Ball
def magic_8_ball(question):
    # Can't use an empty string
    if not question.strip():
        return "I cannot answer that. You can try again."

    # If user is both using profanity and a kind word
    if has_profanity(question) and has_kind_words(question):
        return "I think you already decided for yourself."

    # If user is being nice
    if has_kind_words(question):
        return random.choice(positive_responses)

    # The user is going to get a negative response if they use profanity.
    if has_profanity(question):
        return random.choice(negative_responses)

    # The Magic 8 Ball will provide a positive or neutral response as long as user is not extreme
    if not has_kind_words(question) and not has_profanity(question):
        most_responses = positive_responses + neutral_responses
        return random.choice(most_responses)

# Gradio for UI
demo = gr.Interface(
    fn = magic_8_ball,
    inputs=gr.Textbox(lines=2, placeholder="Ask the Magic 8-Ball a question..."),
    outputs="text",
    title="🎱 Magic 8-Ball Chatbot",
    description="Ask a question. Fate will decide if your attitude doesn't first."
)

demo.launch()




