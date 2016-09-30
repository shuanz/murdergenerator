from flask import Flask
from flask import render_template
import random
import json
from generateAddress import GenerateAddres
from charGenerator import CharGenerator
#from flask_googlemaps import GoogleMaps

app = Flask(__name__)
#GoogleMaps(app)

@app.route('/')
def murdergen(name=None):

    with open('murderList.json') as mlists:
        murder_list = json.load(mlists)

    character_generator = CharGenerator()
    victim = character_generator.generator()
    guilty = character_generator.generator()
    suspecta = character_generator.generator()
    suspectb = character_generator.generator()
    how = random.choice(murder_list["how"])
    why = random.choice(murder_list["why"])
    where = random.choice(murder_list["where"])
    address, lat, lon = GenerateAddres().generator()
    when = random.choice(murder_list["when"])
    who_relation = random.choice(murder_list["who"])
    suspect_name_list = []
    suspect_relation_list = []
    suspect_job_list = []
    list_size = random.randint(1,4)

    for i in victim:
        victim_name = victim[0]
        victim_job = victim[1]
        victim_height = victim[2]
        victim_weight = victim[3]
        victim_tone = victim[4]
        victim_eyecolors = victim[5]
        victim_hairlengths = victim[6]
        victim_haircolors = victim[7]
        victim_hairtypes = victim[8]
        victim_facehairs = victim[9]
        victim_clothings = victim[10]

    for i in guilty:
        guilty_name = guilty[0]
        guilty_job = guilty[1]
        guilty_height = guilty[2]
        guilty_weight = guilty[3]
        guilty_tone = guilty[4]
        guilty_eyecolors = guilty[5]
        guilty_hairlengths = guilty[6]
        guilty_haircolors = guilty[7]
        guilty_hairtypes = guilty[8]
        guilty_facehairs = guilty[9]
        guilty_clothings = guilty[10]
        guilty_victim_relationship = guilty[11]

    for i in suspecta:
        suspecta_name = suspecta[0]
        suspecta_job = suspecta[1]
        suspecta_victim_relationship = suspecta[11]

    for i in suspecta:
        suspectb_name = suspectb[0]
        suspectb_job = suspectb[1]
        suspectb_victim_relationship = suspectb[11]

    for i in range (0, list_size):
        suspectx = character_generator.generator()
        suspect_name_list.append(suspectx[0:])
        suspect_relation_list.append(suspectx[11])
        suspect_job_list.append(suspectx[1])
    if i < 4:
        for c in range (i, 4):
            suspect_name_list.append(["",""])
            suspect_relation_list.append("")
            suspect_job_list.append("")

    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run()
