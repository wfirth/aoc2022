from math import floor
import yaml


def load_input():
    with open("./day11/input_tester.txt") as f:
            data = yaml.safe_load(f.read())
    return(data)

class Monkey:
    ...


class Monkeys:
    def __init__(self):
        self.monkeys = []

    def add_monkey(self, monkey: Monkey):
        self.monkeys.append(monkey)

    def move_item(self, item, target):
        self.monkeys[target].receive_item(item)

    def run_rounds(self, n_rounds):
        for n in range(n_rounds):
            self.run_round()
            if(n+1%2000==0):
                print(
                    " ".join([str(m.total_inspections) for m in self.monkeys])
                )


    def run_round(self):
        for monkey in self.monkeys:
            monkey.round()

    def print_monkeys_items(self):
        for monkey in self.monkeys:
            print(monkey.print_items())

    def print_monkeys_inspections(self):
        for monkey in self.monkeys:
            print(monkey.total_inspections)


class Monkey:
    def __init__(self, monkeys: Monkeys, true_target, false_target, operation, test, starting_items = []) -> None:
        self.monkeys = monkeys
        self.initial_state = starting_items
        self.items = starting_items
        self.true_target = true_target
        self.false_target = false_target
        self.operation = operation
        self.test = test
        self.total_inspections = 0

    def receive_item(self, item):
        self.items.append(item)

    def apply_operation(self, item):
        item.set_value(
            self.operation(item.value)
        )

    def check_test(self, item):
        return(self.test(item.value))

    def reduce_item(self, item):
        # item.set_value(
        #     floor(item.value / 3)
        # )
        item.set_value(
            item.value % 9699690 #96577
        )

    def round(self):
        for item in self.items:
            self.total_inspections += 1
            # Inspect
            self.apply_operation(item)
            # Evaluate worry
            self.reduce_item(item)
            # Test and move
            if self.check_test(item):
                self.monkeys.move_item(item, self.true_target)
            else:
                self.monkeys.move_item(item, self.false_target)
        # After a round, the items are all removed
        self.items = []

    def evaluate_original_items(self):
        if(len(self.items) != len(self.initial_state)):
            return(False)

        same = all([c == og for c, og in zip(self.items, self.initial_state)])
        return(same)

    def print_items(self):
        return(
            ", ".join([str(item.value) for item in self.items])
        )





class Item:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return(str(self.value))

    def set_value(self, new_value):
        self.value = new_value

def initialize_test():
    monkeys = Monkeys()

    monkey0 = Monkey(monkeys, 2, 3, lambda x: x * 19, lambda x: x % 23 == 0, [Item(79), Item(98)])
    monkey1 = Monkey(monkeys, 2, 0, lambda x: x + 6, lambda x: x % 19 == 0, [Item(54), Item(65), Item(75), Item(74)])
    monkey2 = Monkey(monkeys, 1, 3, lambda x: x * x, lambda x: x % 13 == 0, [Item(79), Item(60), Item(97)])
    monkey3 = Monkey(monkeys, 0, 1, lambda x: x + 3, lambda x: x % 17 == 0, [Item(74)])

    monkeys.add_monkey(monkey0)
    monkeys.add_monkey(monkey1)
    monkeys.add_monkey(monkey2)
    monkeys.add_monkey(monkey3)

    return(monkeys)

def initialize():
    monkeys = Monkeys()

    monkey0 = Monkey(monkeys, 1, 6, lambda x: x * 7, lambda x: x % 5 == 0, [Item(74), Item(64), Item(74), Item(63), Item(53)])
    monkey1 = Monkey(monkeys, 2, 5, lambda x: x * x, lambda x: x % 17 == 0, [Item(69), Item(99), Item(95), Item(62)])
    monkey2 = Monkey(monkeys, 4, 3, lambda x: x + 8, lambda x: x % 7 == 0, [Item(59), Item(81)])
    monkey3 = Monkey(monkeys, 0, 7, lambda x: x + 4, lambda x: x % 13 == 0, [Item(50), Item(67), Item(63), Item(57), Item(63), Item(83), Item(97)])
    monkey4 = Monkey(monkeys, 7, 3, lambda x: x + 3, lambda x: x % 19 == 0, [Item(61), Item(94), Item(85), Item(52), Item(81), Item(90), Item(94), Item(70)])

    monkey5 = Monkey(monkeys, 4, 2, lambda x: x + 5, lambda x: x % 3 == 0, [Item(69)])
    monkey6 = Monkey(monkeys, 1, 5, lambda x: x +7, lambda x: x % 11 == 0, [Item(54), Item(55), Item(58)])
    monkey7 = Monkey(monkeys, 0, 6, lambda x: x * 3, lambda x: x % 2 == 0,  [Item(79), Item(51), Item(83), Item(88), Item(93), Item(76)])

    monkeys.add_monkey(monkey0)
    monkeys.add_monkey(monkey1)
    monkeys.add_monkey(monkey2)
    monkeys.add_monkey(monkey3)
    monkeys.add_monkey(monkey4)
    monkeys.add_monkey(monkey5)
    monkeys.add_monkey(monkey6)
    monkeys.add_monkey(monkey7)

    return(monkeys)


def main():
    monkeys = initialize()
    monkeys.run_rounds(10000)
    inspections = [m.total_inspections for m in monkeys.monkeys]
    inspections.sort(reverse=True)
    output = inspections[0] * inspections[1]
    return(output)


if __name__ == "__main__":
    print(main())
