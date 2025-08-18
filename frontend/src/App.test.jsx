import { render, screen } from '@testing-library/react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import App from './App'

describe('App', () => {
  beforeEach(() => {
    global.fetch = vi.fn().mockResolvedValue({ json: async () => [] })
  })

  it('renders send button', () => {
    render(<App />)
    expect(screen.getByText(/send/i)).toBeTruthy()
  })

  it('loads history on mount', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      json: async () => [{ role: 'user', content: 'hi' }, { role: 'bot', content: 'hello' }]
    })
    render(<App />)
    const items = await screen.findAllByRole('listitem')
    expect(items[0].textContent).toContain('user')
    expect(items[0].textContent).toContain('hi')
    expect(items[1].textContent).toContain('bot')
    expect(items[1].textContent).toContain('hello')
  })
})
