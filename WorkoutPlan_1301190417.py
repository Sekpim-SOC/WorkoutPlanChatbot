
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
from owlready2 import *
from owlready2.reasoning import sync_reasoner_pellet
import random

# Defined ontology and classes here
onto = get_ontology("C:/Users/widif/Downloads/TA/inikaliyakwkwkw.owl").load()

# Define the rules
with onto:
    # Rule w1: Person memiliki gender "Male", memiliki "Height" dan "Waist", lalu dihitung 76 – 20 x (Height / Waist), maka akan menghasilkan nilai "RFM"nya
    rule1 = Imp()
    rule1.set_as_rule(
        'Person(?p), hasGender(?p, "Male"), hasHeight(?p, ?h), hasWaist(?p, ?w), divide(?divideresult, ?h, ?w), multiply(?multipliedResult, 20, ?divideresult), subtract(?rfm, 64 ,?multipliedResult) -> hasRFM(?p, ?rfm)'
    )

    # Rule 2: Person memiliki gender "Female", memiliki "Height" dan "Waist", lalu dihitung 64 – 20 x (Height / Waist), maka akan menghasilkan nilai "RFM"nya
    rule2 = Imp()
    rule2.set_as_rule(
        'Person(?p), hasGender(?p, "Female"), hasHeight(?p, ?h), hasWaist(?p, ?w), divide(?divideresult, ?h, ?w), multiply(?multipliedResult, 20, ?divideresult), subtract(?rfm, 76 ,?multipliedResult) -> hasRFM(?p, ?rfm)'
    )

    # Rule 3: Jika Person gender "Male" Memiliki nilai "RFM" Lebih dari 24 makan akan diklasifikasikan sebagai "Obese"

    rule3 = Imp()
    rule3.set_as_rule(
        'Person(?p) , hasGender(?p, "Male") , hasRFM(?p, ?rfm) , greaterThan(?rfm, 24) -> Obesity(?p)'
    )

    # Rule 4: Jika Person gender "Female" Memiliki nilai "RFM" Lebih dari 31 makan akan diklasifikasikan sebagai "Obese"
    rule4 = Imp()
    rule4.set_as_rule(
        'Person(?p) , hasGender(?p, "Female") , hasRFM(?p, ?rfm) , greaterThan(?rfm, 31) -> Obesity(?p)'
    )
# UPPERBODY WORKOUTPLAN
    rule5 = Imp()
    rule5.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveBeginnerUpperBodyWorkoutPlan)'
    )
    rule6 = Imp()
    rule6.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveBeginnerUpperBodyWorkoutPlan)'
    )
    rule7 = Imp()
    rule7.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveBeginnerUpperBodyWorkoutPlan)'
    )
    rule8 = Imp()
    rule8.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveIntermediateUpperBodyWorkoutPlan)'
    )
    rule9 = Imp()
    rule9.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveIntermediateUpperBodyWorkoutPlan)'
    )
    rule10 = Imp()
    rule10.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveIntermediateUpperBodyWorkoutPlan)'
    )
    rule11 = Imp()
    rule11.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveAdvancedUpperBodyWorkoutPlan)'
    )
    rule12 = Imp()
    rule12.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveAdvancedUpperBodyWorkoutPlan)'
    )
    rule13 = Imp()
    rule13.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "UpperBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveAdvancedUpperBodyWorkoutPlan)'
    )

# LOWER WORKOUTPLAN
    rule14 = Imp()
    rule14.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveBeginnerLowerBodyWorkoutPlan)'
    )
    rule15 = Imp()
    rule15.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveBeginnerLowerBodyWorkoutPlan)'
    )
    rule16 = Imp()
    rule16.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveBeginnerLowerBodyWorkoutPlan)'
    )
    rule17 = Imp()
    rule17.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveIntermediateLowerBodyWorkoutPlan)'
    )
    rule18 = Imp()
    rule18.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveIntermediateLowerBodyWorkoutPlan)'
    )
    rule19 = Imp()
    rule19.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveIntermediateLowerBodyWorkoutPlan)'
    )
    rule20 = Imp()
    rule20.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveAdvancedLowerBodyWorkoutPlan)'
    )
    rule21 = Imp()
    rule21.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveAdvancedULowerBodyWorkoutPlan)'
    )
    rule22 = Imp()
    rule22.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "LowerBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveAdvancedLowerBodyWorkoutPlan)'
    )

