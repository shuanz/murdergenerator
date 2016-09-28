from flask import Flask
from flask import render_template
import random
import json
from generateAddress import GenerateAddres
from jobs import GenerateJobs
from nameGen import NameGen
from charGenerator import CharGenerator
from flask_googlemaps import GoogleMaps

app = Flask(__name__)
GoogleMaps(app)

@app.route('/')
def murdergen(name=None):

    with open('murderList.json') as mlists:
        murder_list = json.load(mlists)

    name_gen = NameGen()
    character_generator = CharGenerator()

    victim = character_generator.generator()
    guilty = character_generator.generator()

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

    how = random.choice(murder_list["how"])
    why = random.choice(murder_list["why"])
    where = random.choice(murder_list["where"])
    address, lat, lon = GenerateAddres().generator()
    when = random.choice(murder_list["when"])

    who_relation = random.choice(murder_list["who"])

    suspecta_name = name_gen.generator()
    suspecta_relation = random.choice(murder_list["who"])
    suspecta_job = GenerateJobs().generator()
    suspectb_name = name_gen.generator()
    suspectb_relation = random.choice(murder_list["who"])
    suspectb_job = GenerateJobs().generator()
    suspect_name_list = []
    suspect_relation_list = []
    suspect_job_list = []
    list_size = random.randint(1,4)

    for i in range (0, list_size):
        suspect_name_list.append(name_gen.generator())
        suspect_relation_list.append(random.choice(murder_list["who"]))
        suspect_job_list.append(GenerateJobs().generator())
    if i < 4:
        for c in range (i, 4):
            suspect_name_list.append(["",""])
            suspect_relation_list.append("")
            suspect_job_list.append("")
    return render_template('index.html',
    victim_name=victim_name,
    victim_job=victim_job,
    victim_height = victim_height,
    victim_weight=victim_weight,
    victim_tone=victim_tone,
    victim_eyecolors=victim_eyecolors,
    victim_hairlengths=victim_hairlengths,
    victim_haircolors=victim_haircolors,
    victim_hairtypes=victim_hairtypes,
    victim_facehairs=victim_facehairs,
    victim_clothings=victim_clothings,
    how=how,
    why=why,
    where=where,
    address=address,
    lat=lat,
    lon=lon,
    when=when,
    who_relation=who_relation,
    guilty_name = guilty_name,
    guilty_job = guilty_job,
    guilty_victim_relationship=guilty_victim_relationship,
    guilty_height = guilty_height,
    guilty_weight = guilty_weight,
    guilty_tone = guilty_tone,
    guilty_eyecolors = guilty_eyecolors,
    guilty_hairlengths = guilty_hairlengths,
    guilty_haircolors = guilty_haircolors,
    guilty_hairtypes = guilty_hairtypes,
    guilty_facehairs = guilty_facehairs,
    guilty_clothings = guilty_clothings,
    suspecta_name=suspecta_name[0],
    suspecta_relation=suspecta_relation,
    suspecta_job=suspecta_job,
    suspectb_name=suspectb_name[0],
    suspectb_relation=suspectb_relation,
    suspectb_job=suspectb_job,
    suspectc_name=suspect_name_list[0][0],
    suspectc_relation=suspect_relation_list[0],
    suspectc_job=suspect_job_list[0],
    suspectd_name=suspect_name_list[1][0],
    suspectd_relation=suspect_relation_list[1],
    suspectd_job=suspect_job_list[1],
    suspecte_name=suspect_name_list[2][0],
    suspecte_relation=suspect_relation_list[2],
    suspecte_job=suspect_job_list[2],
    suspectf_name=suspect_name_list[3][0],
    suspectf_relation=suspect_relation_list[3],
    suspectf_job=suspect_job_list[3],
    suspectg_name=suspect_name_list[4][0],
    suspectg_relation=suspect_relation_list[4],
    suspectg_job=suspect_job_list[4]
    )

if __name__ == "__main__":
    app.run()
