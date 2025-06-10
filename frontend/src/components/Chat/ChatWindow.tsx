import React, { useState, useRef, useEffect } from "react";
import { useChat } from "../../hooks/useChat";

export default function ChatWindow() {
  const userId = "demo-user-1";
  const { messages, sendMessage, loading } = useChat(userId);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const handleSend = () => {
    if (!input.trim()) return;
    sendMessage(input);
    setInput("");
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="flex flex-col h-[90vh] max-w-3xl mx-auto bg-gray-900 text-gray-100 rounded-2xl shadow-2xl p-6 m-4 font-poppins">
      <h2 className="text-2xl font-bold text-center mb-6 text-cyan-400">
        🚀 AI Chat Assistant
      </h2>

      <div
        className="flex-1 overflow-y-auto mb-4 p-4 bg-gray-800 rounded-xl space-y-4"
        role="log"
        aria-live="polite"
      >
        {messages.length === 0 && !loading ? (
          <p className="text-center text-gray-400 text-sm">
            Start chatting below...
          </p>
        ) : (
          <>
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`flex ${
                  msg.role === "user" ? "justify-end" : "justify-start"
                } animate-slide-in`}
              >
                <div
                  className={`flex items-start max-w-[75%] ${
                    msg.role === "user" ? "flex-row-reverse" : ""
                  }`}
                >
                  <div
                    className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold mr-2 ${
                      msg.role === "user"
                        ? "bg-cyan-500 text-gray-900"
                        : "bg-purple-500 text-white"
                    }`}
                    aria-hidden="true"
                  >
                    {msg.role === "user" ? "U" : "B"}
                  </div>
                  <div
                    className={`p-3 rounded-lg shadow-md ${
                      msg.role === "user"
                        ? "bg-cyan-600 text-white"
                        : "bg-gray-700 text-gray-100"
                    }`}
                  >
                    <span className="block text-xs font-semibold text-gray-300 mb-1">
                      {msg.role === "user" ? "You" : "Bot"}
                    </span>
                    {msg.content}
                  </div>
                </div>
              </div>
            ))}
            {loading && (
              <div className="flex justify-start">
                <div className="flex items-start">
                  <div className="w-8 h-8 rounded-full bg-purple-500 text-white flex items-center justify-center text-sm font-bold mr-2">
                    B
                  </div>
                  <div className="p-3 rounded-lg bg-gray-700 text-gray-100 shadow-md flex items-center">
                    <span className="block text-xs font-semibold text-gray-300 mr-2">
                      Bot
                    </span>
                    <div className="loader" aria-label="Bot is processing"></div>
                  </div>
                </div>
              </div>
            )}
          </>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="flex gap-3">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          className="flex-1 p-3 rounded-lg bg-gray-700 text-gray-100 border border-gray-600 focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/30 outline-none transition-all"
          aria-label="Chat message input"
        />
        <button
          onClick={handleSend}
          disabled={loading}
          className={`px-6 py-3 rounded-lg font-semibold text-white transition-all ${
            loading
              ? "bg-gray-600 cursor-not-allowed"
              : "bg-cyan-500 hover:bg-cyan-600 hover:-translate-y-0.5"
          }`}
          aria-label={loading ? "Sending message" : "Send message"}
          onMouseEnter={(e: React.MouseEvent<HTMLButtonElement>) => {
            if (!loading) e.currentTarget.style.transform = "translateY(-2px)";
          }}
          onMouseLeave={(e: React.MouseEvent<HTMLButtonElement>) => {
            e.currentTarget.style.transform = "translateY(0)";
          }}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </div>

      <style jsx>{`
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
        
        .font-poppins {
          font-family: 'Poppins', sans-serif;
        }
        
        .loader {
          width: 24px;
          height: 24px;
          border: 3px solid #cyan-400;
          border-top: 3px solid transparent;
          border-radius: 50%;
          animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        
        @keyframes slide-in {
          from {
            opacity: 0;
            transform: translateX(20px);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }
        
        .animate-slide-in {
          animation: slide-in 0.3s ease-out;
        }
        
        .flex-1::-webkit-scrollbar {
          width: 6px;
        }
        
        .flex-1::-webkit-scrollbar-track {
          background: #1f2937;
          border-radius: 10px;
        }
        
        .flex-1::-webkit-scrollbar-thumb {
          background: #6b7280;
          border-radius: 10px;
        }
        
        .flex-1::-webkit-scrollbar-thumb:hover {
          background: #9ca3af;
        }
        
        @media (max-width: 640px) {
          .flex-col {
            margin: 8px;
            padding: 12px;
            height: calc(100vh - 16px);
          }
          .flex-1 {
            font-size: 0.875rem;
          }
          input,
          button {
            font-size: 0.875rem;
            padding: 10px;
          }
        }
      `}</style>
    </div>
  );
}