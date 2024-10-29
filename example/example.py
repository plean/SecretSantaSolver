from participants import participants


def main():
    assignments = secret_santa(participants)
    for giver, recipient in assignments.items():
        print(f"{giver} will gift to {recipient}")
    pass


if __name__ == '__main__':
    main()
    pass
