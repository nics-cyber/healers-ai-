from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample healing techniques data
healing_techniques = {
    "fever": [
        "Drink Tulsi (Holy Basil) tea to reduce fever naturally.",
        "Apply sandalwood paste on the forehead for cooling relief.",
        "Use coriander seed water to detoxify the body.",
        "Recite the Mahamrityunjaya mantra for healing vibrations."
    ],
    "pain": [
        "Massage with warm sesame oil infused with turmeric.",
        "Perform Pranayama (breath control) to release energy blockages.",
        "Apply a paste of dry ginger and water to sore areas.",
        "Chant 'Om' to reduce stress-related pain."
    ],
    "stress": [
        "Practice meditation and listen to Vedic chants.",
        "Burn frankincense and sandalwood for relaxation.",
        "Do Shavasana (corpse pose) for deep relaxation.",
        "Use Ashwagandha for stress and anxiety relief."
    ]
}

@app.route("/heal", methods=["POST"])
def heal():
    data = request.json
    ailment = data.get("ailment", "").lower()
    
    if ailment in healing_techniques:
        remedy = random.choice(healing_techniques[ailment])
        return jsonify({"remedy": remedy})
    else:
        return jsonify({"error": "No remedy found for the given ailment."})

if __name__ == "__main__":
    app.run(debug=True)
