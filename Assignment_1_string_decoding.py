def find_complete_number(batch):
    complete_number = []
    for x in batch:
        if x.isdigit():
            complete_number.append(x)
        else:
            break
    complete_number = "".join(complete_number)
    return complete_number


def check_if_batch_is_valid(batch):
    # start from the 1st character of the batch
    index = 0
    # if index is smaller than the length of batch, continue
    while index < len(batch): 
        # if it is the 1st character
        if index == 0:
            # use user-defined function to find total_test
            total_test = find_complete_number(batch) 
            # determine the length of total_test 
            length_of_total_test = len(total_test) 
            # find the next index after total test
            index = index + length_of_total_test 
            # if total_test is the entire batch, there is no character
            # after total_test, it's invalid
            if index < len(batch):
                continue
            else:
                isValid = False
                break
        # if it is not the 1st character
        else:
            # if batch[index] is '+', then run:
            if batch[index] == '+':
                # locate the index of '+' in this batch
                index_of_plus_sign = batch.find('+') 
                # if there is more character after '+' and this character is a number, then continue
                if (index_of_plus_sign+1 < len(batch)) and (batch[index_of_plus_sign+1].isdigit() == True):                                    
                    # find the substring after '+'
                    batch_after_plus_sign = batch[index_of_plus_sign+1:] 
                    # use user-defined function to find positive case 
                    positive_case = find_complete_number(batch_after_plus_sign) 
                    # determine the length of positive_case
                    length_of_positive_case = len(positive_case) 
                    # if the first character after '+' is 0 and the length of positive case is 1,
                    # positive_case is 0 and valid; if the first character after '+' is not 0, it's also valid
                    if ((batch[index_of_plus_sign+1] == '0') and length_of_positive_case == 1) or (batch[index_of_plus_sign+1] != '0'):
                        next_index_after_positive_case = length_of_total_test+1+length_of_positive_case 
                        #if there is more character after positive case and the character is '-', then continue
                        if next_index_after_positive_case<len(batch) and batch[next_index_after_positive_case] == '-':
                            # locate the index of '-' in this batch
                            index_of_minus_sign = batch.find('-')
                            # if there is more character after '-' and this character is a number, then continue
                            if ((index_of_minus_sign+1) < len(batch)) and (batch[index_of_minus_sign+1].isdigit() == True):
                                # find the substring after '-'
                                batch_after_minus_sign = batch[index_of_minus_sign+1:] 
                                # use user-defined function to find negative case
                                negative_case = find_complete_number(batch_after_minus_sign) 
                                # determine the length of negative_case 
                                length_of_negative_case = len(negative_case) 
                                # if the first character after '-' is 0 and the length of negative case is 1,
                                # negative_case is 0 and valid; if the first character after '-' is not 0, it's also valid
                                if ((batch[index_of_minus_sign+1] == '0') and length_of_negative_case == 1) or (batch[index_of_minus_sign+1] != '0'):                                                    
                                    # find index after last character
                                    index = length_of_total_test + length_of_positive_case + length_of_negative_case + 2 
                                    # if index after last character equals length of the batch, then continue 
                                    if index == len(batch): 
                                        # if total case equals to the addition of positive and negative cases, valid;
                                        # if not, invalid
                                        if int(total_test) == int(positive_case) + int(negative_case):                                                        
                                            isValid = True
                                            break
                                        else:
                                            isValid = False
                                            break
                                    # if index after last character does not equal length of the batch, there is more
                                    # character after last character, invalid
                                    else:
                                        isValid = False
                                        break
                                else:
                                    isValid = False
                                    break
                            # if there is no character after '-' or this character is not a number, invalid   
                            else:
                                isValid = False
                                break
                        #if there is no character after positive case or the character is not '-', invalid
                        else:
                            isValid = False
                            break                                                                                           
                    # if the first character after '+' is 0 but the length of positive case is not 1,
                    # it has leading zeros, so it's invalid; 
                    else:
                        isValid = False
                        break
                # if there is no character after '+' or the character after '+' is not a number,
                # invalid
                else:
                    isValid = False
                    break
            # if batch[index] is '-', then run:
            else:
                # locate the index of '-' in this batch
                index_of_minus_sign = batch.find('-') 
                # if the character after '-' exists and is a number, continue
                if (index_of_minus_sign+1 < len(batch)) and batch[index_of_minus_sign+1].isdigit() == True:
                    # find the substring after '-'
                    batch_after_minus_sign = batch[index_of_minus_sign+1:]
                    # use user-defined function to find negative case
                    negative_case = find_complete_number(batch_after_minus_sign)
                    # determine the length of negative_case
                    length_of_negative_case = len(negative_case)
                    # if the 1st character after '-' is 0 and the length of negative case is 1, then valid;
                    # if the 1st character after '-' is not 0, it's also valid
                    if ((batch[index_of_minus_sign+1] == '0') and length_of_negative_case == 1) or (batch[index_of_minus_sign+1] != '0'):
                        next_index_after_negative_case = length_of_total_test+1+length_of_negative_case
                        #if there is more character after negative case and the character is '+', then continue
                        if next_index_after_negative_case < len(batch) and batch[next_index_after_negative_case] == '+':
                            # locate the index of '+' in this batch
                            index_of_plus_sign = batch.find('+')
                            # if the character after '+' exists and is a number, continue
                            if (index_of_plus_sign+1) < len(batch) and batch[index_of_plus_sign+1].isdigit() == True:
                                # find the substring after '+'
                                batch_after_plus_sign = batch[index_of_plus_sign+1:]
                                # use user-defined function to find positive case
                                positive_case = find_complete_number(batch_after_plus_sign)
                                length_of_positive_case = len(positive_case)
                                # if the 1st character after '+' is 0 and length_of_positive_case is 1, it's valid
                                # if the 1st character after '+' is not 0, also valid
                                if ((batch[index_of_plus_sign+1] == '0') and length_of_positive_case == 1) or (batch[index_of_plus_sign+1] != '0'):
                                    # find index after last character
                                    index = length_of_total_test + length_of_negative_case + length_of_positive_case + 2
                                    # if index after last character equal length of batch, there is no character
                                    # after last character, continue
                                    if index == len(batch):
                                        # if total case equals to the addition of positive and negative cases, valid;
                                        # if not, invalid
                                        if int(total_test) == int(negative_case) + int(positive_case):
                                            isValid = True
                                            break
                                        else:
                                            isValid = False
                                            break
                                    # if index after last character does not equal length of the batch, there is more
                                    # character after last character, invalid
                                    else:
                                        isValid = False
                                        break
                                else:
                                    isValid = False
                                    break

                            # if the character after '+' does not exist or is not a number, invalid    
                            else:
                                isValid = False
                                break    
                        #if there is no character after negative case or the character is not '+', invalid    
                        else:
                            isValid = False
                            break
                    else:
                        isValid = False
                        break
                # if the character after '-' does not exist or is not a number, invalid
                else:
                    isValid = False
                    break

        # When the batch makes isValid equal to False, exit the while loop,
        # if not, continue
        if isValid == False:
            break
        else:
            continue

    return isValid


