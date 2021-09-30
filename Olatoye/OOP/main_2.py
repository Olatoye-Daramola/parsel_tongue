import json

from class_task import *


def add_native():
    native_dict = {}
    native_ = Native(input("Enter Native's first name"), input("Enter Native's last name"),
                     input("Enter Native's gender"), input("Enter Native's sc_id"))
    native_dict["First Name"] = native_.first_name
    native_dict["Last Name"] = native_.last_name
    native_dict["Gender"] = native_.gender
    native_dict["SC ID"] = native_.sc_id

    return native_dict


def add_natives(number_of_natives):
    counter = 1
    dict_of_natives = {}
    while counter <= number_of_natives:
        dict_of_natives[f"Native {number_of_natives}"] = add_native()
        counter += 1
    return dict_of_natives


def add_cohort(cohort_number_):
    cohort_ = Cohort(cohort_number_, input("Enter Cohort name"))
    number_of_natives = int(input("Enter number of natives"))
    cohort_.natives_dict[f"Cohort {cohort_number_} ({cohort_.cohort_name})"] = add_natives(number_of_natives)
    return cohort_.natives_dict


def add_cohorts(number_of_cohorts):
    counter = 1
    dict_of_cohorts = {}
    while counter <= number_of_cohorts:
        cohort_number_ = input('Enter Cohort Number')
        dict_of_cohorts[f"Cohort {cohort_number_}"] = add_cohort(cohort_number_)
        counter += 1
    return dict_of_cohorts


def add_building():
    building_ = Building(input("Enter Building name"), input("Enter Building address"))
    number_of_cohorts = int(input("Enter number of cohorts"))
    building_.cohort_dict[f"Building {number_of_cohorts}"] = add_cohorts(number_of_cohorts)
    return building_.cohort_dict


def add_buildings(number_of_buildings_):
    counter = 1
    while counter <= number_of_buildings_:
        DataBase.general_dict[f"Building {number_of_buildings_}"] = add_building()
        counter += 1
    return DataBase.general_dict


number_of_buildings = input("Enter the number of buildings")
database = add_buildings(number_of_buildings)
print(database)


with open("sample_db.txt", 'w+') as f:
    # for line in database:
    #     print(line)
    #     f.write(line)
    #     f.write('\n')
    data = json.dumps(database)
    f.write(data)
