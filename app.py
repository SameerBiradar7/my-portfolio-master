from flask import Flask, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

# Updated portfolio projects from HTML
projects = [
    {
        "title": "Blood and Donor Management",
        "description": "A web app that helps manage and search for blood donors based on blood group and area. Focused on data handling and efficient search operations.",
        "link": "https://github.com/SameerBiradar7"
    },
    {
        "title": "Swiggy Clone",
        "description": "A MERN-stack based replica of the Swiggy app featuring core functionalities and modern UI/UX. Emphasis on responsive layout and dynamic content.",
        "link": "https://github.com/SameerBiradar7"
    },
    {
        "title": "College Management App",
        "description": "An Android application facilitating student-teacher interactions, course updates, and information sharing. Focused on mobile-first design and seamless usability.",
        "link": "https://github.com/SameerBiradar7"
    }
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects, now=datetime.now)

@app.route("/download_resume")
def download_resume():
    return send_from_directory(directory=os.path.abspath("."), path="Sameer_mca-Resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)