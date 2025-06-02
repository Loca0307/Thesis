            {student.length === 0 ? ( //Conditional Rendering: handle cases when there are no students in the list
              <p>No students available</p>
            ) : (
              student.map((data, i) => (
                <tr key={i}>
                  <td>{data.Name}</td>
                  <td>{data.Email}</td>
                  <td>
                    <Link to={`update/${data.ID}`} className="btn btn-primary">
                      Update
                    </Link>
                    <Link
                      to={`view/${data.ID}`}
                      className="btn btn-success ms-2"
                    >
                      View
                    </Link>
                    <button
                      className="btn btn-danger ms-2"
                      onClick={(e) => handleDelete(data.ID)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))
            )}