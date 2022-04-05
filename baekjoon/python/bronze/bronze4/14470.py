def main():
    a_temperature = int(input())
    target_temperature = int(input())
    gril_point_1_celcius_frozen_time = int(input())
    melt_point_time = int(input())
    gril_point_1_celcius_time = int(input())

    total_time = 0
    if a_temperature < 0:
        total_time = ((0 - a_temperature) * gril_point_1_celcius_frozen_time) + \
            melt_point_time + (target_temperature * gril_point_1_celcius_time)
    else:
        total_time = gril_point_1_celcius_time * \
            (target_temperature - a_temperature)

    print(total_time)


if __name__ == "__main__":
    main()
