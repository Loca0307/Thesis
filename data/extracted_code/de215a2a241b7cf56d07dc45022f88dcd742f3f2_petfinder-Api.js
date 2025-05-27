

const getAuthToken = async () => {
    const response = await fetch("https://api.petfinder.com/v2/oauth2/token", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            grant_type: "client_credentials",
            client_id: import.meta.env.VITE_PETFINDER_CLIENT_ID,
            client_secret: import.meta.env.VITE_PETFINDER_CLIENT_SECRET,
        }),
    });

    const data = await response.json();
    return data.access_token;
};

async function GetSighthounds() { // Default location = UK
    const token = await getAuthToken();

    const sighthoundBreeds = [
        "Greyhound",
        "Whippet",
        "Saluki",
        "Afghan Hound",
        "Borzoi",
        "Ibizan Hound",
        "Italian Greyhound",
        "Scottish Deerhound",
        "Sloughi",
    ];

    const response = await fetch(
        `https://api.petfinder.com/v2/animals?type=dog&breed=${sighthoundBreeds.join(",")}`,
        {
            method: "GET",
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        }
    );

    const data = await response.json();
    console.log(data)
    console.log(data.animals)
    return data.animals; // Return only the list of animals
}

// GetSighthounds();

export default GetSighthounds