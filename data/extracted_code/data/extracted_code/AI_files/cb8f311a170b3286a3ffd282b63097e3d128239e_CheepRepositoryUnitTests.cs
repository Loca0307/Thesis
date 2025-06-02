        _repository.CreateFollow(userEmail, authorEmail);
        try
        {
            _repository.CreateFollow(userEmail, authorEmail);
        }
        catch (Exception ex)
        {
            ex.GetBaseException();
        }