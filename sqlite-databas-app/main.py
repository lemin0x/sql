import datatbase

# datatbase.Create()


#add a record to database
# datatbase.add_one()


#delete Record use rowid as string 
# datatbase.delete_one('6')

#Add many records
# stuff = [
#     ('med ', 'mahmoud','mahm@exemple.com'),
#     ('zahra', 'teyib','zahra@exemple.com'),
#     ('mami', 'sidi','masidi@exepole.com'),
# ]
# datatbase.add_many(stuff)

#lookup Email addres Records
# datatbase.email_lookup('masidi@exepole.com')

# Show all the records database
datatbase.show_all()