NUM_DAYS = 5


def main():
    sales = [0] * NUM_DAYS

    print("Введите продажи за каждый день")

    for index in range(len(sales)):
        sales[index] = float(input(f'День # {index + 1}: '))

    print("Введенные значения: ")

    for value in sales:
        print(value)

    print("\nИТОГО:")
    print(sum(sales))


if __name__ == '__main__':
    main()