import os
import textwrap
import pprint
import google.generativeai as GenerativeAI
from IPython.display import Markdown

# Configure Google Generative AI
GOOGLE_API_KEY = "YOUR_API_KEY_HERE.."
GenerativeAI.configure(api_key=GOOGLE_API_KEY)

# List available models
for model in GenerativeAI.list_models():
    pprint.pprint(model)

# Choose a specific model
chosen_model = "gemini-pro"  # Change this to the model you want to use

# Initialize the selected model
model = GenerativeAI.GenerativeModel(model_name=chosen_model)

def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

# Generate content using the selected model
response = model.generate_content(
    "Write a code for different image processing techniques in Python programming language, I would be running the code in Google colab",
    stream=True
)

response.resolve()

# Convert response to markdown
to_markdown(response.text)

