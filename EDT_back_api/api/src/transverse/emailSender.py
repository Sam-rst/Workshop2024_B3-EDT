from email.message import EmailMessage
import smtplib

sender = "workshop.studytime@outlook.com"

def envoyerMailToUser(user_email, username, password):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = user_email
    email["Subject"] = "STUDYTIME: première connexion à votre compte"
    
    message = f"""
    Bonjour,
    Voici vos identifiants de connexion pour l'application StudyTime :
    - Username: {username}
    - Mot de passe: {password}

    Si vous n'êtes pas à l'origine de cette demande, veuillez supprimer cet email.

    Cordialement,
    Le service SAV de StudyTime
    """
    
    email.set_content(message)

    # Utilisation du mot de passe d'application ici
    smtp = smtplib.SMTP("smtp.office365.com", port=587)
    smtp.starttls()
    smtp.login(sender, "Workshop2024!")  # Mot de passe d'application ici
    smtp.sendmail(sender, user_email, email.as_string())
    smtp.quit()

    return True
