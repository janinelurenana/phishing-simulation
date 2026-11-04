# Phishing Website Simulation

A Flask-based phishing awareness simulation developed for an academic cybersecurity project. The application demonstrates how social engineering techniques can influence users to interact with fraudulent university login pages.

## Overview

The project simulates a university account verification scenario using a fictional institution, Northbridge University.

Users navigate through a mock university email, a simulated login portal, and an awareness page explaining the phishing techniques involved.

## Features

- Simulated university email interface.
- Fictional student login portal.
- Dummy credential validation.
- Flask session-based interaction handling.
- Phishing awareness and educational debrief page.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3

## Project Structure

```text
phishing-simulation/
│
├── app.py
│
├── templates/
│   ├── email.html
│   ├── login.html
│   └── awareness.html
│
├── static/
│   └── style.css
│
└── venv/
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone <repository-url>
cd phishing-simulation
```

**2. Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install flask
```

**4. Run the application**

```bash
python app.py
```

**5. Access the application**

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## Simulation Flow

1. **Simulated Email** – Users encounter a mock university account verification email.
2. **Login Portal** – The verification link redirects users to a fictional university login page.
3. **Credential Validation** – Submitted credentials are checked against a predefined dummy account.
4. **Awareness Page** – Users are redirected to an educational page explaining the simulated phishing attempt.

## Test Credentials

| Field | Value |
|---|---|
| Username | `student.demo` |
| Password | `DemoPass123!` |

## Security and Ethical Considerations

- Developed exclusively for educational and cybersecurity awareness purposes.
- Uses a fictional university identity.
- Uses predefined dummy credentials.
- Does not store submitted passwords.
- Uses Flask sessions to retain the submitted username and credential validation result.
- Intended for local testing and controlled demonstrations only.

## Disclaimer

This project is an academic cybersecurity simulation. It must not be used to impersonate real institutions, collect actual user credentials, or conduct unauthorized phishing campaigns.

## Author
**Christelle Janine M. Lurenana**
Developed as part of an academic cybersecurity project.
