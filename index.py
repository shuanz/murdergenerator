from flask import Flask
from flask import render_template
import random
import json
from generateAddress import GenerateAddres
import names

app = Flask(__name__)

@app.route('/')
def hello(name=None):

    with open('murderList.json') as lists:
        murder_list = json.load(lists)
    victim = names.get_full_name()
    how = random.choice(murder_list["how"])
    why = random.choice(murder_list["why"])
    where = random.choice(murder_list["where"])
    address = GenerateAddres().generator()
    when = random.choice(murder_list["when"])
    whoa = names.get_full_name()
    whob = random.choice(murder_list["who"])
    suspecta = names.get_full_name()
    suspectb = names.get_full_name()
    name_list = []
    list_size = random.randint(1,4)
    for i in range (0, list_size):
        name_list.append(names.get_full_name())
    if i < 4:
        for c in range (i, 4):
            name_list.append("")
    return render_template('hello.html',
    victm=victim,
    how=how,
    why=why,
    where=where,
    address=address,
    when=when,
    whoa=whoa,
    whob=whob,
    suspecta=suspecta,
    suspectb=suspectb,
    suspectc=name_list[0],
    suspectd=name_list[1],
    suspecte=name_list[2],
    suspectf=name_list[3],
    suspectg=name_list[4]
    )

if __name__ == "__main__":
    app.run()
