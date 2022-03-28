
def x_fee(fee, usage):
    return usage * fee


def y_fee(default_fee, fee, limit_usage, usage):
    if usage <= limit_usage:
        return default_fee
    return (usage - limit_usage) * fee + default_fee


def main():
    x_bill_by_l = int(input())
    y_default_fee = int(input())
    y_default_usage_limit = int(input())
    y_add_fee_by_l = int(input())
    joi_usage = int(input())

    print(min(x_fee(x_bill_by_l, joi_usage), y_fee(
        y_default_fee, y_add_fee_by_l, y_default_usage_limit, joi_usage)))


if __name__ == "__main__":
    main()
