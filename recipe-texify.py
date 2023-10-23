import yaml

with open('recipes.yaml') as dbfile:
    dbload = yaml.safe_load(dbfile)


#process:
# first let's get it printing the whole recipe
# then afterwards let's get it to sum up the ingredients and summarise them at the beginning

# TeX commands

def texbegin(cmd):
    return r'\begin{'+cmd+'}'
def texend(cmd):
    return r'\end{'+cmd+'}'

def printrecipes(db):
    indentnum = 0

    def writeline(text,indentnum):
        print(('  '*indentnum)+text)

    for recipe in db:
        rname = recipe['name']
        rserv = str(recipe['servings'])
        
        indentnum+=1

        writeline(texbegin('recipe')+'{'+rname+'}{'+rserv+'}', indentnum)

        for step in recipe['steps']:
            indentnum+=1
            writeline(texbegin('step'), indentnum)
            if 'ingredients' in step: 
                indentnum+=1
                writeline(texbegin('ingrs'), indentnum)
                for ingredient in step['ingredients']:
                    indentnum+=1
                    if type(ingredient['qty']) is int:
                        writeline(r'\ingr{', indentnum) #TODO: actual TEX
                    elif type(ingredient['qty']) is float:
                        print(ingredient['qty'].as_integer_ratio()) #TODO; actual TEX
                    indentnum-=1
                writeline(texend('ingrs'), indentnum)
                indentnum-=1

            writeline(texend('step'), indentnum)
            indentnum-=1

    writeline(texend('recipe'), 1) 
    indentnum-=1

printrecipes(dbload)
