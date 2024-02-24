################## Nested Dictionary #######################

student = {
    "name" : "Nasim",
    "subject" : {
        "phy" : 87,
        "che" : 90,
        "mat" : 95,
        "department" : {
            "computer" : 80,
            "eletronics" : 90,
            "electical" : 70}
        }
    }
print(student)
print(student["subject"]["phy"])
print(student["subject"]["department"]["computer"])
