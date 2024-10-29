from participants import participants
from secret_santa_solver import secret_santa


def main():
    assignments = secret_santa(participants)
    for giver, recipient in assignments.items():
        print(f"{giver} will gift to {recipient}")
    pass


if __name__ == '__main__':
    main()
    pass
