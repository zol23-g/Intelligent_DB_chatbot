// src/hooks/useChat.ts
import { useState } from 'react';
import { sendChatMessage } from './useApi';

export function useChat(userId: string) {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([]);

  const sendMessage = async (message: string) => {
    setMessages(prev => [...prev, { role: "user", content: message }]);
    const res = await sendChatMessage(userId, message);
    setMessages(prev => [...prev, { role: "assistant", content: res.reply }]);
  };

  return { messages, sendMessage };
}
