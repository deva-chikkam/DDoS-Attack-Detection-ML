# Detection of Application-Layer DDoS Attacks using Machine Learning

## 📌 Project Overview
An end-to-end Machine Learning web application designed to detect and mitigate application-layer Distributed Denial of Service (DDoS) attacks. This project analyzes network traffic features to accurately classify malicious HTTP traffic patterns produced by common toolkits.

## 🚀 Key Achievements
* Engineered an Ensemble Stacking Classifier using Python, achieving 99.9% accuracy in detecting malicious HTTP traffic patterns.
* Analyzed NSL-KDD and NBOT-IoT datasets to identify attack signatures produced by common toolkits like Slowloris and GoldenEye.
* Developed a Flask-based dashboard for real-time traffic classification and secure user authentication using SQLite.

## 🛠️ Deployment & Troubleshooting 
During the deployment of this application, several real-world MLOps and infrastructure challenges were successfully resolved:
* **Environment Modernization:** Upgraded legacy `scikit-learn` `.sav` models to be fully compatible with modern Python 3.12 architecture by successfully debugging syntax errors and retraining Voting and Stacking classifiers.
* **Backend Data Parsing:** Resolved front-end `UnboundLocalError` crashes by rewriting the backend routing logic to dynamically strip array formatting and safely translate raw machine learning outputs into user-friendly text (e.g., mapping `9` to `Neptune (DoS)`).
* **Authentication Infrastructure:** Maintained complete SQLite3 database authentication logic while bypassing deprecated third-party SMTP server protocols for local development testing.

## 🔮 Future Enhancements
* **Real-Time Data Pipelines:** Utilizing streaming analytics tools like Apache Kafka and Apache Flink to monitor live threats as they unfold.
* **SIEM Integration:** Combining the system with Security Information and Event Management (SIEM) tools to provide real-time alerts and trigger automated firewall responses.
