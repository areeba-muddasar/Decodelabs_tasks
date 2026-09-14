# ============================================
# PROJECT 1: ADVANCED RULE-BASED AI CHATBOT
# DecodeLabs - Batch 2026
# ============================================

import re
import random
from datetime import datetime

from colors import Colors
from knowledge_base import responses, fallback_responses


# ============================================
# SESSION VARIABLES
# ============================================

conversation_history = []
total_messages = 0
start_time = datetime.now()
user_name = None


# ============================================
# INPUT SANITIZATION
# ============================================

def sanitize_input(text):

    text = text.lower()

    text = " ".join(text.split())

    text = re.sub(
        r"[^a-zA-Z0-9\s?!.,]",
        "",
        text
    )

    return text.strip()


# ============================================
# TIME-BASED GREETING
# ============================================

def get_time_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good morning! ☀️"

    elif hour < 18:
        return "Good afternoon! 😊"

    else:
        return "Good evening! 🌙"


# ============================================
# USER NAME DETECTION
# ============================================

def detect_name(user_input):

    global user_name

    patterns = [
        r"my name is ([a-zA-Z]+)",
        r"i am ([a-zA-Z]+)",
        r"i'm ([a-zA-Z]+)",
        r"call me ([a-zA-Z]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            user_input
        )

        if match:

            user_name = match.group(1).capitalize()

            return (
                f"Nice to meet you, "
                f"{user_name}! 😊"
            )

    return None


# ============================================
# GET BOT RESPONSE
# ============================================

def get_response(user_input):

    global total_messages

    total_messages += 1

    # ========================================
    # EXIT COMMANDS
    # ========================================

    exit_commands = [
        "bye",
        "exit",
        "quit",
        "goodbye",
        "see you"
    ]

    if user_input in exit_commands:
        return None


    # ========================================
    # NAME DETECTION
    # ========================================

    name_response = detect_name(user_input)

    if name_response:
        return name_response


    # ========================================
    # USER NAME QUESTION
    # ========================================

    name_questions = [
        "what is my name",
        "do you know my name",
        "who am i"
    ]

    if user_name:

        for question in name_questions:

            if question in user_input:

                return (
                    f"Your name is "
                    f"{user_name}! 😊"
                )


    # ========================================
    # SPECIAL COMMANDS
    # ========================================

    if user_input == "time":

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        return (
            f"The current time is "
            f"{current_time}."
        )


    if user_input == "date":

        current_date = datetime.now().strftime(
            "%B %d, %Y"
        )

        return (
            f"Today's date is "
            f"{current_date}."
        )


    # ========================================
    # CHECK KNOWLEDGE BASE
    # ========================================

    # Longer phrases are checked first.
    # This prevents "hi" from matching
    # inside "machine learning".

    sorted_keys = sorted(
        responses.keys(),
        key=len,
        reverse=True
    )

    for key in sorted_keys:

        if key in user_input:

            return random.choice(
                responses[key]
            )


    # ========================================
    # FALLBACK
    # ========================================

    return random.choice(
        fallback_responses
    )


# ============================================
# DISPLAY WELCOME MESSAGE
# ============================================

def print_welcome():

    print(
        Colors.HEADER
        + "=" * 65
        + Colors.END
    )

    print(
        Colors.BOLD
        + Colors.BLUE
        + "          🤖 ADVANCED RULE-BASED AI CHATBOT 🤖"
        + Colors.END
    )

    print(
        Colors.HEADER
        + "=" * 65
        + Colors.END
    )

    print(
        Colors.GREEN
        + f"💡 {get_time_greeting()}"
        + Colors.END
    )

    print(
        Colors.GREEN
        + "💡 I'm DecodeBot, your AI assistant."
        + Colors.END
    )

    print(
        Colors.YELLOW
        + "💡 Type 'help' to see available features."
        + Colors.END
    )

    print(
        Colors.RED
        + "💡 Type 'bye' or 'exit' to quit."
        + Colors.END
    )

    print(
        Colors.HEADER
        + "-" * 65
        + Colors.END
    )


