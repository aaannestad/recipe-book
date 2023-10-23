import yaml

with open('recipes.yaml') as dbfile:
    dbload = yaml.safe_load(dbfile)


#process:
# first let's get it printing the whole recipe
# then afterwards let's get it to sum up the ingredients and summarise them at the beginning

# TeX commands

preamble = r'''\documentclass{article}

\input{preamble.tex}

\begin{document}
'''

final = r'\end{document}'

def texbegin(cmd):
    return r'\begin{'+cmd+'}'
def texend(cmd):
    return r'\end{'+cmd+'}'

def printrecipes(db):
    indentnum = 0

    def writeline(text,indentnum):
        output.write(('  '*indentnum)+text+'\n')

    for recipe in db:
        rname = recipe['name']
        rserv = str(recipe['servings'])
        
        indentnum+=1

        writeline(texbegin('recipe')+'{'+rname+'}{'+rserv+'}', indentnum)

        for step in recipe['steps']:
            indentnum+=1
            writeline(texbegin('step'), indentnum)
            indentnum+=1
            writeline(texbegin('ingrs'), indentnum)
            indentnum+=1
            if 'ingredients' in step: 

                for ingredient in step['ingredients']:
                    unit = ingredient['unit']
                    item = ingredient['item']
                    if type(ingredient['qty']) is int:
                        quant = str(ingredient['qty'])
                    elif type(ingredient['qty']) is float:
                        quantratio = ingredient['qty'].as_integer_ratio()
                        quant = r'\nicefrac{'+str(quantratio[0])+'}{'+str(quantratio[1])+'}'
                    if ingredient['unit'] == 'item':
                        writeline(r'\itemingr{'+quant+'}{'+item+'}', indentnum)
                    else:
                        writeline(r'\ingr{'+quant+'}{'+unit+'}{'+item+'}', indentnum)


            if 'tools' in step:
                for tool in step['tools']:
                    writeline(r'\tool{'+tool+'}', indentnum)

            indentnum-=1
            writeline(texend('ingrs'), indentnum)
            indentnum-=1

            indentnum+=1
            desc = step['desc']
            writeline(texbegin('stepdesc'),indentnum)
            indentnum+=1
            writeline(desc, indentnum)
            indentnum-=1
            writeline(texend('stepdesc'), indentnum)
            indentnum-=1

            writeline(texend('step'), indentnum)
            indentnum-=1

    writeline(texend('recipe'), 1) 
    indentnum-=1

with open('recipes.tex', 'w') as output:
    output.write(preamble)
    printrecipes(dbload)
    output.write(final)
