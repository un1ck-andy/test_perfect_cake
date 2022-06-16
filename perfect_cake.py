from math import sqrt
from resource import getrusage, RUSAGE_SELF
from argparse import ArgumentParser


# for memusage test
# @profile
def main(args):
    if args.numbers and args.radius:
        n = int(args.numbers)
        r = int(args.radius)
    else:
        n = int(input("Скільки ярусів має бути? "))
        r = int(input("Який радіус найбільшого ярусу? "))

    print("Радіус найменшого ярусу:")
    print(cake_calculate(n, r))

    # for runtime test
    # print(getrusage(RUSAGE_SELF))


def cake_calculate(n, r):
    x = sqrt((r * r) / n)
    return "%.5f" % x


if __name__ == "__main__":
    parser = ArgumentParser(description="Вирахуємо ідеальний торт")

    parser.add_argument("-n", "--numbers", help="Кількість ярусів")
    parser.add_argument("-r", "--radius", help="Радіус найбільшого ярусу")
    args = parser.parse_args()

    main(args)
