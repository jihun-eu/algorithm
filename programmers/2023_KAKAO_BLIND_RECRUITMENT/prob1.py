from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def main(today, terms, privacies):
    terms = {term.split()[0]: int(term.split()[1]) for term in terms}
    def func(today): return datetime.strptime(today, "%Y.%m.%d")
    today = func(today)
    answer = []
    for i, privacy_info in enumerate(privacies):
        registered_date, privacy = privacy_info.split()
        if (func(registered_date) + relativedelta(months=terms[privacy])) <= today:
            answer.append(i+1)
    return answer


if __name__ == "__main__":
    t = main("2022.05.19", ["A 6", "B 12", "C 3"], [
        "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
    print(t)
