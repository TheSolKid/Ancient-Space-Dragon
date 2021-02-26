import json

file = open("lexico.txt", "r")
y = file.read()
diction = json.loads(y)
file.close()
sec_dict = {}


def parekleidia(diction):
    for keys, Timh in diction.items():
        if type(Timh) is dict:
            parekleidia(Timh)
            if keys in sec_dict:
                sec_dict[keys] += 1
            else:
                sec_dict[keys] = 1
        elif keys in sec_dict:
            sec_dict[keys] += 1
        else:
            sec_dict[keys] = 1
        if type(Timh) is list:
            for i in range(len(Timh)):
                if type(Timh[i]) is dict:
                    parekleidia(Timh[i])


parekleidia(diction)
TimiKleidiwn = max(sec_dict.items(), key=lambda x: x[1])
ListaKleidiwn = list()
for key, value in sec_dict.items():
    if value == TimiKleidiwn[1]:
        ListaKleidiwn.append(key)
print("Η μέγιστη τιμή ενός κλειδιού είναι: ", ListaKleidiwn)
