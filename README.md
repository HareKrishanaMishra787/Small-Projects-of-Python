# Small-Projects-of-Python
# 🎯 Flask Number Guessing Game(Project 1)

Welcome to the **Flask Number Guessing Game** – a fun and interactive web app built with Python and Flask! Guess a number between **0 and 9**, and let the server tell you if you're right — with fun visuals!

## 🚀 How It Works

- The server picks a **random number** between 0 and 9.
- You try to guess the number by entering it in the URL:  
  `http://127.0.0.1:5000/your_number`
- You'll get a response:
  - ✅ **Correct guess** – You win! 🎉
  - 🔼 **Too high** – Try again!
  - 🔽 **Too low** – Try again!

## 🧰 Tech Stack

- **Python 3**
- **Flask**
- **Random**
- Fun **GIFs** to keep it playful!

## 🛠️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install Flask (if not already installed):
   ```bash
   pip install flask
   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. Open your browser and go to:  
   `http://127.0.0.1:5000`
      ```

# 🎤 Kanye Says... – Quote Generator App(Project 2)

This fun little Python app displays random Kanye West quotes in a stylish UI using **Tkinter**. Every time you click the Kanye face button, it fetches a new quote from the [Kanye REST API](https://api.kanye.rest) and displays it in a speech bubble.

## 🖼️ Features

- 🔁 Random Kanye quotes with every click
- 🎨 Beautiful UI with background and button images
- 🐍 Built with Python and Tkinter
- 🔗 Uses the Kanye REST API

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install requirements:**
   ```bash
   pip install requests
   ```

3. **Make sure the image files are in the same directory:**
   - `background.png`
   - `kanye.png`

4. **Run the app:**
   ```bash
   python main.py
   ```

## 🧠 Screenshot
<img src = 'https://github.com/user-attachments/assets/777b40e4-f6a8-45e1-9e61-967e5b458fae' width = "300">



💡 *Click the button and get inspired... Kanye style!*

# 🚀 ISS Overhead Notifier (Project 3)

A simple Python script that notifies you via email when the **International Space Station (ISS)** is flying above your location **at night**! 🌌✨

---

## 📋 Features
- Checks if the ISS is currently overhead (+/- 5 degrees of your location).
- Ensures it's nighttime at your location before sending a notification.
- Sends you an **email alert** to look up and spot the ISS! 📬👀

---

## 🛠️ Built With
- Python 🐍
- [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)
- SMTP (for sending emails)

---

## 🚀 How it Works
1. Fetches real-time ISS coordinates.
2. Compares them to your location.
3. Checks if it’s dark outside.
4. If both true ➔ sends an email notification!

---

## 📦 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/iss-overhead-notifier.git
   cd iss-overhead-notifier

   ```
# 🌍 Miles to Kilometers Converter(Project 4)

A simple and intuitive GUI application built with Python's Tkinter that converts miles into kilometers with just one click.

---

## 🛠 Features

- 🧮 Converts miles to kilometers accurately.
- 🪟 Minimal and user-friendly graphical interface.
- 🖱️ Single-click conversion using a button.
- 🔄 Real-time input and output display.

---