# ============================================
# SHOW HISTORY
# ============================================

def show_history():

    if not conversation_history:

        print(
            Colors.YELLOW
            + "No conversation history yet."
            + Colors.END
        )

        return


    print(
        Colors.MAGENTA
        + "\n📜 CONVERSATION HISTORY"
        + Colors.END
    )

    print(
        Colors.HEADER
        + "-" * 65
        + Colors.END
    )

    for index, (user, bot) in enumerate(
        conversation_history,
        start=1
    ):

        print(
            f"{index}. You: {user}"
        )

        print(
            f"   Bot: {bot}"
        )

    print(
        Colors.HEADER
        + "-" * 65
        + Colors.END
    )


# ============================================
# SHOW SESSION STATISTICS
# ============================================

def print_stats():

    duration = datetime.now() - start_time

    unique_inputs = len(
        set(
            message[0]
            for message in conversation_history
        )
    )

    print(
        Colors.HEADER
        + "=" * 65
        + Colors.END
    )

    print(
        Colors.BOLD
        + "📊 SESSION STATISTICS"
        + Colors.END
    )

    print(
        f"   Total Messages     : {total_messages}"
    )

    print(
        f"   Conversation Turns : "
        f"{len(conversation_history)}"
    )

    print(
        f"   Unique Inputs      : "
        f"{unique_inputs}"
    )

    print(
        f"   Session Duration   : "
        f"{duration}"
    )

    if user_name:

        print(
            f"   User Name          : "
            f"{user_name}"
        )

    print(
        Colors.HEADER
        + "=" * 65
        + Colors.END
    )


# ============================================
# MAIN CHATBOT LOOP
# ============================================

def main():

    print_welcome()

    while True:

        try:

            user_input = input(
                Colors.BOLD
                + "\nYou: "
                + Colors.END
            )


            # =================================
            # SANITIZE INPUT
            # =================================

            clean_input = sanitize_input(
                user_input
            )


            # =================================
            # EMPTY INPUT
            # =================================

            if not clean_input:

                print(
                    Colors.YELLOW
                    + "🤖 Bot: Please enter something!"
                    + Colors.END
                )

                continue


            # =================================
            # SPECIAL COMMANDS
            # =================================

            if clean_input == "history":

                show_history()

                continue


            if clean_input == "stats":

                print_stats()

                continue


            if clean_input == "clear":

                conversation_history.clear()

                print(
                    Colors.GREEN
                    + "🧹 Conversation history cleared!"
                    + Colors.END
                )

                continue


            # =================================
            # GET RESPONSE
            # =================================

            response = get_response(
                clean_input
            )


            # =================================
            # SAVE HISTORY
            # =================================

            conversation_history.append(
                (
                    clean_input,
                    response
                )
            )


            # =================================
            # EXIT
            # =================================

            if response is None:

                print(
                    Colors.GREEN
                    + "\n🤖 Bot: Goodbye! "
                    + "Have a great day! 👋"
                    + Colors.END
                )

                print(
                    Colors.YELLOW
                    + "Thanks for chatting with me!"
                    + Colors.END
                )

                print_stats()

                break


            # =================================
            # DISPLAY RESPONSE
            # =================================

            print(
                Colors.CYAN
                + "🤖 Bot: "
                + response
                + Colors.END
            )


        # =====================================
        # KEYBOARD INTERRUPT
        # =====================================

        except KeyboardInterrupt:

            print(
                Colors.RED
                + "\n\n⚠️ Conversation interrupted."
                + Colors.END
            )

            print_stats()

            break


        # =====================================
        # ERROR HANDLING
        # =====================================

        except Exception as error:

            print(
                Colors.RED
                + f"\n⚠️ An error occurred: {error}"
                + Colors.END
            )

            print(
                Colors.YELLOW
                + "Please try again."
                + Colors.END
            )


# ============================================
# RUN APPLICATION
# ============================================

if __name__ == "__main__":
    main()