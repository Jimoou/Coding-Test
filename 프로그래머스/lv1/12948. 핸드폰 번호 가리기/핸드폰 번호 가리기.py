import re
def solution(phone_number):
    if len(phone_number) == 4:
        return phone_number
    return re.sub('\d',"*", phone_number, len(phone_number) - 4)