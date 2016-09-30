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

    victim = character_generator.generate()
    guilty = character_generator.generate()
    suspecta = character_generator.generate()
    suspectb = character_generator.generate()
    suspectc = character_generator.generate()
    suspectd = character_generator.generate()
    suspecte = character_generator.generate()
    suspectf = character_generator.generate()
    suspectg = character_generator.generate()
    case = case_generator.generate()

    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run()
