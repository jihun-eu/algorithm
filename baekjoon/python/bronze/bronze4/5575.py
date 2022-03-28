def split_work_time(work_time_lst):
    splitter = len(work_time_lst) // 2

    return work_time_lst[:splitter], work_time_lst[splitter:]


def get_work_time(go_to_work, get_off_work):
    working_time = [0] * 3
    for i, t in enumerate(zip(go_to_work, get_off_work)):
        during = t[-1] - t[0]

        working_time[i] = during

    carry = 0
    for i in range(2, -1, -1):
        if carry:
            working_time[i] += carry
            carry = 0
        if working_time[i] < 0:
            working_time[i] += 60
            carry = -1

    print(*working_time)


def main():
    employees = [list(map(int, input().split())) for _ in range(3)]
    for employee in employees:
        employee_go_to_work, employee_get_off_work = split_work_time(employee)
        get_work_time(employee_go_to_work, employee_get_off_work)


if __name__ == "__main__":
    main()
