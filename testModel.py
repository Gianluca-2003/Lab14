from model.model import Model

myModel = Model()

myModel.buildGraph(3,5)

print(myModel.printGraph())

'''
path = myModel.trovaPercorsoPiuLungo(1584)
print('cammino piu lungo. Partendo da: ',1584)
print('Lunghezza: ',len(path))
for node in path:
    print(node)
'''
print('------------')

costo, camminoMax = myModel.trovaPercorsoPesoMassimo(101)
print(f"cammino con costo massimo")
print(f"costo: {costo}")
for node in camminoMax:
    print(node)