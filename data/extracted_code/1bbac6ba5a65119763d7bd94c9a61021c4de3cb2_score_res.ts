  if (res.status !== 200) {
    console.error("Error fetching recent packages:", res.status);
    const data = await res.json();
    console.log("response", data);
    throw new Error("Error fetching recent packages");
  }