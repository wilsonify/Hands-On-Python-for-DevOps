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

# + id="9BkhUmnRYibB"
user_data = {
    'username': 'user_with_emoji😊',
}

# + id="AMRL8K_efh9e"


# + id="s3gt6mYMY61W"
import json

with open('sample.json', 'w', encoding='utf-8') as file:
        json.dump(user_data, file, ensure_ascii=False, indent=2)
