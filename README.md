# Ancient Healing AI Dashboard

## 🌿 Overview
The **Ancient Healing AI Dashboard** is an intelligent system that provides traditional healing remedies based on ancient techniques from Hinduism, Ayurveda, Siddha medicine, Tibetan healing, and other spiritual practices. Users can input their ailments, and the AI suggests remedies such as herbal treatments, meditation techniques, mantras, and more.

## ✨ Features
- **AI-Powered Healing Recommendations**: Get remedies for ailments like fever, pain, and stress.
- **Ancient Healing Techniques**: Uses Ayurveda, Pranayama, Vedic mantras, and more.
- **Interactive Dashboard**: A simple and clean UI to interact with the AI.
- **JSON API Support**: Easily send requests and receive healing recommendations.
- **Flask-Powered Backend**: Lightweight and efficient Python web server.
- **Randomized Suggestions**: Different remedies each time you ask for help.

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Steps to Run
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/ancient-healing-ai.git
   cd ancient-healing-ai
   ```
2. **Install Dependencies:**
   ```bash
   pip install flask
   ```
3. **Run the Flask App:**
   ```bash
   python app.py
   ```
4. **Access the Dashboard:**
   - Open a browser and go to: `http://127.0.0.1:5000`

## 📡 API Usage
To request a healing recommendation via API:
```bash
curl -X POST http://127.0.0.1:5000/heal -H "Content-Type: application/json" -d '{"ailment": "fever"}'
```
Response Example:
```json
{
  "remedy": "Drink Tulsi (Holy Basil) tea to reduce fever naturally."
}
```

## 🎨 Future Enhancements
- Expand the database with more ailments and remedies.
- Add user authentication for personalized recommendations.
- Implement voice-assisted AI for interactive healing guidance.
- Create a mobile-friendly UI.

## 🤝 Contributing
Feel free to fork the repo and submit pull requests!

## 📜 License
This project is open-source under the MIT License.

