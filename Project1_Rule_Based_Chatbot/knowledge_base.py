# ============================================
# KNOWLEDGE BASE
# Advanced Rule-Based AI Chatbot
# ============================================


# ============================================
# RESPONSES
# ============================================

responses = {

    # ========================================
    # GREETINGS
    # ========================================

    "hello": [
        "Hello! How can I help you today? 😊",
        "Hi there! Great to see you!",
        "Hey! What can I help you with?"
    ],

    "hi": [
        "Hi! Nice to meet you! 👋",
        "Hello! How's your day going?",
        "Hey there! Ready to chat?"
    ],

    "hey": [
        "Hey! How are you doing?",
        "Hello! What would you like to know?",
        "Hi! What's up?"
    ],

    "good morning": [
        "Good morning! ☀️ Hope you have a productive day!",
        "Good morning! Ready to learn something new?"
    ],

    "good afternoon": [
        "Good afternoon! 😊 How can I assist you?"
    ],

    "good evening": [
        "Good evening! 🌅 What can I help you with?"
    ],


    # ========================================
    # GENERAL CONVERSATION
    # ========================================

    "how are you": [
        "I'm doing great! Thanks for asking! 😊",
        "I'm functioning perfectly and ready to help!",
        "I'm just a chatbot, but I'm doing fantastic!"
    ],

    "what is your name": [
        "I'm DecodeBot, your Rule-Based AI Assistant. 🤖",
        "My name is DecodeBot!",
        "You can call me DecodeBot."
    ],

    "who made you": [
        "I was created as a Rule-Based AI Chatbot project.",
        "I'm a Python-based chatbot developed as part of a DecodeLabs project.",
        "I was designed to demonstrate rule-based AI and conversational logic."
    ],

    "what can you do": [
        "I can answer questions about AI, Machine Learning, Deep Learning, Python, and Data Science.",
        "I can handle greetings, technical questions, jokes, facts, Python examples, conversation history, and session statistics.",
        "I'm a rule-based chatbot designed to provide predefined responses based on user input."
    ],


    # ========================================
    # ARTIFICIAL INTELLIGENCE
    # ========================================

    "what is artificial intelligence": [
        "Artificial Intelligence, or AI, is the field of creating machines that can perform tasks that normally require human intelligence."
    ],

    "what is ai": [
        "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence, such as learning, reasoning, and decision-making."
    ],

    "why is ai important": [
        "AI is important because it can automate tasks, analyze large amounts of data, support decision-making, and solve complex problems."
    ],

    "examples of ai": [
        "Examples of AI include virtual assistants, recommendation systems, facial recognition, autonomous vehicles, and AI-powered chatbots."
    ],


    # ========================================
    # MACHINE LEARNING
    # ========================================

    "what is machine learning": [
        "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.",
        "Machine Learning enables computers to learn from data and improve their performance through experience."
    ],

    "what is ml": [
        "ML stands for Machine Learning. It allows computers to learn patterns from data and make predictions."
    ],

    "types of machine learning": [
        "The three main types of Machine Learning are supervised learning, unsupervised learning, and reinforcement learning."
    ],

    "what is supervised learning": [
        "Supervised Learning trains a model using labeled data, where the correct answers are already known."
    ],

    "what is unsupervised learning": [
        "Unsupervised Learning finds hidden patterns or structures in data without using labeled answers."
    ],

    "what is reinforcement learning": [
        "Reinforcement Learning allows an agent to learn by interacting with an environment and receiving rewards or penalties."
    ],


    # ========================================
    # DEEP LEARNING
    # ========================================

    "what is deep learning": [
        "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns."
    ],

    "what is neural network": [
        "A neural network is a machine learning model inspired by the human brain. It consists of interconnected nodes organized into layers."
    ],


    # ========================================
    # PYTHON
    # ========================================

    "what is python": [
        "Python is a popular, high-level programming language widely used in AI, Machine Learning, Data Science, automation, and web development. 🐍"
    ],

    "give me a small python code": [
        "Here's a simple Python program:\n\n"
        "name = input('Enter your name: ')\n"
        "print('Hello', name)"
    ],

    "give me python code": [
        "Here's a simple Python example:\n\n"
        "number = 10\n"
        "print('Square:', number * number)"
    ],

    "write a small python code": [
        "Here's a simple Python program:\n\n"
        "number = int(input('Enter a number: '))\n"
        "print('Square:', number ** 2)"
    ],

    "python example": [
        "Here's a simple Python example:\n\n"
        "for i in range(1, 6):\n"
        "    print(i)"
    ],

    "python list": [
        "A Python list stores multiple values in a single variable.\n\n"
        "Example:\n"
        "numbers = [1, 2, 3, 4, 5]"
    ],


    # ========================================
    # DATA SCIENCE
    # ========================================

    "what is data science": [
        "Data Science combines programming, statistics, mathematics, and domain knowledge to extract useful insights from data."
    ],

    "what is data analysis": [
        "Data Analysis is the process of inspecting, cleaning, transforming, and interpreting data to discover useful information."
    ],

    "what is pandas": [
        "Pandas is a Python library commonly used for data manipulation, analysis, and working with structured datasets."
    ],

    "what is numpy": [
        "NumPy is a Python library used for numerical computing and working efficiently with arrays and mathematical operations."
    ],


    # ========================================
    # FUN
    # ========================================

    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
        "Why don't scientists trust atoms? Because they make up everything! 😂",
        "What do you call a bear with no teeth? A gummy bear! 🐻"
    ],

    "tell me a fact": [
        "The first chatbot, ELIZA, was created in the 1960s.",
        "Python was named after Monty Python, not the snake. 🐍",
        "The term Artificial Intelligence was introduced in the 1950s."
    ],


    # ========================================
    # PERSONAL / CONVERSATION
    # ========================================

    "thank you": [
        "You're very welcome! 😊",
        "Glad I could help!",
        "Anytime! That's what I'm here for!"
    ],

    "thanks": [
        "You're welcome! 😊",
        "My pleasure!",
        "Happy to help!"
    ],

    "good": [
        "That's great to hear! 😊",
        "Awesome! Keep it up!",
        "Wonderful!"
    ],

    "bad": [
        "Oh no! I hope things get better! 🤗",
        "Sorry to hear that. Stay positive!"
    ],


    # ========================================
    # HELP
    # ========================================

    "help": [
        "🤖 Available Features:\n"
        "  • Greetings\n"
        "  • AI questions\n"
        "  • Machine Learning\n"
        "  • Deep Learning\n"
        "  • Python\n"
        "  • Data Science\n"
        "  • Python code examples\n"
        "  • Jokes and facts\n"
        "  • Conversation history\n"
        "  • Session statistics\n"
        "  • User name memory\n"
        "  • Type 'bye' or 'exit' to quit"
    ]
}


# ============================================
# FALLBACK RESPONSES
# ============================================

fallback_responses = [
    "Sorry, I don't understand that. 🤔",
    "Hmm, I didn't get that. Can you rephrase?",
    "I'm not sure about that. Try asking something else!",
    "I don't have a rule for that yet. Type 'help' to see what I can do.",
    "Sorry! That question is outside my current knowledge base."
]