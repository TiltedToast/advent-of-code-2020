def load_data(file):
    with open(file, "r") as f:
        data_read = f.read()
    return data_read


class Passport:
    def __init__(self, init_string):
        self.data = {}
        fields = init_string.split()
        for field in fields:
            k, v = field.split(":")
            self.data[k] = v

    def has_all_fields(self):
        needed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for field in needed_fields:
            if field not in self.data.keys():
                return False
        return True

    def has_valid_fields(self):
        if not self.has_all_fields():
            return False

        invalidated = False
        for k, v in self.data.items():

            # Four digits; at least 1920 and at most 2002
            if k == "byr":
                if len(v) != 4:
                    invalidated = True
                if not 1920 <= int(v) <= 2002:
                    invalidated = True

            # Four digits; at least 2010 and at most 2020
            elif k == "iyr":
                if len(v) != 4:
                    invalidated = True
                if not 2010 <= int(v) <= 2020:
                    invalidated = True

            # Four digits; at least 2020 and at most 2030
            elif k == "eyr":
                if len(v) != 4:
                    invalidated = True
                if not 2020 <= int(v) <= 2030:
                    invalidated = True

            # A number followed by either cm or in
            # If cm at least 150 and at most 193, if inches at least 59 and at most 76
            elif k == "hgt":
                if v[-2:] == "cm":
                    if not 150 <= int(v[:-2]) <= 193:
                        invalidated = True
                elif v[-2:] == "in":
                    if not 59 <= int(v[:-2]) <= 76:
                        invalidated = True

            # A # followed by exactly six characters 0-9 or a-f
            elif k == "hcl":
                if len(v) != 7:
                    invalidated = True
                if v[0] != "#":
                    invalidated = True
                for c in v[1:]:
                    if c not in "0123456789abcdef":
                        invalidated = True

            # Exactly one of: amb blu brn gry grn hzl oth
            elif k == "ecl":
                if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    invalidated = True

            # A nine-digit number, including leading zeroes
            elif k == "pid":
                if len(v) != 9:
                    invalidated = True
                for c in v:
                    if c not in "0123456789":
                        invalidated = True
        if invalidated:
            return False
        return True


def get_passport_list(data):
    return [Passport(line) for line in data.split("\n\n")]


def main():
    data = load_data("input.txt")
    passports = get_passport_list(data)
    print(f"There are {sum(passport.has_all_fields() for passport in passports)} valid passports")
    print(f"There are {sum(passport.has_valid_fields() for passport in passports)} passports where "
          f"everything is present and valid")


if __name__ == '__main__':
    main()
