def solution(phone_book):
    hash = {}
    for number in phone_book:
        hash[number] = 1
    for number in phone_book:
        temp = ""
        for n in number:
            temp += n
            if temp in hash and temp != number:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
