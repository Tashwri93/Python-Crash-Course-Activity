def show_magicians(magicians):
    for names in magicians:
        msg = "Magician " + names.title()
        print(msg)

magician_name = ['paul' , 'james' , 'samuel', 'tim']
show_magicians(magician_name)
