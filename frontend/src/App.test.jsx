import { render, screen, fireEvent, waitFor } from '@testing-library/react'
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

  it('sends teach requests', async () => {
    render(<App />)
    fireEvent.change(screen.getAllByPlaceholderText(/trigger/i)[0], {
      target: { value: 'ping' }
    })
    fireEvent.change(screen.getAllByPlaceholderText(/response/i)[0], {
      target: { value: 'pong' }
    })
    fireEvent.click(screen.getAllByRole('button', { name: /teach/i })[0])
    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith(
        '/api/teach',
        expect.objectContaining({
          method: 'POST',
          body: JSON.stringify({ trigger: 'ping', response: 'pong' })
        })
      )
    })
  })
})
