# pip install happytransformer

from happytransformer import HappyTextToText as HappyTTT
from happytransformer import TextToTextSettings

def Grammar_Fixer(Text):
    Grammar = HappyTTT("T5","prithivida/grammar_error_correcter_v1")
    config = TextToTextSettings(do_sample=True, top_k=10, max_length=100)
    corrected = Grammar.generate_text(Text, args=config)
    print("Corrected Text:", corrected.text)

Text = "They have went home tomorrow"

Grammar_Fixer(Text)
