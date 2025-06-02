  public UserDTO resultToDTO(ResultSet resultSet) throws SQLException {
    String dbsUsername = resultSet.getString("username");
    String dbsEmail = resultSet.getString("email");
    String dbsPassword = resultSet.getString("password_hash");
    boolean dbsIsAdmin = (resultSet.getByte("isAdmin")) == 1;
    int balance = resultSet.getInt("balance");

    return new UserDTO(dbsUsername, dbsEmail, dbsPassword, dbsIsAdmin, balance);
  }

  public User resultToUser(ResultSet resultSet) throws SQLException {
    String dbsUsername = resultSet.getString("username");
    String dbsEmail = resultSet.getString("email");
    String dbsPassword = resultSet.getString("password_hash");
    boolean dbsIsAdmin = resultSet.getBoolean("isAdmin");
    int balance = resultSet.getInt("balance");