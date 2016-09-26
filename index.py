from flask import Flask
from flask import render_template
import random
import json
from generateAddress import GenerateAddres
from jobs import GenerateJobs
from nameGen import NameGen
from victimGenerator import VictimGenerator

app = Flask(__name__)

@app.route('/')
def murdergen(name=None):
<<<<<<< HEAD

    with open('murderList.json') as mlists:
        murder_list = json.load(mlists)

    name_gen = NameGen()
    victim_generator = VictimGenerator()

    victim = victim_generator.generator()

    for i in victim:
        victim_name = victim[0]
        victimjob = victim[1]
        victim_height = victim[2]
        victim_weight = victim[3]
        victim_tone = victim[4]
        victim_eyecolors = victim[5]
        victim_hairlengths = victim[6]
        victim_haircolors = victim[7]
=======
>>>>>>> 4fd7d2f3c9e74533d87762d6de8da30c639fcde2


    how = random.choice(murder_list["how"])
    why = random.choice(murder_list["why"])
    where = random.choice(murder_list["where"])
    address = GenerateAddres().generator()
    when = random.choice(murder_list["when"])
    who_name = name_gen.generator()
    who_relation = random.choice(murder_list["who"])
    who_job = GenerateJobs().generator()
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
            suspect_name_list.append("")
            suspect_relation_list.append("")
            suspect_job_list.append("")
    return render_template('hello.html',
    victim_name=victim_name,
    victimjob=victimjob,
    victim_height = victim_height,
    victim_weight=victim_weight,
    victim_tone=victim_tone,
    victim_eyecolors=victim_eyecolors,
    victim_hairlengths=victim_hairlengths,
    victim_haircolors=victim_haircolors,
    how=how,
    why=why,
    where=where,
    address=address,
    when=when,
    who_name=who_name,
    who_relation=who_relation,
    who_job=who_job,
    suspecta_name=suspecta_name,
    suspecta_relation=suspecta_relation,
    suspecta_job=suspecta_job,
    suspectb_name=suspectb_name,
    suspectb_relation=suspectb_relation,
    suspectb_job=suspectb_job,
    suspectc_name=suspect_name_list[0],
    suspectc_relation=suspect_relation_list[0],
    suspectc_job=suspect_job_list[0],
    suspectd_name=suspect_name_list[1],
    suspectd_relation=suspect_relation_list[1],
    suspectd_job=suspect_job_list[1],
    suspecte_name=suspect_name_list[2],
    suspecte_relation=suspect_relation_list[2],
    suspecte_job=suspect_job_list[2],
    suspectf_name=suspect_name_list[3],
    suspectf_relation=suspect_relation_list[3],
    suspectf_job=suspect_job_list[3],
    suspectg_name=suspect_name_list[4],
    suspectg_relation=suspect_relation_list[4],
    suspectg_job=suspect_job_list[4]
    )

if __name__ == "__main__":
    app.run()