# FULLBODY WORKOUTPLAN
    rule23 = Imp()
    rule23.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveBeginnerFullBodyWorkoutPlan)'
    )
    rule24 = Imp()
    rule24.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveBeginnerFullBodyWorkoutPlan)'
    )
    rule25 = Imp()
    rule25.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "beginner") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveBeginnerFullBodyWorkoutPlan)'
    )
    rule26 = Imp()
    rule26.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveIntermediateFullBodyWorkoutPlan)'
    )
    rule27 = Imp()
    rule27.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveIntermediateFullBodyWorkoutPlan)'
    )
    rule28 = Imp()
    rule28.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "intermediate") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveIntermediateFullBodyWorkoutPlan)'
    )
    rule29 = Imp()
    rule29.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "inactive") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, InactiveAdvancedFullBodyWorkoutPlan)'
    )
    rule30 = Imp()
    rule30.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "active") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, ActiveAdvancedUFullBodyWorkoutPlan)'
    )
    rule31 = Imp()
    rule31.set_as_rule(
        'Person(?p) , hasActivityLevel(?p, "veryActive") , hasDifficultyPreference(?p, "advanced") , hasMuscleGroupPreference(?p, "FullBody") , WorkoutPlan(?wp) ->  hasWorkoutPlan(?p, ?wp) , hasWorkoutPlan(?wp, veryActiveAdvancedFullBodyWorkoutPlan)'
    )

# Now you can save the ontology with the added rules
onto.save("modified_ontology.owl")

# Define the command handlers for the Telegram bot
# Create an instance of the Person class
p1 = None

# Define the states for the conversation handler
WELCOME, PERSON_NAME, HAS_GENDER, HAS_HEIGHT, HAS_WAIST, HAS_ACTIVITY_LEVEL, HAS_DIFFICULTY_PREFERENCE, HAS_MUSCLE_GROUP_PREFERENCE, PERSON_DATA_RETRIEVE = range(
    9)

# Define the command handlers for the Telegram bot


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello! Welcome to Let's Get Fit WorkoutPlan Chatbot")
    return person_name(update, context)


