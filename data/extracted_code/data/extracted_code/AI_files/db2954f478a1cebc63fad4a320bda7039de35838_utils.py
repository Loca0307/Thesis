    """
    Send a data message via Firebase Cloud Messaging (FCM).

    Args:
        token (str): The recipient's FCM device token.
        msg_id (str): The unique message ID.
        title (str): The title of the message.
        body (str): The body content of the message.

    Returns:
        str: The response from the Firebase messaging service.

    Raises:
        ImportError: If the Firebase Admin SDK is not installed.
    """