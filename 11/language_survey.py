
from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_servey = AnonymousSurvey(question)

my_servey.show_question()
print("Enter 'q' at any times to exit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_servey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_servey.show_results()