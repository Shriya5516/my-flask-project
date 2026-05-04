// HerRoute — small JS helpers
document.addEventListener("DOMContentLoaded", () => {
    // Auto-dismiss flash messages
    document.querySelectorAll(".flash").forEach(el => {
        setTimeout(() => {
            el.style.transition = "opacity .4s ease";
            el.style.opacity = 0;
            setTimeout(() => el.remove(), 400);
        }, 4500);
    });

    // SOS button
    const sos = document.getElementById("sos-btn");
    if (sos) {
        sos.addEventListener("click", async () => {
            sos.disabled = true;
            sos.textContent = "Sending…";
            try {
                const r = await fetch("/api/sos", { method: "POST" });
                const data = await r.json();
                alert(data.message + (data.contacts && data.contacts.length
                    ? "\n\nNotified: " + data.contacts.join(", ")
                    : ""));
            } catch (e) {
                alert("Could not send SOS. Please call 112 immediately.");
            } finally {
                sos.disabled = false;
                sos.textContent = "Send SOS";
            }
        });
    }

    // Share live location demo
    const share = document.getElementById("share-loc");
    if (share) {
        share.addEventListener("click", () => {
            if (!navigator.geolocation) {
                alert("Geolocation is not supported in this browser.");
                return;
            }
            share.disabled = true;
            share.textContent = "Locating…";
            navigator.geolocation.getCurrentPosition(
                (pos) => {
                    const link = `https://maps.google.com/?q=${pos.coords.latitude},${pos.coords.longitude}`;
                    prompt("Copy & share this live-location link with your contacts:", link);
                    share.disabled = false;
                    share.textContent = "Share Live Location";
                },
                () => {
                    alert("Could not access your location. Please allow location permission.");
                    share.disabled = false;
                    share.textContent = "Share Live Location";
                }
            );
        });
    }
});
