# Assignment1 - Object Oriented Programming
# Author - Rudolf Suguitan
# Student No. - C13460538

import httplib2

# Main
h = httplib2.Http(".cache")
f_header, myfile = h.request("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data")
myfile = myfile.decode().split("\n")

# add numeric values each attributes from over an under 50k
# these will later be used to get their avg and midpoint
age_o50 = 0
edu_o50 = 0
gain_o50 = 0
loss_o50 = 0
hours_o50 = 0
age_u50 = 0
edu_u50 = 0
gain_u50 = 0
loss_u50 = 0
hours_u50 = 0
# dictionary for attributes over 50k
workclass_o50 = {}
status_o50 = {}
occupation_o50 = {}
relationship_o50 = {}
race_o50 = {}
sex_o50 = {}
# dictionary for attributes under 50k
workclass_u50 = {}
status_u50 = {}
occupation_u50 = {}
relationship_u50 = {}
race_u50 = {}
sex_u50 = {}
# split each list with commas
for i in range(0, len(myfile) - 2):
    myfile[i] = myfile[i].split(", ")

# There are 2 sets of dictionary
# 1 set for for people earning over 50k and another set for people earning equal or less than 50k
# This part of code will add all discrete attributes into both sets of dictionaries but will only be equal to 0
# This means that the attribute is there but there are no occurances yet.
# This allows me to compare 2 particular attributes from both over and under 50k dictionaries
tr = 0  # count total number of line
for al in myfile:
    # if line is empty, break
    if al == "":
        break

    tr += 1  # increment to find total number of lines/people

    if al[1] in workclass_o50:
        workclass_o50[al[1]] = 0
    else:
        workclass_o50[al[1]] = 0

    if al[5] in status_o50:
        status_o50[al[5]] += 0
    else:
        status_o50[al[5]] = 0

    if al[6] in occupation_o50:
        occupation_o50[al[6]] += 0
    else:
        occupation_o50[al[6]] = 0

    if al[7] in relationship_o50:
        relationship_o50[al[7]] += 0
    else:
        relationship_o50[al[7]] = 0

    if al[8] in race_o50:
        race_o50[al[8]] += 0
    else:
        race_o50[al[8]] = 0

    if al[9] in sex_o50:
        sex_o50[al[9]] += 0
    else:
        sex_o50[al[9]] = 0

    if al[1] in workclass_u50:
        workclass_u50[al[1]] = 0
    else:
        workclass_u50[al[1]] = 0

    if al[5] in status_u50:
        status_u50[al[5]] += 0
    else:
        status_u50[al[5]] = 0

    if al[6] in occupation_u50:
        occupation_u50[al[6]] += 0
    else:
        occupation_u50[al[6]] = 0

    if al[7] in relationship_u50:
        relationship_u50[al[7]] += 0
    else:
        relationship_u50[al[7]] = 0

    if al[8] in race_u50:
        race_u50[al[8]] += 0
    else:
        race_u50[al[8]] = 0

    if al[9] in sex_u50:
        sex_u50[al[9]] += 0
    else:
        sex_u50[al[9]] = 0

print("\nTotal number of lines/people:", tr)
line_test = tr * 1  # used to get the desired amount lines in file to be tested

#########Train_set############

