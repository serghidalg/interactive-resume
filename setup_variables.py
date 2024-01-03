#!/bin/python
import os
import shutil

# Only variables in this variable will be saved!
variables = {}
def variables_ollama():
    variables['url'] = input('Enter your main Ollama URL: ')
    setup_url2 = input('Do you want to set up a secondary Ollama instance? (y/n): ')
    if setup_url2 in ('y', 'yes'):
        variables['url2'] = input('Enter your secondary Ollama URL: ')
    else:
        variables['url2'] = variables['url']

def variables_logic():
    variables['instructions'] = input('What instructions do you want your assistant to follow: \n')
    variables['first_prompt'] = input('What should be the first prompt from the assistant?: \n')
    variables['sleep_timer'] = 0.0005

def variables_personal():
    variables['name'] = input('Enter your full name: ')
    variables['url_linkedin'] = input('Enter the link to your Linkedin profile: ')
    variables['url_github'] = input('Enter the link to your GitHub profile: ')
    variables['url_cv'] = input('Enter the link to your static CV: ')


def file_save_variables():
    if 'variables.py' in os.listdir():
        print('An old copy of variabels.py was moved to .variables.py.backup')
        shutil.copy('variables.py', '.variables.py.backup')
    with open('variables.py', 'w') as file:
        for variable, value in variables.items():
            if type(value) == str:
                file.write(f"{variable} = '{value}'\n")
            else:
                file.write(f"{variable} = {value}\n")

print('#################################################################')
print('You are starting the setup of your variables.py configuration :D')
print('#################################################################')
print('\n## Configuring your personal information ##')
variables_personal()
print('\n## Configuring your Ollama server information ##')
variables_ollama()
print('\n## Configuring your session logic ##')
variables_logic()
print('\n## Saving to your variables.py file ##')
file_save_variables()
print('################################################################')
print('All done! Thanks for using my tool!!')
print('################################################################')
