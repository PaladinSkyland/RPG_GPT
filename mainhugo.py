from OpenAI import OpenAIclass
import json

OpenAI = OpenAIclass()

# Read the JSON file
with open('prompt.json') as file:
    data = json.load(file)

# Extract the object prompts
prompts = data['prompts']
# Find the prompt with name 'IntroductionRPG'
for prompt in prompts:
    if prompt['name'] == 'IntroductionRPG':
        IntroductionRPG = prompt
    if prompt['name'] == 'Who are you?':
        whoareu = prompt

# Use the selected prompt
system_message2 = OpenAI.user_message(IntroductionRPG['prompt'])
system_message1 = OpenAI.system_message(whoareu['prompt'])
messages = [system_message1, system_message2]
print(OpenAI.return_completion(messages))
