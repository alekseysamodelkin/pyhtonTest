# -----------------------------
# Program by Samodelkin
# -----------------------------


def create_record(name, tel, address):
    "Create Record"
    record={
        'name': name,
        'phone': tel,
        'address': address
    }
    return record

user1 = create_record("Petr","+89367498374", "Moscow")
user2 = create_record("Artem", "+6382648234", "Kazan")


print(user1)
print(user2)

def give_award(medal, *persons):
    "give medals for persons"
    for person in persons:
        print("komrad " + person.title() + " nagrada " + medal)



give_award("za_Berlin", "vasya", "petr")
give_award("za_Moskvu", "petr", "oleg")


