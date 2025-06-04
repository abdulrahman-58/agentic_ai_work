# 🔀 Multi-Agent Assistant (OpenAI SDK + Gemini API)

A smart multi-agent assistant built using the `agents` and `chainlit` libraries. This system routes user queries to specialized agents (Web Developer, Mobile Developer, Marketing Agent) through a Manager Agent. The system uses **OpenAI SDK** to access **Gemini models** via a custom API endpoint.

---

## 🚀 Features

* **Multi-Agent Architecture**
  Includes specialized agents for:

  * 🧑‍💻 Web Development
  * 📱 Mobile App Development
  * 📢 Digital Marketing

* **Manager Agent**
  Analyzes user queries and routes them to the appropriate expert agent.

* **OpenAI SDK + Gemini API Integration**
  Uses `openai.AsyncOpenAI` client to connect to Google's Gemini API via custom `base_url`.

* **Chainlit Integration**
  Provides an interactive frontend chat interface using `chainlit`.

* **Domain-specific Handling**
  Each agent only responds to queries relevant to their field. If asked about something else, they politely decline.

---

## 🧠 How It Works

1. User sends a message.
2. The **Manager Agent** analyzes the query.
3. Based on content, the Manager chooses one of:

   * `Web Developer`
   * `Mobile Developer`
   * `Marketing Agent`
   * `None` (if the query doesn't match any category)
4. The selected agent responds accordingly.

---

## 🛠️ Tech Stack

| Component  | Description                                    |
| ---------- | ---------------------------------------------- |
| `agents`   | Multi-agent orchestration framework            |
| `openai`   | Used as SDK to call Gemini via custom endpoint |
| `chainlit` | Chat frontend for real-time interactions       |
| `dotenv`   | Loads the Gemini API key from `.env` file      |

---

## 📦 Installation

```bash
pip install chainlit agents openai python-dotenv
```

---

## 🔐 Environment Variables

Create a `.env` file in your root directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🧪 Running the App

Run the Chainlit app:

```bash
chainlit run app.py
```

Replace `app.py` with your script's filename.

---

## 💬 Sample Interaction

```txt
User: How do I create a navigation bar in React?
→ Manager: Assigning to Web Developer...
→ Web Developer: You can use Flexbox with React components...

User: How do I launch my Android app?
→ Manager: Assigning to Mobile Developer...
→ Mobile Developer: First, generate a signed APK, then upload it to the Play Console...

User: What's a good Instagram growth strategy?
→ Manager: Assigning to Marketing Agent...
→ Marketing Agent: Use consistent posting, hashtags, and community engagement...

User: Can you help with investment tips?
→ Manager: Sorry, our team can't handle this type of request.
```

---

## 📃 License

This project is released under the MIT License.

---
