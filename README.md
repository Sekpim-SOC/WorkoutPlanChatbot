# Let's Get Fit WorkoutPlan Chatbot
This repository contains a Telegram chatbot that helps users create personalized workout plans based on their gender, height, waist circumference, activity level, difficulty preference, and muscle group preference. The chatbot uses OWL (Web Ontology Language) to model and reason about user data, allowing it to provide tailored workout recommendations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the telegram bot and owlready2.

```bash
pip install python-telegram-bot==13.13
```
```bash
pip install owlready2
```

## How to start the chatbot

1. Change the directory of the .owl file with your own
2. Create a telegram chatbot with BotFather
3. use TOKEN from BotFather to the code
4. Run the .py file

## Instruction
1. Start the bot by invoking the /start command on Telegram.
2. Provide your name, gender, height, waist circumference, activity level, difficulty preference, and muscle group preference as prompted.
3. The chatbot will perform reasoning using OWL and present a personalized workout plan based on your inputs.
4. The workout plan will include exercises for Warm-up, Core, Upper Body/Lower Body/Full Body, and Cool-down sessions.

## Note
The ontology "inikaliyakwkwkw.owl" contains the underlying rules and data definitions for the chatbot's reasoning. The code loads the ontology, applies reasoning rules, and generates tailored workout plans for users based on the information provided.

## Paper

[SINKRON](https://jurnal.polgan.ac.id/index.php/sinkron/article/view/12689)
