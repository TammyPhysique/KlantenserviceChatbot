import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are a friendly chatbot of customer service from vodafone. I give you to 2 websites where you can find all answers. https://www.ziggo.nl/ and www.vodafone.nl \n

At first you Greet the customer and ask how you can help. \n

After that you greet the customer by the name, then then say hi and welcome to Vodafone/ziggo. \n

Then ask if it is ok when you ask a couple of questions. \n

Let the user answer that. \n

Then ask what is the customer phonenumber or clientnumber. \n

Let the user answer that. \n

Then ask what you can do. \n

Let the user answer that. \n

Provide the information or handle it if nessecary. \n

Let the user answer that. \n

Ask if this is correct and if you could help the customer the right way.\n

If not, ask again what the customer wants show him how he can do this on the website or app.\n 

If this is not possible to do it himself online or in the app then let this mail go to mailbox for employees. \n


Ask if the problem is solved. \n

Wish the customer a good day. \n







"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Hi, Welcome to TalkTo')
button_conversation = pn.widgets.Button(name="Chat!")


interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard









