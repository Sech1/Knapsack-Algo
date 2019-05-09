def main():
    item_num, weight_bound, parse_data = open_file_parse()
    bagged = knapsack(parse_data, weight_bound)
    # EX: The optimal Knapsack solution has total value 11 and involves items {1, 2, 4}
    bagged = sorted(bagged, key=lambda item: item[0])
    total_value = sum_value(bagged)
    sorted_items = return_item_set(bagged)
    out_string = "The optimal Knapsack solution has a total value {0} and involves items {1}".format(total_value,
                                                                                                     sorted_items)
    print(out_string)


def sum_value(bagged_items):
    total = 0
    for item in bagged_items:
        total += item[2]
    return total


def return_item_set(bagged_items):
    items = set()
    for item in bagged_items:
        items.add(item[0])
    return items


def knapsack(items, weight_bound):
    table = [[0 for weight in range(weight_bound + 1)] for item in range(len(items) + 1)]

    for item, weight, value in items:
        for weight_val in range(1, weight_bound + 1):
            if weight > weight_val:
                table[item][weight_val] = table[item - 1][weight_val]
            else:
                table[item][weight_val] = max(table[item - 1][weight_val], table[item - 1][weight_val - weight] + value)

    result = []
    weight_val = weight_bound
    for item, weight, value in reversed(items):
        was_added = table[item][weight_val] != table[item - 1][weight_val]
        if was_added:
            item, weight, value = items[item - 1]
            result.append(items[item - 1])
            weight_val -= weight

    return result


def open_file_parse():
    with open("input/knapsack.txt") as f:
        data = f.readlines()
        split = data[0].strip('\n')
        item_num = int(split.split(' ')[0])
        weight_bound = int(split.split(' ')[1])
        data.pop(0)
        parse_data = list()
        item_name = 1
        for line in data:
            split = line.strip('\n')
            weight = split.split(' ')[0]
            value = split.split(' ')[1]
            parse_data.append([item_name, int(weight), int(value)])
            item_name += 1
    f.close()

    return item_num, weight_bound, parse_data


if __name__ == "__main__":
    main()
