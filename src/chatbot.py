
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Bot instantiation

preprocessors=['chatterbot.preprocessors.clean_whitespace',
		'chatterbot.preprocessors.unescape_html',
		'chatterbot.preprocessors.convert_to_ascii']

chatbot = ChatBot(name='Sleeplika',
		preprocessors=preprocessors,
		logic_adapters=[
			{
				'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            			'input_text': 'What is your name?',
            			'output_text': 'My name is Sleeplika.'
			},
			{
				'import_path': 'chatterbot.logic.MathematicalEvaluation'
			},
			{
				'import_path': 'chatterbot.logic.BestMatch',
				'statement_comparison_function': 'chatterbot.comparisons.jaccard_similarity',
				'response_selection_method': 'chatterbot.response_selection.get_most_frequent_response',
				# 'default_response': 'Sorry, could you rephrase? I did not understand you.'
			},
			{
				'import_path': 'chatterbot.logic.TimeLogicAdapter',
				'positive': ['What time is it?',
						'What day of the week is today?',
						'What is the date?',
						'What year am I in?']
			}
		]
	)

trainer = ListTrainer(chatbot=chatbot)

trainer.train([
    'Hi, can I help you?',
    'Sure, I\'d like to book an appointment with the therapist.',
    'Your therapy appointment has been booked.'
])

trainer = ChatterBotCorpusTrainer(chatbot=chatbot)
trainer.train('chatterbot.corpus.english')

# Get a response to the input text 'I would like to book a flight.'
statements = ['I want to book a therapy appointment.',
		'What is your name?',
		'What time is it?',
		'What is 9 + 10?',
		'What is the meaning of Life, the Universe, and Everything?',
		'Read a bedtime story from Reddit.',
		'Play sleeping music.',
		'What new movie should I go watch in theaters?']

for statement in statements:
	print(statement)
	response = chatbot.get_response(statement=statement)
	print(f'- {response}')
