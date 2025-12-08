betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'},
                 {'Name': 'Lauren Smith',
                 'Phone': 'x5909',
                 'Street': '1480 Blossom Ave',
                 'City': 'San Jose',
                 'State': 'CA',
                 'Email': 'smith@macalester.edu'},
                 {'Name': 'Olivia Carbonara',
                  'Phone': 'x1635',
                  'Street': '1450 Plainview Ct',
                  'City': 'San Jose',
                  'State': 'CA',
                  'Email': 'carbonara@macalester.edu'}
                 ]

print(address_book)

def filter_by_city(city, address_book):
    matches = []
    for address in address_book:
        if address['City'] == city:
            matches.append(address)
    return matches

print(filter_by_city('Saint Paul' , address_book))
