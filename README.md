# 📞 Asterisk Call Center Dashboard

This project simulates a VoIP-based call center environment using **Asterisk PBX** and a real-time **HTML dashboard**. It allows monitoring the online/offline status of agents assigned to **Sales** and **Technical Support** departments.

---

## 🎯 Project Purpose

To build an open-source, easy-to-deploy, realistic call center simulation where SIP-based agents can receive calls and their availability can be tracked via a live web dashboard.

---

## ⚙️ Technologies Used

- **Asterisk PBX** – Manages SIP registrations, calls, and queues  
- **MicroSIP** – Lightweight SIP softphone for agents  
- **Python (Flask)** – Backend and API server  
- **HTML / CSS / JavaScript** – Frontend UI  
- **Socket polling** – Refreshes data every 3 seconds  
- **subprocess** – Communicates with Asterisk CLI

---

## 🔍 Features

- 🔄 Real-time agent and customer status monitoring  
- 👥 Separation between Sales and Technical Support departments  
- 💡 Simple and intuitive status indicators: ONLINE / OFFLINE  
- 🌐 Accessible from any web browser

---

## 📁 Project Structure

```text
asterisk-callcenter-dashboard/
├── templates/
│   └── index.html        # Main dashboard interface
├── app.py                # Flask app
├── checkAsterisk.py      # Handles CLI interaction with Asterisk
├── sip.conf              # SIP user configuration
├── extensions.conf       # Dial plan definitions
├── queues.conf           # Queue configurations
├── LICENSE
└── README.md
```
---

## 🚀 Installation

1. Install and configure **Asterisk PBX** (Debian/Ubuntu recommended).
2. Set up SIP users, extensions, and queues using:
   - `sip.conf`
   - `extensions.conf`
   - `queues.conf`
3. Register your SIP users with a client like **MicroSIP**.
4. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/asterisk-callcenter-dashboard.git
   cd asterisk-callcenter-dashboard
   ```
Install Python dependencies:

```bash
pip install flask
```
Start the Flask app:

   ```bash
   python app.py
   ```
Open the dashboard in your browser:
   ```bash   
   http://localhost:5000
   or
   http://<your-server-ip>:5000
   ```
🔮 Future Enhancements
📡 Real-time updates via WebSocket

📈 Per-agent call metrics (calls, duration, missed)

🔐 Admin panel with authentication

📊 Visual charts for call analytics

🛎️ Integration with Slack/Telegram for alerts

💬 CRM or ticket system integration

👨‍💻 Developers:

Ömer Faruk GÜVEN

Mehmet Burak KARABULUT

📬 Contact
For issues, suggestions, or contributions, please open an issue or contact us on GitHub.

📝 License
MIT License © 2025

---

Let me know if you’d like to auto-generate a GitHub Pages demo site or add a screenshot to the README.