c_o50 = 0  # count how many over 50k
c_u50 = 0  # count how many under 50k
# this is going to be used to compare 7841 people earning over 50k with 7841 people earning 50k or less
# this is because there are only 7841 people earning over 50k and to make a fair comparison, i compared this people with also 7841 people earning under 50k
only = 7841  # this can be changed to 'only=tr*.75' to get data from the 75% of file but the accuracy will be lower since there will be more people earning less than 50k
for dct in myfile:
    # if line is empty, break
    if dct == "":
        break
    # adding numeric values to particular over 50k variable and incrementing each particular attribute in over 50k dictionary
    if dct[14] == '>50K':

        if c_o50 < only:  # do whats below until the amount of people obtained that earns over 50k is not the amount of only
            c_o50 += 1

            # convert these attributes into integer and add each to a particular variable
            age_o50 += int(dct[0])
            edu_o50 += int(dct[4])
            gain_o50 += int(dct[10])
            loss_o50 += int(dct[11])
            hours_o50 += int(dct[12])

            if dct[1] in workclass_o50:
                workclass_o50[dct[1]] += 1
                if dct[1] == '?':
                    workclass_o50[dct[1]] -= 1

            if dct[5] in status_o50:
                status_o50[dct[5]] += 1
                if dct[5] == '?':
                    status_o50[dct[5]] -= 1

            if dct[6] in occupation_o50:
                occupation_o50[dct[6]] += 1
                if dct[6] == '?':
                    occupation_o50[dct[6]] -= 1

            if dct[7] in relationship_o50:
                relationship_o50[dct[7]] += 1
                if dct[7] == '?':
                    relationship_o50[dct[7]] -= 1

            if dct[8] in race_o50:
                race_o50[dct[8]] += 1
                if dct[8] == '?':
                    race_o50[dct[8]] -= 1

            if dct[9] in sex_o50:
                sex_o50[dct[9]] += 1
                if dct[9] == '?':
                    sex_o50[dct[9]] -= 1

        elif c_o50 > only:
            break

    # adding numeric values to particular under 50k variable and incrementing each particular attribute in under 50k dictionary
    elif dct[14] == '<=50K':

        if c_u50 < only:  # do whats below until the amount of people obtained that earns under 50k is not the amount of only
            c_u50 += 1

            # convert these attributes into integer and add each to a particular variable
            age_u50 += int(dct[0])
            edu_u50 += int(dct[4])
            gain_u50 += int(dct[10])
            loss_u50 += int(dct[11])
            hours_u50 += int(dct[12])

            if dct[1] in workclass_u50:
                workclass_u50[dct[1]] += 1
                if dct[1] == '?':
                    workclass_u50[dct[1]] -= 1

            if dct[5] in status_u50:
                status_u50[dct[5]] += 1
                if dct[5] == '?':
                    status_u50[dct[5]] -= 1

            if dct[6] in occupation_u50:
                occupation_u50[dct[6]] += 1
                if dct[6] == '?':
                    occupation_u50[dct[6]] -= 1

            if dct[7] in relationship_u50:
                relationship_u50[dct[7]] += 1
                if dct[7] == '?':
                    relationship_u50[dct[7]] -= 1

            if dct[8] in race_u50:
                race_u50[dct[8]] += 1
                if dct[8] == '?':
                    race_u50[dct[8]] -= 1

            if dct[9] in sex_u50:
                sex_u50[dct[9]] += 1
                if dct[9] == '?':
                    sex_u50[dct[9]] -= 1

        elif c_u50 > only:
            break

###########Classifier###############

# calculating the average of numeric values in over 50k
avg_age_o50 = age_o50 / c_o50
avg_edu_o50 = edu_o50 / c_o50
avg_gain_o50 = gain_o50 / c_o50
avg_loss_o50 = loss_o50 / c_o50
avg_hours_o50 = hours_o50 / c_o50

# calculating the average of numeric values in under 50k
avg_age_u50 = age_u50 / c_u50
avg_edu_u50 = edu_u50 / c_u50
avg_gain_u50 = gain_u50 / c_u50
avg_loss_u50 = loss_u50 / c_u50
avg_hours_u50 = hours_u50 / c_u50

# calculating the midpoint of the averages of numeric values of over and under 50k
mp_age = (avg_age_o50 + avg_age_u50) / 2
mp_edu = (avg_edu_o50 + avg_edu_u50) / 2
mp_gain = (avg_gain_o50 + avg_gain_u50) / 2
mp_loss = (avg_loss_o50 + avg_loss_u50) / 2
mp_hours = (avg_hours_o50 + avg_hours_u50) / 2

print("\n\nAmout of people earning >50k used for comparison:", c_o50)
print("\nAmount of people earning <=50k used for comparison:", c_u50)

############Testing###################
'''
-this part of code finds out if the person is either earning below or over 50k
-this is done by reading each column of the current line of the file and compare it with the midpoints and other attributes in the dictionaries
-for example, if the age of the current line is over the midpoint of age, a counter for over 50k will increment. if its less then increment counter for less than 50k
-for discrete attributes, for example, private in workclass, it will check if private is in both sets of dictionary. if private occured more in over 50k
    dictionary, a counter for over 50k will increment. then if private occured more in under 50k dictionary, a counter for less 50k will increment
-this part of code is basically guessing if each column in the current line tend to be earning either greater or less than 50k
-at the end of each line, if the counter for over 50k is equal or greater than under 50k counter, the person is earning over 50k, else the person is earing less than 50k
'''
o_count = 0  # counter for over 50k
u_count = 0  # counter for under 50k

