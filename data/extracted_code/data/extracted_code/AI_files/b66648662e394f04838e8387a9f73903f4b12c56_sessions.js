    const { role } = req.body;
    const allowedRoles = ['mentor', 'mentee'];
    if (!allowedRoles.includes(role)) {
      return res.status(400).json({ error: 'Invalid role. Allowed values are "mentor" or "mentee".' });
    }