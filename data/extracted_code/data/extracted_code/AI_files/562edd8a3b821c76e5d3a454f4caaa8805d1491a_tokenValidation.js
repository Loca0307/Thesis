    const authHeader = req.header('Authorization');
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
        return res.status(401).json({ error: 'Authentication token missing or malformed' });
    }

    /*
    Prevent jwtPayload from being undefined
    Bug found by ChatGPT (https://chatgpt.com/share/67e01958-bc68-8011-8db0-16deafd5fd7b)
     */
    try {
        const payload = jwt.verify(token, secretKey);
        return payload;
    } catch (err) {
        return res.status(403).json({ error: 'Token is invalid' });