// src/components/Chat/ChatWindow.tsx
import React, { useState } from 'react';
import { useChat } from '../../hooks/useChat';
import '../../styles/globals.css';

export default function ChatWindow() {
  const userId = 'demo-user-1';
  const { messages, sendMessage } = useChat(userId);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim()) return;
    sendMessage(input);
    setInput('');
  };

  return (
    <div className="chat-container">
      <h2>🤖 Welcome to the Intelligent Chatbot</h2>
      <div className="chat-messages">
        {messages.length === 0 && (
          <p style={{ textAlign: 'center', color: '#aaa' }}>
            Start the conversation by typing below...
          </p>
        )}
        {messages.map((msg, index) => (
          <div key={index} className={`chat-message ${msg.role}`}>
            <strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <div className="chat-input-wrapper">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ flexGrow: 1, padding: '10px', borderRadius: '5px', border: '1px solid #ddd' }}
        />
        <button onClick={handleSend} style={{ padding: '10px 20px' ,backgroundColor: '#0a67b9', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer'}}>Send</button>
      </div>
    </div>
  );
}
