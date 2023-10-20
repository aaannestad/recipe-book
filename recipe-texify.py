import yaml

with open('format.yaml') as dbfile:
    db = yaml.safe_load(dbfile)


#process:
# first let's get it printing the whole recipe
# then afterwards let's get it to sum up the ingredients and summarise them at the beginning

for recipe in db:
    for step in recipe['steps']:
        print(step)
