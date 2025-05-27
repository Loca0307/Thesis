
    req.user = {
      userId: decoded.userId,
      role: decoded.role,
    };

    next();
  } catch (error) {
    logger.error("JWT verification failed", { error });
    return next(new UnauthorizedError("Invalid or expired token"));
  }