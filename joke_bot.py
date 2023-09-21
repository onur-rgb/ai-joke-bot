from utils import (
    get_model_and_tokenizer,
    get_pipeline_for_langchain,
    format_message,
    StopOnTokens,
)
import numpy as np
import gradio as gr
from transformers import TextIteratorStreamer, StoppingCriteriaList
from threading import Thread


class Bot:
    name = 'Llamastar'

    def __init__(self):
        # Specify the model name or path
        self.model_name_or_path = "TheBloke/Llama-2-7B-chat-GPTQ"

        # Initialize the language model and tokenizer
        self.model, self.tokenizer = get_model_and_tokenizer(self.model_name_or_path)

        # Create a langchain pipeline
        self.langchain_pipeline = get_pipeline_for_langchain(self.model, self.tokenizer)

        # Define different categories of joke prefixes
        self.joke_prefixes = ["outer space joke", "holiday joke", "computer joke", "animal joke", "business joke", "sports joke"]

    # Define a Gradio chat interface for the chatbot
    def gradio_chat(self):

        # Define a function for generating responses
        def predict(message, history):
            stop = StopOnTokens()
            messages = format_message(message, history)
            model_inputs = self.tokenizer([messages], return_tensors="pt").to("cuda")
            streamer = TextIteratorStreamer(self.tokenizer, skip_prompt=True, skip_special_tokens=True)
            generate_kwargs = dict(
                model_inputs,
                streamer=streamer,
                max_new_tokens=256,
                do_sample=True,
                top_p=0.95,
                top_k=1000,
                temperature=0.8,
                num_beams=1,
                stopping_criteria=StoppingCriteriaList([stop])
            )
            t = Thread(target=self.model.generate, kwargs=generate_kwargs)
            t.start()

            partial_message = ""
            for new_token in streamer:
                if new_token != '<':
                    partial_message += new_token
                    yield partial_message

        description = """<h1><center>AI Comedy Club</center></h1>"""
        chatbot = gr.Chatbot(label='Llamastar')
        textbox = gr.Textbox(placeholder='You can insert your prompt here.', show_label=False)
        examples = ["Hello", "You are so funny make another joke.", "Give me some sports joke."]
        gr.ChatInterface(fn=predict, chatbot=chatbot, textbox=textbox, examples=examples, description=description).queue().launch(share=True)


if __name__ == "__main__":
    bot = Bot()

    # Chatbot
    bot.gradio_chat()
