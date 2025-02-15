# 🚀 Arkxion Organization

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/arkxion/arkxion-org)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-Framework-blue?logo=flask)](https://flask.palletsprojects.com/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-Server-brightgreen?logo=gunicorn)](https://gunicorn.org/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deployment-success?logo=github)](https://pages.github.com/)

## 🌟 Project Overview

This repository is dedicated to building the **Arkxion Organization's** web application.<br>
It utilizes the `Flask` framework and supports **static site generation** via `Frozen-Flask`.<br>
Additionally, it is designed for **easy deployment on GitHub Pages**.

## 📦 Installation

Follow these steps to set up the application:

### 1️⃣ Using Docker

```sh
git clone https://github.com/arkxion/arkxion-org.git
cd arkxion-org
docker-compose up -d --build
```

### 2️⃣ Running in a Local Environment

```sh
git clone https://github.com/arkxion/arkxion-org.git
cd arkxion-org
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r docker/requirements.txt
python src/run.py
```

---

## 🌍 Internationalization (i18n) Setup

This application supports multiple languages (`ja`, `en_US`, `en_UK`) and uses `gettext` for translation management.

### 1️⃣ Extract Translations

To update translation files (`messages.pot`), run:

```sh
pybabel extract -F src/app/babel.cfg -o src/app/translations/messages.pot src/app
```

### 2️⃣ Initialize Language Directories

```sh
pybabel init -i src/app/translations/messages.pot -d src/app/translations -l ja
pybabel init -i src/app/translations/messages.pot -d src/app/translations -l en_US
pybabel init -i src/app/translations/messages.pot -d src/app/translations -l en_UK
```

### 3️⃣ Compile Translations

```sh
pybabel compile -d src/app/translations
```

---

## 🏗️ Static Site Generation (GitHub Pages)

This project supports **static site generation** using `Frozen-Flask` and can be deployed via **GitHub Pages**.

### 1️⃣ Generate Static Site

```sh
python src/freeze.py
```

This will output static files to the `docs/` directory.

### 2️⃣ Setup GitHub Pages

Navigate to **Settings > Pages** in the repository and set:  
📌 **Branch:** `main` → **Folder:** `docs/`  

This enables **automatic deployment via GitHub Pages**.

---

## 🚀 Running the Application

### 1️⃣ Run with Docker Compose

```sh
docker-compose down
docker-compose up -d --build
```

### 2️⃣ Run in Flask Development Mode

```sh
python src/run.py
```

### 3️⃣ Update and Deploy Static Site

After making changes, apply updates with:

```sh
python src/freeze.py
git add docs/
git commit -m "Update static site"
git push origin main
```

---

## 📜 Project Structure

```
arkxion-org/
│── .github/             # GitHub-specific configuration
│   ├── workflows/       # CI/CD workflows
│   │   ├── deploy.yml
│   │   ├── main.yml
│   │   ├── security_scan.yml
│   │   ├── static.yml
│   ├── ISSUE_TEMPLATE/  # Issue templates
│   ├── PULL_REQUEST_TEMPLATE/
│   ├── dependabot.yml   # Dependabot configuration
│   ├── SECURITY.md      # Security policy
│
│── ci_cd/               # CI/CD configurations
│   ├── github_actions/
│   │   ├── main.yml
│   │   ├── security_scan.yml
│   ├── jenkins/
│   │   ├── pipeline.groovy
│
│── docker/              # Docker environment
│   ├── Dockerfile
│   ├── requirements.txt
│
│── docs/                # Static site output for GitHub Pages
│   ├── index.html
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   ├── js/
│   │   ├── pdf/
│   │   ├── video/
│
│── src/                 # Main application source code
│   ├── app/             # Flask application
│   │   ├── static/
│   │   ├── templates/
│   │   ├── translations/ # i18n files
│   │   ├── views/
│   │   ├── __init__.py
│   ├── config/          # Configuration files
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   ├── __init__.py
│   ├── freeze.py        # Static site generation script
│   ├── run.py           # Flask application entry point
│
│── .editorconfig        # Code style settings
│── .gitignore           # Git ignore rules
│── docker-compose.yml   # Docker Compose configuration
│── LICENSE              # Project license
│── README.md            # This file
```

---

## 🎯 Contributing

We welcome contributions to this project!  
For bug reports or feature suggestions, please open an **[Issue](https://github.com/arkxion/arkxion-org/issues)**.

---

📌 **License**: MIT License  
© 2025 Arkxion Organization. All Rights Reserved.
