# Simple-Chat-Bot
** 🤖 A Simple Self-Learning Chat Bot**

This project is a **rule-based chatbot** built using Python that can **learn from user interactions**. Unlike static chatbots, this bot dynamically updates its knowledge base by storing new responses in a JSON file.

---

## 🚀 Key Features

- 💬 Interactive command-line chatbot
- 🧠 Self-learning capability using JSON storage
- 📁 Persistent knowledge base (`knowledge_base.json`)
- 🔄 Dynamically updates responses during runtime
- ⚡ Lightweight and beginner-friendly

---

## 🧑‍💻 Tech Stack

- **Language:** Python
- **Libraries Used:**
  - `json` (for data storage)
  - `os` (for file handling)

---

## 🧠 How It Works

The chatbot follows a **simple learning loop**:

1. User enters a message
2. Bot checks the message in `knowledge_base.json`
3. If found → returns stored response
4. If not found:
   - Bot asks the user for the correct response
   - Saves it into the knowledge base
5. Future queries will use the learned response

This makes the bot **adaptive over time**.

---

## 📂 Project Structure
 
