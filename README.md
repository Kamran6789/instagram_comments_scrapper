# 📲 Instagram Comment Scraper using Playwright & MySQL

This project automates the process of logging into Instagram, navigating to specific profiles or posts, scraping all available comments, and storing them in a MySQL database. Built with [Playwright](https://playwright.dev/) for browser automation and [MySQL Connector](https://pypi.org/project/mysql-connector-python/) for database operations, it is designed to simulate human behavior and avoid detection by Instagram's anti-bot mechanisms.

---

## 🚀 Features

- ✅ **Instagram Login Automation**
- ✅ **Simulates Human-like Behavior** (random delays, scrolling, etc.)
- ✅ **Scrapes Comments** from specific posts or profile feeds
- ✅ **Keyword Matching** (e.g. highlight or filter comments containing a word like "mata")
- ✅ **Stores Comments in MySQL Database**
- ✅ **Creates Table Automatically if Not Exists**

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core scripting language |
| Playwright | Headless browser automation |
| MySQL | Data storage |
| mysql-connector-python | Python interface for MySQL |
| Random & Time | Delay functions to mimic human behavior |

---

## 📦 Installation

pip install playwright mysql-connector-python
playwright install