right = 0  # counter if the guess is right
wrong = 0  # counter if the guess is wrong

accuracy = 0  # percentage of right guess

prt = 0  # counter used to stop testing if the desired amount of lines has been reached
for row in myfile:
    # if line is empty, break
    if row == "":
        break

    if prt < line_test:  # if the desired amount of lines to test has not been reached do whats below
        prt += 1

        if mp_age < int(row[0]):
            o_count += 1
        elif mp_age > int(row[0]):
            u_count += 1

        if mp_edu < int(row[4]):
            o_count += 1
        elif mp_edu > int(row[4]):
            u_count += 1

        if mp_gain < int(row[10]):
            o_count += 1
        elif mp_gain > int(row[10]):
            u_count += 1

        if mp_loss < int(row[11]):
            o_count += 1
        elif mp_loss > int(row[11]):
            u_count += 1

        if mp_hours < int(row[12]):
            o_count += 1
        elif mp_hours > int(row[12]):
            u_count += 1
        # the process for each discrete attributes is the same as the first explained one
        # converting each into int to be able to make comparisons of occurances
        if int(workclass_o50[row[1]]) > int(
                workclass_u50[row[1]]):  # if row[1] occured more in workclass_o50, then increment o_count
            o_count += 1
        elif int(workclass_o50[row[1]]) < int(
                workclass_u50[row[1]]):  # if row[1] occured more in workclass_u50, then increment u_count
            u_count += 1
        elif int(workclass_o50[row[1]]) == int(
                workclass_u50[row[1]]):  # if equal, then increment o_count(more chance to earn more than 50k)
            o_count += 1

        if int(status_o50[row[5]]) > int(status_u50[row[5]]):
            o_count += 1
        elif int(status_o50[row[5]]) < int(status_u50[row[5]]):
            u_count += 1
        elif int(status_o50[row[5]]) == int(status_u50[row[5]]):
            o_count += 1

        if int(occupation_o50[row[6]]) > int(occupation_u50[row[6]]):
            o_count += 1
        elif int(occupation_o50[row[6]]) < int(occupation_u50[row[6]]):
            u_count += 1
        elif int(occupation_o50[row[6]]) == int(occupation_u50[row[6]]):
            o_count += 1

        if int(relationship_o50[row[7]]) > int(relationship_u50[row[7]]):
            o_count += 1
        elif int(relationship_o50[row[7]]) < int(relationship_u50[row[7]]):
            u_count += 1
        elif int(relationship_o50[row[7]]) == int(relationship_u50[row[7]]):
            o_count += 1

        if int(race_o50[row[8]]) > int(race_u50[row[8]]):
            o_count += 1
        elif int(race_o50[row[8]]) < int(race_u50[row[8]]):
            u_count += 1
        elif int(race_o50[row[8]]) == int(race_u50[row[8]]):
            o_count += 1

        if int(sex_o50[row[9]]) > int(sex_u50[row[9]]):
            o_count += 1
        elif int(sex_o50[row[9]]) < int(sex_u50[row[9]]):
            u_count += 1
        elif int(sex_o50[row[9]]) == int(sex_u50[row[9]]):
            o_count += 1

    elif prt > line_test:  # if the desired amount of lines to test has been reached, break for loop
        break
    # if o_count is greater than u_count and if the current line/person is earning over 50k (means correct guess) then increment right
    if o_count >= u_count:
        if row[14] == '>50K':
            right += 1
        elif row[14] == '<=50K':  # if the guess is incorrect, incremment wrong
            wrong += 1
    # if u_count is greater than o_count and if the current line/person is earning under 50k (means correct guess) then increment right
    elif o_count < u_count:
        if row[14] == '>50K':  # if the guess is incorrect, incremment wrong
            wrong += 1
        elif row[14] == '<=50K':
            right += 1
    # bring both counters back to 0 for the following line test
    o_count = 0
    u_count = 0

print("\n\nNumber of lines tested:", prt)
print("\nRight guesses:", right)
print("\nWrong guesses:", wrong)

accuracy = (right / (right + wrong)) * 100
print("\n\nAccuracy:", accuracy)

