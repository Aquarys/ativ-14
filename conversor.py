def pol (cem):
  pol= cem*0.39
  print('{:.2f}'.format(pol))
  #return pol
  file = open('polegadas.txt', 'w+')
  file.write('o valor {:.1f}  centímetros é {:.2f} polegadas' .format(cem,pol))
  file.seek(0,0)
  file.read()
  file.seek(0,0)
  file.close()