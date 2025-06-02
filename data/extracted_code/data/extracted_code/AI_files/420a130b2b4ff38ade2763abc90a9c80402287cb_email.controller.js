        const fromUserId = req.id;
        const { to, subject, message } = req.body;

        if (!to || !subject || !message) return res.status(400).json({
            message: "All the information is required",
            success: false,
        });

        const toUser = await User.findOne({ email: to });
        if (!toUser) return res.status(404).json({
            message: "Recipient user not found",
            success: false,
        });

        const email = await Email.create({
            to: toUser.email,
            subject,
            message,
            userId: fromUserId
        });

        // Save the email for the recipient user as well
        await Email.create({
            to: toUser.email,
            subject,
            message,
            userId: toUser._id
        });

        return res.status(201).json({
            email,
            message: "Message sent successfully",
            success: true,
        });