def isValidString(s):
    # if the string is '', invalid; else, continue
    if s != '':
        # Split the string s using R as a separator, and store split items in a list 
        list_split_by_R = s.split('R')
        # After using R as a separator, the first item in the list should be '' 
        if list_split_by_R[0] == '':
            # remove the 1st item in the list
            list_split_by_R.pop(0)
            # test each item in the list, starting from the 1st one
            for batch in list_split_by_R:
                # turn each character of the batch into a list
                each_batch_list = list(batch)
                # list valid characters that are allowed in the batch
                valid_ch = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-')
                # if all characters in the batch are in the list of valid_ch, then continue
                if all(ch in valid_ch for ch in each_batch_list):
                    # only continue when batch has at least one character
                    if len(batch)>0:
                        # if the 1st character of the batch is a number, then continue
                        if batch[0].isdigit():
                            # if the 1st character of the batch is not 0, then continue
                            if batch[0] != '0':
                                isValid = check_if_batch_is_valid(batch)                                
                                # When the batch makes isValid equal to False, exit the for loop,
                                # no need to evaluate next batch; if not, continue to evaluate the
                                # next batch
                                if isValid == False:
                                    break
                                else:
                                    continue
                            # if the 1st character of the batch is 0, invalid
                            else:
                                isValid = False
                                break
                        # if the 1st character of the batch is not a number, invalid
                        else:
                            isValid = False
                            break
                    # stop when there is no character in the batch
                    else:
                        isValid = False
                        break
                # if one character in the batch are not in the list of valid_ch, invalid
                else:
                    isValid = False
                    break
        # After using R as a separator, the first item in the list is not '', invalid
        else:
            isValid = False
    else:
        isValid = False
        
    return isValid

