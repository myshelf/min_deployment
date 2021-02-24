from reg_demo.version_management import get_data, write_data

data = get_data()
print(data)
write_data(new_contents = "The data!")
data = get_data()
print(data)

# data = get_data()
# print(data)
# write_data(new_contents = "Overwriting data!")
# data = get_data()
# print(data)