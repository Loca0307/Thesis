
  if (document.readyState === 'loading') {
    return new Promise((resolve) => {
      document.addEventListener('DOMContentLoaded', () => {
        setup().then(resolve)
      }, { once: true })
    })
  }

  try {
    await loadScript(widgetUrl)
    window.dispatchEvent(new Event('greenspark-setup'))
  } catch (error) {
    console.error('Greenspark Widget - Failed to load script:', error)
    setTimeout(() => setup(), 1000)
  }