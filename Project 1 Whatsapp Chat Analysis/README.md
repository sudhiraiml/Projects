## 📊 WhatsApp Chat Analyzer

An interactive dashboard to analyze WhatsApp chat history using Python and Streamlit. Upload your exported `.txt` chat file and get insights like message frequency, user contribution, emoji usage, word trends, and more!

---

## 🚀 Features

- 🔍 **Top-level Stats**: Total messages, word count, media shared, and links shared
- 👥 **Most Active Users**: User-wise message breakdown
- 📝 **Most Common Words**: Excludes stop words for clarity
- 😂 **Emoji Analysis**: Count of most-used emojis
- 📆 **Timelines**: Monthly and daily message distribution
- 📊 **Activity Heatmap**: See when the chat is most active during the week
- 🧠 **Stop Word Removal**: Handles Hinglish stopwords for better analysis

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- WordCloud
- URLEXtract
- Emoji

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
````

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the browser at `http://localhost:8501` if it doesn't open automatically.

---

## 📁 Project Structure

```
.
├── app.py                  # Main Streamlit app
├── helper.py               # All analysis and utility functions
├── preprocessor.py         # Raw chat data parser and formatter
├── stop_hinglish.txt       # List of stop words
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📂 How to Export WhatsApp Chat

1. Open any WhatsApp chat
2. Click on the three dots > More > Export Chat
3. Choose **Without Media**
4. Send the `.txt` file to your computer
5. Upload it into the app

---

## 📌 Real-Life Use Cases

* Team performance tracking in WhatsApp groups
* Analyzing personal or family chat behavior
* Understanding digital communication trends
* Fun analytics for group chats (top emoji user, etc.)

---

## 🙋‍♂️ Author

Made with ❤️ by \[Your Name]
Feel free to fork, star, and contribute!

---

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

