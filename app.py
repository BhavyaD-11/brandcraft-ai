from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# put your NEW API key here (the one you regenerated)
client = OpenAI(
    api_key=""
)

@app.route("/", methods=["GET", "POST"])
def index():
    branding = ""

    if request.method == "POST":
        industry = request.form["industry"]
        tone = request.form["tone"]

        prompt = f"""
Create branding for a business.

Industry: {industry}
Brand Tone: {tone}

Generate:
1. Brand Name
2. Tagline
3. Short Brand Description
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        branding = response.choices[0].message.content

    return render_template("index.html", branding=branding)

if __name__ == "__main__":
    app.run(debug=True)
