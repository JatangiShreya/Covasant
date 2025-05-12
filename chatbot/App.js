import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  
  const predefinedAnswers = {
    "hello":"Hii Welcome to the conversation ..How can I help ",
    "What is Python?": "Python is a popular high-level programming language known for its simplicity and readability. It is used for web development, data analysis, artificial intelligence, and more.",
    "What is JavaScript?": "JavaScript is a programming language that is commonly used to create interactive effects within web browsers. It is essential for web development.",
    "What is React?": "React is a JavaScript library for building user interfaces. It allows developers to build single-page applications with a component-based architecture.",
    "What is 2+2?": "2 + 2 is 4.",
    "What is the weather like today?": "The weather is sunny with a slight chance of rain.",
    "Tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "What is your name?": "I am ChattyBot, your friendly assistant.",
    "Who created you?": "I was created by a talented team of developers.",
  };


  const getBotResponse = (userMessage) => {
    const response = predefinedAnswers[userMessage.trim()];
    return response || "Sorry, I don't understand that question.";
  };

  const sendMessage = async () => {
    if (!message.trim()) return;

  
    const userMessage = { sender: 'You', text: message };
    setChatHistory((prev) => [...prev, userMessage]);

    
    const botReplyText = getBotResponse(message);

 
    const botReply = { sender: 'Bot', text: botReplyText };
    setChatHistory((prev) => [...prev, botReply]);

    
    setMessage('');
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        <div className="chat-header">ChattyBot 🤖</div>
        <div className="messages">
          {chatHistory.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender === 'You' ? 'user-message' : 'bot-message'}`}
            >
              <span>{msg.text}</span>
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask me anything..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
