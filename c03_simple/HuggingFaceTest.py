# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.6
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + id="mwXUcr7wBZbj"
# !pip install huggingface_hub transformers[agents]

# + id="z48Rgtz6IcAF"
from huggingface_hub import login

login("<INSERT_TOKEN_HERE>")

# + id="VMppsQluJG7b"
from transformers import HfAgent

agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoderbase")

# + id="4BuzW4cHORYR"
agent.run("Draw me a picture of `prompt`", prompt="rainbow butterflies")
