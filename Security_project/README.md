# README - Security Monitoring System

## **Project Overview**
This project is a security monitoring system designed to detect unauthorized access attempts and trigger alerts. The system logs security events, captures images of potential culprits, and sends email notifications to the concerned recipient.

## **Directory Structure**
```
│   Culprit.jpg           # Captured image of the unauthorized user (if applicable)
│   location.py           # Retrieves the system's location
│   Logs.txt              # Stores security logs
│   mail.txt              # Stores recipient email ID
│   password.py           # Handles password verification and management
│   password.txt          # Stores encrypted password
│   pic.py                # Captures images using the webcam
│   rmail.txt             # Stores recipient email for alerts
│   sender.py             # Sends email notifications with logs and images
│   setup.py              # Initializes the system and configures credentials
│   trigger.py            # Monitors security events and triggers alerts
```

## **File Descriptions**

### `trigger.py`
- Monitors security events using Windows Event Logs.
- Detects failed login attempts or suspicious activities.
- Calls `pic.py` to capture an image of the intruder.
- Sends an alert email using `sender.py`.

### `sender.py`
- Sends an email alert with security logs and captured images.
- Reads recipient email from `rmail.txt`.
- Uses SMTP for sending emails.

### `pic.py`
- Captures an image using the system's webcam.
- Saves the image as `Culprit.jpg`.

### `location.py`
- Retrieves the system's approximate location.
- Can be used for additional security features.

### `password.py`
- Handles password storage and verification.
- Ensures secure authentication mechanisms.

### `setup.py`
- Initializes the system.
- Creates required configuration files like `password.txt` and `mail.txt`.

### `Logs.txt`
- Stores logs of security events and alerts triggered.

### `mail.txt`
- Stores the sender’s email credentials securely.

### `password.txt`
- Stores an encrypted version of the system password.

### `rmail.txt`
- Stores the recipient email address for receiving alerts.

## **How to Set Up**
```
│   git clone --no-checkout https://github.com/DurishettyAnirudh/Python.git
│   cd python
│   git sparse-checkout init --cone
│   git sparse-checkout set Security_project
│   git checkout    
```

1. Run `setup.py` to configure passwords and email settings.
2. Execute `trigger.py` to start monitoring security events.
3. Ensure `sender.py` has access to SMTP credentials.
4. The system will log security events, capture images, and send alerts automatically.

## **Requirements**
- Python 3.x
- Required Python libraries (install using `pip install -r requirements.txt` if applicable)
- Windows environment (for event log monitoring)

## **Usage**
- Run `trigger.py` to monitor unauthorized access attempts.
- If a breach is detected, `pic.py` captures the intruder's image, and `sender.py` sends an email alert.
- All logs are stored in `Logs.txt` for review.

## **Security Considerations**
- Ensure `password.txt` and `mail.txt` are stored securely.
- Avoid hardcoding sensitive credentials; use environment variables if possible.
- Regularly update email and password settings for security.

## **Future Improvements**
- Implement multi-factor authentication.
- Improve image capture quality and logging details.
- Enhance location tracking for better security monitoring.

