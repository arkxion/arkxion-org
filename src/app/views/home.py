from flask import Blueprint, render_template, redirect, url_for

# Define the Blueprint
home_bp = Blueprint("home", __name__, url_prefix="/<lang>")

# Research paper data
RESEARCH_PAPERS = [
    {
        "title": "English (Original)",
        "subtitle": "",
        "pdf_link": "https://zenodo.org/records/14760823",
    },
    {
        "title": "Japanese",
        "subtitle": "Translated by Hayate Esaki",
        "pdf_link": "/static/pdf/research-papers/arkxion_poai_whitepaper_ja_20250202_v1.pdf",
    },
]


@home_bp.route("/")
def home(lang):
    """
    Homepage route.
    Retrieves the language code from the <lang> part of the URL.
    """
    if lang not in ["en", "ja"]:
        return redirect(
            url_for("home.home", lang="en")
        )  # Redirect to default language if invalid
    return render_template("home/index.html", papers=RESEARCH_PAPERS, lang=lang)
