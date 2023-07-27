# pip install happytransformer

from happytransformer import HappyTextToText as HappyTTT
from happytransformer import TextToTextSettings

def Grammar_Fixer(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    grammar = HappyTTT("T5", "prithivida/grammar_error_correcter_v1")
    config = TextToTextSettings(do_sample=True, top_k=10, max_length=100)
    corrected = grammar.generate_text(text, args=config)

    with open(file_path, 'w') as file:
        file.write(corrected.text)

    print("Grammar fixed and saved to the file:", file_path)

# Replace 'input.txt' with the path to your input text file

file_path = 'input.txt'

Grammar_Fixer(file_path) # call the main function to start the program
