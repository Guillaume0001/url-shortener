# 🚀 Django URL Shortener

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python\&logoColor=white) ![Django](https://img.shields.io/badge/django-5.0-green?logo=django\&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-success?logo=fastapi) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

**A modern URL shortener fully built on Django with API key authentication 🌐✨**  
*Turn your long links into short, shareable URLs quickly and efficiently! 🏎️💨*

---

## 🔥 Features

* ✂️ Shorten long URLs
* 🌐 Redirect short URLs to their original targets using Django
* 🛠️ REST API to create, list, and manage your URLs
* 🔑 API Key authentication for secure access
* ⚡ Fast JSON responses from FastAPI
* 🛡️ Error handling (invalid URL, link not found, etc.)

---

## 🧰 Prerequisites

* Python 3.11+ 🐍
* Django 5+ 🏗️
* Database: SQLite / PostgreSQL / MySQL 💾

---

## ⚡ Installation

**1️⃣ Clone the repo**

```bash
git clone https://github.com/Guillaume0001/url-shortener.git
cd url-shortener
```

**2️⃣ Create and activate a virtual environment**

```bash
python -m venv venv        # Linux might need: apt install python3-venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

**3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**5️⃣ Add your link on Django**

```bash
nano site/settings/settings.py
```

Add your domain or IP in `ALLOWED_HOSTS=[Here]`.

**6️⃣ Set up API key**

```bash
nano .env
```

.env content  
```text
API_KEY=*Your secure API Key*
```

---

## 🏁 Running the Services

**Django (Redirector)**

```bash
python manage.py runserver 0.0.0.0:80
```

➡️ Django is now available at `http://<your domain or IP>:80`

---

## 🛠️ API Usage

**Create a short URL**

```http
POST /api/shorten/
Content-Type: application/json

{
    "url": "https://example.com/very/long/and/boring/url"
}
```

**Response:**

```json
{
    "short_url": "http://<your url>/40afd8f1"
}
```

**List all URLs**

```http
GET /api/urls/
```

**Delete a URL**

```http
DELETE /api/url/<id>/delete
```

**Response:**

```json
{
    "result": "success"
}
```

**Update a URL**

```http
PUT /api/url/<id>
```

Content:
```json
{
    "short_url": "url"
}
```

**Redirection**
Visit the short URL in your browser:

```text
http://127.0.0.1/40afd8f1 -> redirects to the original URL
```

**Want to see a redirection ?**  
[https://url.zyrr.fr/sflkdin](https://url.zyrr.fr/sflkdin) is redirecting to [https://www.linkedin.com/company/scanfleet-tech](https://www.linkedin.com/company/scanfleet-tech) (Not working currently)

---

## 🤝 Contribution

We ❤️ contributions! Here's how you can help:

1. Fork the repository 🍴
2. Create your features / corrections 🌟
3. Commit your changes:  
``git commit -m "My super feature"`` ✅  
4. Push to your repository:  
``git push`` 🚀  
5. Open a [Pull Request](https://github.com/Guillaume0001/url-shortener/pulls) ✨  

Please make sure your code is **PEP8 compliant** and well-documented. 📝

---

## 🐛 Issues

Found a bug or have a feature request?  

- Open a new issue here: [GitHub Issues](https://github.com/Guillaume0001/url-shortener/issues) 🔧  
- Provide a **clear description**, steps to reproduce, and expected behavior.  

We'll review and respond as quickly as possible! ⏱️

---

## 📋 TODO

- [x] Add user authentication for API Access 🔐  
- [ ] Implement custom short URL slugs 🏷️  
- [ ] Add a dashboard to manage URLs 📊  
- [ ] Add analytics 📈  
- [ ] Dockerize the system 🐳  
- [ ] Add unit and integration tests ✅  
- [ ] Improve error pages for invalid short URLs 💥  

---

## 📝 License

This project is under MIT License.  
&copy; Guillaume MALEYRAT - 2026