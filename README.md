# 🌿 Certweb – Energy Certificate Platform

![Banner](docs/images/banner.png) <!-- Replace with your own screenshot -->

**Certweb** is a web application built with **Django** that allows users to request **energy certificates** quickly and professionally.  
The project showcases my skills as a **Mechanical Engineer** and full-stack developer with **Python/Django**, including responsive frontend design and a working contact form with email integration.

---

## 💻 Tech Stack

- **Backend:** Django 5.2  
- **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript  
- **Database:** MySQL  
- **Email integration:** Django `send_mail` (console backend for development, SMTP for production)  
- **Version control:** Git / GitHub  

---

## 📂 Project Structure
Certweb/
├── Certweb/ # Django project settings
├── CertwebAPP/ # Main app (Home, Services, About)
├── ContactAPP/ # Contact form app (forms, email sending)
├── static/ # CSS, images, JS
└── templates/ # HTML templates

---

## 🚀 Features

1. **Landing page** with services and about section.  
2. **Functional contact form** with email sending:  
   - Sends user data (Name, Email, Phone, Address, Message).  
   - In development, emails are printed to the console.  
   - In production, emails are sent via Gmail SMTP.  
3. **Services page** highlighting the value of energy certificates.  
4. **Responsive design** (mobile & tablet friendly).  
5. **Navigation bar and footer** styled with modern CSS.  
6. **MySQL integration** for scalable data storage.  

---

## 📸 Screenshots

### Home
![Home](docs/images/home.png)

### Services
![Services](docs/images/services.png)

### Contact Form
![Contact](docs/images/contact.png)

### Thank You Page
![Thanks](docs/images/thanks.png)

---

## ⚙️ Installation

1. Clone the repository:

```bash
