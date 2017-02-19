from operator import mul


def validate_nip(nip):
    nip = nip.replace('-', '')
    if len(nip) != 10 or not nip.isdigit():
        return False
    *digits, crc = map(int, nip)
    weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    check_sum = sum(map(mul, digits, weights))
    return check_sum % 11 == crc
