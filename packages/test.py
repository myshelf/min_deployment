from reg_demo.version_management import get_data, write_data

get_data()
write_data("Overwriting data!")
get_data()

if __name__ == "__main__":
    main()
