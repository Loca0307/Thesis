</div> *@
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notifications</title>
    @*Entire script by chatgpt*@
    <script>
        async function fetchNewNotifications() {
            try {
                const response = await fetch('/Notifications?handler=NewNotifications');
                if (response.ok) {
                    const newNotifications = await response.json();
                    if (newNotifications.length > 0) {
                        appendNotifications(newNotifications);
                    }
                }
            } catch (error) {
                console.error("Error fetching new notifications:", error);
            }
        }

        function appendNotifications(notifications) {
            const ul = document.getElementById('notifications-list');
            notifications.forEach(notification => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <p>
                        <span>
                            <a href="/${notification.authorName}">${notification.authorName}</a>
                            ${notification.tagNotification ? 'tagged you!' : 'chirped!'}
                        </span>
                    </p>
                    <p>${notification.cheepContent}</p>`;
                ul.appendChild(li);
            });
        }

        setInterval(fetchNewNotifications, 5000); // Check every 5 seconds
    </script>
</head>
<body>
    <ul id="notifications-list">
        @foreach (var notif in Model.notifications)
        {
            <li>
                <p>
                    <span>
                        <a href="/@notif.authorName">@notif.authorName</a>
                        @(notif.tagNotification ? "tagged you!" : "chirped!")
                    </span>
                </p>
                <p>@notif.cheepContent</p>
            </li>
        }
    </ul>
</body>
</html>
