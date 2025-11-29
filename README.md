
📘 **WebSync Website V1– Selenium Automation Testing**

Automated UI Testing Framework using Python + Selenium + PyTest

🚀 Project Overview

This repository contains end-to-end UI automation test scripts for the WebSync – Digital Solutions website.
The goal of this automation project is to validate core website functionalities including:

Homepage validation

Navigation menu testing

About Us, Services, Products, Process pages

UI/UX validations

Contact page functionality

Workflow verification

Responsive behavior (future enhancement)

The automation tests are designed to be scalable, modular, and follow the Page Object Model (POM) structure.

🧰 **Tech Stack**

| Component           | Technology                      |
| ------------------- | ------------------------------- |
| **Language**        | Python 3.x                      |
| **Automation Tool** | Selenium WebDriver              |
| **Test Runner**     | PyTest                          |
| **Design Pattern**  | Page Object Model (POM)         |
| **Driver Manager**  | webdriver-manager               |
| **Report**          | PyTest HTML Report              |
| **Browser**         | Chrome (Incognito Mode Enabled) |


📁 **Project Structure**

WebSyncAutomation/
│
├── tests/
│   ├── test_homepage.py
│   ├── test_navigation.py
│   ├── test_services_page.py
│   ├── test_products_page.py
│   ├── test_process_page.py
│   └── test_contact_page.py
│
├── pages/
│   ├── base_page.py
│   ├── homepage.py
│   ├── navigation.py
│   ├── services_page.py
│   ├── products_page.py
│   ├── process_page.py
│   └── contact_page.py
│
├── utilities/
│   ├── driver_setup.py
│   ├── logger.py
│   └── helpers.py
│
├── reports/
│   ├── pytest-html-report.html
│
├── README.md
├── requirements.txt
└── conftest.py

🌐 **Test Coverage**

✔ **Homepage Tests**

Verify logo is displayed

Verify navigation links

Verify banner content

Verify Get Started & Appointment buttons

✔ **Navigation Menu**

About Us

Services

Products

Process

Contact

Bangla Language Switch

✔ **Services Page**

Validate service items

Validate CTA buttons

Validate workflow blocks

✔ **Products Page**

Validate Inventory Management System info

Validate Visit Now & Demo buttons

✔ **Process Page**

Verify all 4 phases

Validate descriptions

✔ **Contact Page**

Verify email, phone, locations

Verify Get In Touch functionality
