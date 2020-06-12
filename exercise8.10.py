def show_magicians(magicians):
    for names in magicians:
        print(names)

def make_great(magicians):
    great_magicians =[]

    while magicians:
        magician = magicians.pop()
        great_magician = magician + " The Great "
        great_magicians.append(great_magician)


    for great_magician in great_magicians:
        magicians.append(great_magician)


    
  


magician_name = ['paul' , 'james' , 'samuel', 'tim']
show_magicians(magician_name)

print("\n")
make_great(magician_name)
show_magicians(magician_name)


