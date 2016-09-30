from flask import Flask
from flask import render_template
import random
import json
from addressGenerator import AddressGenerator
from charGenerator import CharGenerator
from caseGenerator import CaseGenerator
#from flask_googlemaps import GoogleMaps

app = Flask(__name__)
#GoogleMaps(app)

@app.route('/')
def murdergen(name=None):

    with open('murderList.json') as mlists:
        murder_list = json.load(mlists)

    character_generator = CharGenerator()
    case_generator = CaseGenerator()

    victim = character_generator.generator()
    guilty = character_generator.generator()
    suspecta = character_generator.generator()
    suspectb = character_generator.generator()
    suspectc = character_generator.generator()
    suspectd = character_generator.generator()
    suspecte = character_generator.generator()
    suspectf = character_generator.generator()
    suspectg = character_generator.generator()
    case = case_generator.generator()

    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run()
