def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians =[]

    while magicians:
        magician = magicians.pop()
        great_magician = magician + " The Great "
        great_magicians.append(great_magician)


    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians



    
  


magician_name = ['paul' , 'james' , 'samuel', 'tim']
show_magicians(magician_name)

print("\n")
great_magicians = make_great(magician_name[:])
show_magicians(great_magicians)

print("\n")
show_magicians(magician_name)


