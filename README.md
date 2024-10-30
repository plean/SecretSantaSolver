# Secret Santa Solver

The **Secret Santa Solver** is a Python tool designed to assign Secret Santa gift pairs for a group of participants. Each participant has the option to specify a list of people they feel comfortable gifting to, allowing for a personalized and comfortable gift exchange experience. If no preferences are specified, the participant can be assigned to any other participant.

## Features

- **Customizable Gift Preferences**: Participants can specify individuals they feel comfortable gifting to. If no preferences are given, they are open to gifting to anyone.
- **Fair Assignment**: Each participant is both a gift giver and receiver, with assignments matching each participant's preferences.
- **Email Notification**: Optionally, send email notifications to participants with their assigned recipient's information.

## Getting Started

### Prerequisites

- Python 3.7+
- `smtplib` (optional, for email notifications)

### Installation

Clone the repository to your local environment:

```bash
git clone https://github.com/yourusername/secret-santa-solver.git
cd secret-santa-solver
```

Install any required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Input Format

The Secret Santa Solver expects a list of participants in the following format:

```python
participants = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'links': None  # Alice is open to gifting anyone
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'links': ['Alice', 'Charlie']  # Bob prefers gifting Alice or Charlie
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'links': None  # Charlie is open to gifting anyone
    },
    # Add as many participants as needed
]
```

Each dictionary in the `participants` list should contain:
- `name` (str): Participant's name.
- `email` (str): Participant's email address.
- `links` (list or None): A list of names the participant feels comfortable gifting to. If `None`, the participant is open to gifting to anyone.

### Running the Secret Santa Solver

1. Save your list of participants in a file or define it directly in the code.
2. Import and call the solver function.

Example usage:

```python
from secret_santa_solver import secret_santa

participants = [
    {'name': 'Alice', 'email': 'alice@example.com', 'links': None},
    {'name': 'Bob', 'email': 'bob@example.com', 'links': ['Alice', 'Charlie']},
    {'name': 'Charlie', 'email': 'charlie@example.com', 'links': None},
    # Add more participants here
]

assignments = secret_santa(participants)

for giver, recipient in assignments.items():
    print(f"{giver} will gift to {recipient}")
```

This will output the Secret Santa assignments based on the participants' preferences.

### Optional: Sending Notifications

To notify participants of their assigned recipients, use the `send_email_notifications` function. You will need an SMTP email service configured with your credentials.

```python
from secret_santa_solver import send_email_notifications

send_email_notifications(assignments, smtp_server='smtp.example.com', smtp_port=587,
                         email_user='your_email@example.com', email_password='your_password')
```

## Function Documentation

### `secret_santa(participants)`

This function takes a list of participants and assigns each participant a recipient they feel comfortable gifting to, if possible.

- **Parameters**: 
  - `participants` (list): A list of dictionaries, each containing `name`, `email`, and `links`.
- **Returns**:
  - `dict`: A dictionary with each participant's name as the key and their assigned recipient's name as the value. If `None`, that mean the solver haven't found a solution after trying `MAX_RETRY` times.

### `send_email_notifications(assignments, smtp_server, smtp_port, email_user, email_password)`

Optionally send email notifications to each participant about their Secret Santa assignment.

- **Parameters**:
  - `assignments` (dict): Dictionary output from `secret_santa` containing givers and recipients.
  - `smtp_server` (str): SMTP server address.
  - `smtp_port` (int): SMTP server port.
  - `email_user` (str): SMTP username/email.
  - `email_password` (str): SMTP password.

## Example Output

After running the program, the output will show assignments such as:

```plaintext
Alice will gift to Charlie
Bob will gift to Alice
Charlie will gift to Bob
```

Each participant is both a giver and receiver, and assignments follow their preferences when specified.

## Contributing

If you’d like to contribute, please fork the repository and submit a pull request. Feel free to open issues for suggestions or bugs.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for details.
