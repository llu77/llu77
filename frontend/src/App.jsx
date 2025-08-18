import { useState } from 'react'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')

  const sendMessage = async () => {
    if (!input.trim()) return
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    })
    const data = await res.json()
    setMessages([
      ...messages,
      { role: 'user', text: input },
      { role: 'bot', text: data.reply }
    ])
    setInput('')
  }

  return (
    <div>
      <ul>
        {messages.map((m, i) => (
          <li key={i}>
            <b>{m.role}:</b> {m.text}
          </li>
        ))}
      </ul>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  )
}

export default App
