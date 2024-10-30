import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_notifications(assignments, participants, smtp_server, smtp_port, email_user, email_password):
    """
    Sends email notifications to each participant in the Secret Santa.
    
    Parameters:
        assignments (dict): A dictionary with each participant's name as the key and their assigned recipient's name as the value.
        participants (list): A list of dictionaries, each containing name, email, and links.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port (e.g., 587 for Gmail).
        email_user (str): SMTP username/email (sender's email).
        email_password (str): SMTP password (sender's email password).
    """
    
    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(email_user, email_password)

        for giver, recipient in assignments.items():
            # Get the giver's email and recipient's name
            giver_email = next(p['email'] for p in participants if p['name'] == giver)
            recipient_name = recipient
            
            # Create the email message
            message = MIMEMultipart()
            message['From'] = email_user
            message['To'] = giver_email
            message['Subject'] = "Your Secret Santa Assignment 🎅🎄"
            
            # Email body
            body = f"Hello {giver},\n\nYou have been chosen to be the Secret Santa for {recipient_name}!\n" \
                   f"Get creative with your gift idea and keep it a surprise! 🎁\n\nHappy gifting and happy holidays!\n\nBest,\nSecret Santa Organizer"
            
            message.attach(MIMEText(body, 'plain'))
            
            # Send the email
            try:
                server.sendmail(email_user, giver_email, message.as_string())
                print(f"Email sent to {giver} ({giver_email}) with recipient {recipient_name}.")
            except Exception as e:
                print(f"Failed to send email to {giver} ({giver_email}): {e}")
