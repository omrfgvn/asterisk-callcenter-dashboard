# Asterisk Call Center Dashboard

This project simulates a VoIP-based call center using **Asterisk PBX** and a real-time **HTML dashboard**. It allows users to monitor the availability of call center agents assigned to **Sales** and **Technical Support** departments.

---

## 🎯 Project Purpose

The goal is to create a realistic call center environment where SIP-based agents can receive and answer calls, and users can view real-time agent availability through a web dashboard. The system is designed to demonstrate how a basic call center can be managed using open-source tools.

---

## 🧪 Technologies Used

- **Asterisk PBX** – Handles SIP registration, call routing, and queues  
- **MicroSIP** – Lightweight SIP softphone for call agents  
- **Python** – Backend logic and connection to Asterisk via AMI  
- **HTML / CSS / JavaScript** – Responsive and dynamic frontend  
- **AJAX / WebSocket (planned)** – For live dashboard updates  
- **Asterisk AMI** – Asterisk Manager Interface used for real-time system information

---

## 📊 Features

- 📞 Realistic simulation of a multi-department call center  
- 👥 Agent status tracking: Available, In Call, Busy, Offline  
- 🌐 Web-based live dashboard showing agent availability  
- 🧩 Simple integration with existing Asterisk installations  
- 🧭 Clear separation between **Sales** and **Technical Support** teams

---

## 🧱 Project Structure

```
asterisk-callcenter-dashboard/
├── static/
│   └── style.css
├── templates/
│   └── dashboard.html
├── app.py
├── utils/
│   └── ami_handler.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. **Set up Asterisk** on a Linux server (Debian/Ubuntu recommended).
2. Configure your Asterisk system:
   - Add users in `sip.conf`
   - Set dial plans in `extensions.conf`
   - Define queues in `queues.conf`
3. **Register MicroSIP clients** with the SIP accounts you've created.
4. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/asterisk-callcenter-dashboard.git
   cd asterisk-callcenter-dashboard
   ```

5. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the dashboard application:

   ```bash
   python app.py
   ```

7. Access the dashboard at:

   ```
   http://localhost:5000
   ```

   Or using your server’s IP address.

---

## 🔮 Future Enhancements

- ✅ Real-time updates using WebSocket
- 📈 Call metrics per agent (total calls, durations, missed calls)
- 🧑‍💼 Role-based admin panel
- 📊 Visual graphs for call volume over time
- 🔔 Slack/Telegram alert integration
- 💬 CRM system or support ticket integration

---

## 🧪 Example Use Case

Imagine a company with two departments: **Sales** and **Technical Support**. Each department has its own call queue. This dashboard allows supervisors to monitor which agents are available, how many are busy, and helps improve response times by visualizing bottlenecks.

---

## 🤝 Contributing

We welcome contributions from the open source community! To contribute:

1. Fork the project 🍴  
2. Create a feature branch (`feature/your-feature`)  
3. Commit your changes  
4. Open a pull request ✔️  

---

## 📜 License

MIT License © 2025  
Developed by [Mehmet Burak KARABULUT](https://github.com/mbk2103) & [Ömer Faruk GÜVEN](https://github.com/omrfgvn)

---

## 📬 Contact

For issues, suggestions or improvements, please open an [issue](https://github.com/omrfgvn/asterisk-callcenter-dashboard/issues) or contact us via GitHub.

---
