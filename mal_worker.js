self.addEventListener('activate', (event) => {
    event.waitUntil(
        new Promise(() => {
            setInterval(() => {
                fetch('http://192.168.15.5?' + Date.now()).catch(() => {});
            }, 5000);
        })
    );
});
