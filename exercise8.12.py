def make_sandwiches(*ingredients):
    
    print("\nOrdering sandwiches with these ingredients: ")
    for ingredient in ingredients:
        print("- " + ingredient.title())


make_sandwiches('ham')
make_sandwiches('ham', 'cheese')
make_sandwiches('tuna' , 'sweetcorn', 'mayo')