## 📸 Screenshot
![miles](https://github.com/user-attachments/assets/dd4d4508-d0cf-45ec-b351-8992e2429f00)



---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have Python installed. You can download it from:

🔗 https://www.python.org/downloads/

### 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/miles-to-km-converter.git
cd miles-to-km-converter
```

# 🎨 Dot Painting Generator(Project 5)

A vibrant, grid-style dot painting made with Python's `turtle` module—perfect for fans of generative art and Damien Hirst-inspired visuals.

---

## 🖼️ Project Overview

This Python project creates a beautiful 10x10 grid of randomly colored dots, inspired by the works of Damien Hirst. It uses a pre-defined color palette and places dots with precise spacing using the `turtle` graphics library.

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Install required modules (if not already available):
   ```bash
   pip install colorgram.py

# 📊 Pixela Coding Tracker(Project 6)

Track your daily coding hours in a fun and visual way using [Pixela](https://pixe.la)!  
This Python script lets you create a user account, build a graph, and update or delete your coding activity easily through Pixela’s API.

## 🚀 Features
- Create a Pixela user account and graph
- Add your daily coding hours
- Update past records
- Delete any record if needed
- See your progress visually on your personal Pixela graph!

## 🛠️ Tech Stack
- Python 3
- `requests` library
- Pixela API

## 📋 Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-link>
cd <repository-folder>
```

### 2. Install dependencies
```bash
pip install requests
```

### 3. Run the script
```bash
python main.py
```

### 4. Follow the prompts
- Enter how many hours you coded today.
- Your data will be added to your Pixela graph!

## 🔗 Your Graph Link
After setup, view your graph here:  
👉 `https://pixe.la/v1/users/<your-username>/graphs/<your-graph-id>.html`

_(Example: `https://pixe.la/v1/users/krishana/graphs/graph1.html`)_

## 🧹 Future Improvements
- Add authentication through environment variables for better security
- Schedule daily reminders to update the graph
- Build a GUI version

---


# Greeting Card Website - Hare Krishna Mishra(Project 7)

A simple portfolio website built with **Flask** and **HTML/CSS**.

## Project Structure
- `server.py`: Flask server file
- `templates/index.html`: Main HTML page
- `static/`: CSS, JS, and image files

## How to Run

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install flask
python server.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## Technologies Used
- Python Flask
- HTML5 & CSS3
- JavaScript

# 🧠 NATO Phonetic Alphabet Translator 🔤(Project 8)

A simple Python program that converts any input word into its NATO phonetic alphabet equivalent using a CSV file as a dictionary. Great for learning, communication clarity, or just having fun with code words!

## 🚀 Features

- Converts each letter of a word into its corresponding NATO phonetic alphabet code.
- Handles invalid characters gracefully.
- Easy to use and beginner-friendly.
- Lightweight and fast — built with just Python and Pandas.

## 📂 Project Structure

```
├── main.py                      # Main script for running the translator
├── nato_phonetic_alphabet.csv  # CSV file containing the phonetic alphabet
├── .gitignore                  # Git ignored files setup
└── .idea/                      # Project settings (for JetBrains IDE users)
```

## 📌 Usage

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Enter any word when prompted, and see the phonetic code output!

## 📝 Example

```
Enter the word: chat
['Charlie', 'Hotel', 'Alpha', 'Tango']
```

## ⚠️ Notes

- Only alphabetical characters are accepted. The program will prompt again if invalid input is detected.
- You can customize the CSV file to include other code words or phonetic systems.

## ❤️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.



# 📬 Saturday Motivation Mailer(Project 9)

This Python project sends a random motivational quote every **Saturday** to your email inbox to help kick-start the weekend with positivity and inspiration.

## 💡 Features

- 📆 Automatically checks if it's Saturday
- ✉️ Sends a motivational quote via email using Gmail SMTP
- 📜 Quotes are randomly picked from a text file (`quotes.txt`)

## 🛠️ How It Works

1. Checks the current day of the week.
2. If it's Saturday, it reads a random quote from `quotes.txt`.
3. Sends that quote to your email using Gmail's SMTP server.

## 🧾 Files

- `main.py`: Main Python script that automates the email sending.
- `quotes.txt`: Collection of motivational quotes.

## 🧪 Prerequisites

- Python 3.x
- An active Gmail account
- Enable **"Less secure app access"** or set up an **App Password** for your Gmail account

## 🚀 Usage

```bash
python main.py
```

Make sure to update these in `main.py`:
```python
my_email = "your_email@gmail.com"
password = "your_app_password"
to_addrs = "recipient_email@gmail.com"
```

## ⚠️ Disclaimer

This script uses plaintext credentials for demo purposes. Use environment variables or a `.env` file for better security in production.

## 📃 License

This project is licensed under the MIT License.


Happy coding! 🧑‍💻✨

# 🍅 Pomodoro Timer(Project 10)

A simple and beautiful **Pomodoro Timer** built with Python using Tkinter GUI. This app helps boost productivity by breaking work into intervals — traditionally 25 minutes of focused work followed by short breaks.

![Pomodoro Timer](tomato.png)

## 🕒 Features

- 25-minute work intervals (customizable)
- 5-minute short breaks
- 20-minute long break after 4 work sessions
- Visual check marks to track progress
- Playful tomato-themed UI 🌿

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Clone the repo or download the files.
3. Place the `tomato.png` in the same directory as `main.py`.
4. Run the app:

```bash
python main.py

```


Created by **Hare Krishna Mishra**


Made with ❤️ using Python and Pixela API!

      
