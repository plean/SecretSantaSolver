from participants import participants
from secret_santa_solver import secret_santa, send_email_notification


def main():
    assignments = secret_santa(participants)

    for giver, recipient in assignments.items():
        print(f"{giver} will gift to {recipient}")

    send_email_notifications(
        assignments,
        participants,
        smtp_server="smtp.example.com",
        smtp_port=587,
        email_user="your_email@example.com",
        email_password="your_password"
    )
    pass


if __name__ == '__main__':
    main()
    pass