def person_name(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Please enter your name:")
    return PERSON_NAME


def get_person_name(update, context):
    name = update.message.text
    context.user_data['name'] = name
    return has_gender(update, context)


def has_gender(update, context):
    keyboard = [
        [InlineKeyboardButton("Male", callback_data='Male'), InlineKeyboardButton(
            "Female", callback_data='Female')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please select your gender:", reply_markup=reply_markup)
    return HAS_GENDER


def get_has_gender(update, context):
    query = update.callback_query
    context.user_data['gender'] = query.data
    query.answer()
    return has_height(update, context)


def has_height(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Please enter your height (in cm):")
    return HAS_HEIGHT


def get_has_height(update, context):
    height = update.message.text
    context.user_data['height'] = int(height)
    return has_waist(update, context)


def has_waist(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please enter your waist circumference (in cm):")
    return HAS_WAIST


def get_has_waist(update, context):
    waist = update.message.text
    context.user_data['waist'] = int(waist)
    return has_activity_level(update, context)


def has_activity_level(update, context):
    keyboard = [
        [InlineKeyboardButton("Inactive", callback_data='inactive'), InlineKeyboardButton(
            "Active", callback_data='active')],
        [InlineKeyboardButton("Very Active", callback_data='veryActive')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please select your activity level:", reply_markup=reply_markup)
    return HAS_ACTIVITY_LEVEL


def get_has_activity_level(update, context):
    query = update.callback_query
    context.user_data['activity_level'] = query.data
    query.answer()
    return has_difficulty_preference(update, context)


def has_difficulty_preference(update, context):
    keyboard = [
        [InlineKeyboardButton("Beginner", callback_data='beginner'), InlineKeyboardButton(
            "Intermediate", callback_data='intermediate')],
        [InlineKeyboardButton("Advanced", callback_data='advanced')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please select your difficulty preference:", reply_markup=reply_markup)
    return HAS_DIFFICULTY_PREFERENCE


def get_has_difficulty_preference(update, context):
    query = update.callback_query
    context.user_data['difficulty_preference'] = query.data
    query.answer()
    return has_muscle_group_preference(update, context)


def has_muscle_group_preference(update, context):
    keyboard = [
        [InlineKeyboardButton("UpperBody", callback_data='UpperBody'), InlineKeyboardButton(
            "LowerBody", callback_data='LowerBody')],
        [InlineKeyboardButton("FullBody", callback_data='FullBody')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Please select your muscle group preference:", reply_markup=reply_markup)
    return HAS_MUSCLE_GROUP_PREFERENCE


def get_has_muscle_group_preference(update, context):
    query = update.callback_query
    context.user_data['muscle_group_preference'] = query.data
    query.answer()
    return person_data_retrieve(update, context)


def person_data_retrieve(update, context):
    name = context.user_data['name']
    gender = context.user_data['gender']
    height = context.user_data['height']
    waist = context.user_data['waist']
    activity_level = context.user_data['activity_level']
    difficulty_preference = context.user_data['difficulty_preference']
    muscle_group_preference = context.user_data['muscle_group_preference']

    global p1
    p1 = onto.Person(hasName=name, hasGender=gender, hasHeight=height, hasWaist=waist,
                     hasActivityLevel=activity_level, hasDifficultyPreference=difficulty_preference,
                     hasMuscleGroupPreference=muscle_group_preference)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Information received. Reasoning will now be performed.")
    run_reasoner(update, context)


def run_reasoner(update, context):
    name = context.user_data['name']
    # Run the reasoner
    sync_reasoner_pellet(infer_property_values=True,
                         infer_data_property_values=True)

    # Retrieve and send the inferred property values
    check_individual_exercises("WarmUpSession", update, context)
    check_individual_exercises("CoreSession", update, context)

    if p1.hasMuscleGroupPreference == "LowerBody":
        check_individual_exercises("LowerBodySession", update, context)
    elif p1.hasMuscleGroupPreference == "UpperBody":
        check_individual_exercises("UpperBodySession", update, context)
    elif p1.hasMuscleGroupPreference == "FullBody":
        check_individual_exercises("FullBodySession", update, context)

    check_individual_exercises("CoolingDownSession", update, context)

    # Print the property values of p1
    response = f"Name: {name}\n"
    response += f"Gender: {p1.hasGender}\n"
    response += f"Relative Fat Mass (RFM): {p1.hasRFM}\n"
    response += f"Activity Level: {p1.hasActivityLevel}\n"
    response += f"Difficulty Preference: {p1.hasDifficultyPreference}\n"
    response += f"Muscle Group Preference: {p1.hasMuscleGroupPreference}\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def check_individual_exercises(individual_name, update, context):
    exercises_list = p1.hasWorkoutPlan

    # Retrieve the individual
    individual = onto.search_one(iri="*{}*".format(individual_name))

    if individual:
        expected_exercises = individual.hasExercise
        matching_exercises = [str(exercise).split(
            '.')[-1] for exercise in exercises_list if exercise in expected_exercises]

        if matching_exercises:
            response = f"{individual_name}:\n\n"
            if individual_name == "WarmUpSession":
                for exercise in matching_exercises:
                    response += exercise + f" 10 Reps\n"
                response += "\n"
            elif individual_name == "CoolingDownSession":
                for exercise in matching_exercises:
                    response += exercise + f" 5 Minutes\n"
                response += "\n"
            else:
                random.shuffle(matching_exercises)
                # Select three random exercises
                selected_exercises = matching_exercises[:3]

                for exercise in selected_exercises:
                    response += exercise + f" 4 - 5 Sets 8-12 Reps\n"
                response += "\n"
        else:
            response = f"No matching exercises found in {individual_name}."
    else:
        response = f"Individual {individual_name} not found in the ontology."

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def error(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="An error occurred.")


def main():
    # Set up the Telegram bot
    TOKEN = "6499997602:AAGoWGWR62604P0h-ILN5H6-G2VCqIyo40I"
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the command and message handlers
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PERSON_NAME: [MessageHandler(Filters.text, get_person_name)],
            HAS_GENDER: [CallbackQueryHandler(get_has_gender)],
            HAS_HEIGHT: [MessageHandler(Filters.text, get_has_height)],
            HAS_WAIST: [MessageHandler(Filters.text, get_has_waist)],
            HAS_ACTIVITY_LEVEL: [CallbackQueryHandler(get_has_activity_level)],
            HAS_DIFFICULTY_PREFERENCE: [CallbackQueryHandler(get_has_difficulty_preference)],
            HAS_MUSCLE_GROUP_PREFERENCE: [CallbackQueryHandler(get_has_muscle_group_preference)],
            PERSON_DATA_RETRIEVE: [MessageHandler(
                Filters.text, person_data_retrieve)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
