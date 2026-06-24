from db.query import find_all_users

# Read
print(find_all_users()) #example

# # implement the rest of these queries in db/query and import the methods so the below works.
# print(find_user_by(id=3))
# print(find_user_by(email='mr.withers@amazing.co.uk')) # should fail

# # create
# create_user(fname="Mr.", lname="Withers", email="mr.withers@amazing.co.uk")
# print(find_user_by(email='mr.withers@amazing.co.uk')) # should not fail

# # delete
# delete_user(id=3)
# print(find_user_by(id=3)) # should fail

# # update (one field at a time)
# print(find_user_by(id=50))
# update_user_by_id(id=50, fname="Sir")
# print(find_user_by(id=50))
# update_user_by_id(id=50, lname="Kit")
# print(find_user_by(id=50))




# # Extra:

# # creating a user without all fields (other than id) should fail
# create_user(fname="Mr.", email="mr.blank@amazing.co.uk") => cause exception
# print(find_user_by(email="mr.blank@amazing.co.uk")) # should  fail

# # Specific SQL
# print(find_users_by_id_range(low, high))
# print(find_users_where_email_starts_with("a"))

# # Update any number of fields for a record
# update_user_by_id(id=50, fname="Eero", lname="Pleen")
# print(find_user_by(id=50))
# update_user_by_id(id=50, fname="Ellie", lname="Koptir", email="ellie.koptir@chinook.com")
# print(find_user_by(id=50))








