                        // Save changes to the database
                        await _context.SaveChangesAsync();
                        return Ok($"You are now following \"{whom.UserName}\"");
                    }
                    else
                    {
                        return BadRequest("You are already not following the user");
                    }
                }
                else
                {
                    return NotFound("Follower user not found");
                }