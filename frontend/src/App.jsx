import { useState, useEffect } from 'react'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [trigger, setTrigger] = useState('')
  const [response, setResponse] = useState('')

  useEffect(() => {
    const loadHistory = async () => {
      const res = await fetch('/api/history')
      const data = await res.json()
      setMessages(data.map(m => ({ role: m.role, text: m.content })))
    }
    loadHistory()
  }, [])

  const sendMessage = async () => {
    if (!input.trim()) return
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input })
    })
    const data = await res.json()
    setMessages(prev => [
      ...prev,
      { role: 'user', text: input },
      { role: 'bot', text: data.reply }
    ])
    setInput('')
  }

  const teach = async () => {
    if (!trigger.trim() || !response.trim()) return
    await fetch('/api/teach', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trigger, response })
    })
    setTrigger('')
    setResponse('')
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
      <div>
        <h3>Teach the bot</h3>
        <input
          placeholder="Trigger"
          value={trigger}
          onChange={(e) => setTrigger(e.target.value)}
        />
        <input
          placeholder="Response"
          value={response}
          onChange={(e) => setResponse(e.target.value)}
        />
        <button onClick={teach}>Teach</button>
      </div>
    </div>
  )
}

export default App
