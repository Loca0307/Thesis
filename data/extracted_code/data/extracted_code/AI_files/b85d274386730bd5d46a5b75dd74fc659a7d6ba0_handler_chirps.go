}

func (cfg *apiConfig) handleDeleteChirpByID(response http.ResponseWriter, request *http.Request, userID uuid.UUID) {
	// Parse request params
	chirpID, err := uuid.Parse(request.PathValue("chirpID"))
	if err != nil {
		msg := fmt.Sprintf("chirps: Problem parsing chirpID from request: %s", err)
		log.Println(msg)
		respondWithError(response, http.StatusBadRequest, msg)
		return
	}

	// Fetch chirp to confirm user owns it
	row, err := cfg.db.GetChirpByID(request.Context(), chirpID)
	if err != nil {
		msg := fmt.Sprintf("chirps: Problem retrieving chirp with id '%s': %s", chirpID, err)
		log.Println(msg)
		respondWithError(response, http.StatusNotFound, msg)
		return
	}

	if row.UserID != userID {
		msg := fmt.Sprintf("chirps: User '%s' does not own chirp '%s'", userID, chirpID)
		log.Println(msg)
		respondWithError(response, http.StatusForbidden, msg)
		return
	}

	// Delete chirp
	err = cfg.db.DeleteChirpByID(request.Context(), chirpID)
	if err != nil {	
		msg := fmt.Sprintf("chirps: Problem deleting chirp with id '%s': %s", chirpID, err)
		log.Println(msg)
		respondWithError(response, http.StatusInternalServerError, msg)
		return
	}

	// Respond with success
	response.WriteHeader(http.StatusNoContent)