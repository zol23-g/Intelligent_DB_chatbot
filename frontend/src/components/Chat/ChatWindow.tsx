import React, { useState, useRef, useEffect } from 'react';
import { useChat } from '../../hooks/useChat';
import '../../styles/globals.css';

export default function ChatWindow() {
  const userId = 'demo-user-1';
  const { messages, sendMessage, loading } = useChat(userId);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  const handleSend = () => {
    if (!input.trim()) return;
    sendMessage(input);
    setInput('');
  };

  // Optional: Scroll to bottom on message send
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div
      className="chat-container"
      style={{
        maxWidth: '850px',
        height: '90vh',
        margin: '30px auto',
        backgroundColor: '#ffffff',
        padding: '30px',
        borderRadius: '12px',
        boxShadow: '0 4px 15px rgba(0, 0, 0, 0.08)',
        border: '1px solid #e0e0e0',
        display: 'flex',
        flexDirection: 'column',
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
      }}
    >
      <h2 style={{ textAlign: 'center', marginBottom: '20px', fontFamily: "'Poppins', sans-serif", fontSize: '24px', fontWeight: '600', color: '#333' }}>
        🤖 Intelligent DB Chatbot
      </h2>

      <div
        className="chat-messages"
        style={{
          flexGrow: 1,
          overflowY: 'auto',
          marginBottom: '20px',
          padding: '10px 15px',
          border: '1px solid #ddd',
          borderRadius: '8px',
          backgroundColor: '#f4f6f9',
          fontSize: '16px'
        }}
      >
        {loading ? (
          <p style={{ textAlign: 'center', color: '#aaa' }}>Loading previous messages...</p>
        ) : messages.length === 0 ? (
          <p style={{ textAlign: 'center', color: '#aaa' }}>
            Start the conversation by typing below...
          </p>
        ) : (
          messages.map((msg, index) => (
            <div
              key={index}
              style={{
                backgroundColor: msg.role === 'user' ? '#e3f2fd' : '#fff8e1',
                border: '1px solid #ccc',
                padding: '14px',
                borderRadius: '10px',
                margin: '10px 0',
                alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start',
                fontFamily:
                  msg.role === 'user'
                    ? "'Courier New', Courier, monospace"
                    : "'Georgia', serif"
              }}
            >
              <strong style={{ display: 'block', marginBottom: '5px', fontSize: '14px' }}>
                {msg.role === 'user' ? 'You' : 'Bot'}:
              </strong>
              {msg.content}
            </div>
          ))
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-wrapper" style={{ display: 'flex', gap: '10px' }}>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{
            flexGrow: 1,
            padding: '12px',
            borderRadius: '8px',
            border: '1px solid #ccc',
            fontSize: '16px',
            fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
          }}
        />
        <button
          onClick={handleSend}
          style={{
            padding: '12px 24px',
            backgroundColor: '#0a67b9',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            cursor: 'pointer',
            fontWeight: 'bold',
            fontSize: '16px'
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}
