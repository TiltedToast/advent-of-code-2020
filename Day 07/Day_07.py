inpt = open("input.txt").read().strip().split("\n")


class Bag:
    def __init__(self, desc):
        self.desc = desc
        self.results = []

        self.checked = False
        self.contains_gold = False

    def add_child(self, obj, count):
        self.results.append((obj, count))

    def check_gold(self):
        for result in self.results:
            if result[0].checked:
                continue

            result[0].check_gold()

            if self.desc == "muted yellow":
                print(result[0].desc)
                print(result[0].contains_gold)

        if len(self.results) == 0:
            self.checked = True
            return

        if "shiny gold" in self.desc:
            self.checked = True
            self.contains_gold = True
            return

        for result in self.results:
            if result[0].contains_gold:
                self.contains_gold = True
                break
        self.checked = True

    def check_num_bags(self):
        total = 0
        for result in self.results:
            total += result[1]
            total += result[0].check_num_bags() * result[1]
        return total


bags = {}
bag_to_obj = {}

for bag in inpt:
    original = f"{bag.split()[0]} {bag.split()[1]}"
    output = [(f"{result.split()[1]} {result.split()[2]}", result.split()[0]) for result in
              bag.split("contain ")[1].split(", ")]
    bags[original] = output

for bag in bags:
    bag_to_obj[bag] = Bag(bag)

for bag in bag_to_obj:
    results = bags[bag]
    if results[0][0] == 'other bags.':
        continue

    for result in results:
        bag_to_obj[bag].add_child(bag_to_obj[result[0]], int(result[1]))

for bag in bag_to_obj:
    bag_to_obj[bag].check_gold()

bag_to_obj["shiny gold"].contains_gold = False

print(sum(bag_to_obj[bag].contains_gold for bag in bag_to_obj))
print(bag_to_obj["shiny gold"].check_num_bags())
