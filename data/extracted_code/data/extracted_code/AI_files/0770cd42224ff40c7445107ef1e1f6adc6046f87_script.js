    const time = `${hours}:${minutes} ${ampm}`;

    // Extracting and formatting day and date
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    const dayName = days[now.getDay()];
    const monthName = months[now.getMonth()];
    const day = now.getDate();
    const year = now.getFullYear();

    const date = `${dayName}, ${monthName} ${day}, ${year}`;

    document.getElementById("dateTime").innerText = `${time} - ${date}`;
}

displayDateTime();