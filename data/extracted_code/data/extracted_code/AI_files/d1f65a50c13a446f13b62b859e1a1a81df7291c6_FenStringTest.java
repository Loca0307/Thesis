
    // Testing edge cases for location to square conversion
    @Test
    public void locationToSquareEdgeCases() {
        assertThatThrownBy(() -> FenString.locationToSquare(64)).isInstanceOf(IllegalArgumentException.class);
        assertThatThrownBy(() -> FenString.locationToSquare(-2)).isInstanceOf(IllegalArgumentException.class);
    }

    // Testing edge cases for square to location conversion with additional characters
    @Test
    public void squareToLocationCheckAndCheckmate() {
        assertThat(FenString.squareToLocation("e2+")).isEqualTo(12);
        assertThat(FenString.squareToLocation("e2#")).isEqualTo(12);
        assertThatThrownBy(() -> FenString.squareToLocation("k9+")).isInstanceOf(IllegalArgumentException.class);
    }

    // Testing invalid piece placements
    @Test
    public void invalidPiecePlacements() {
        assertThatThrownBy(() -> new FenString("8/8/8/8/8/8/8/9 w KQkq -")).isInstanceOf(IllegalArgumentException.class);
        assertThatThrownBy(() -> new FenString("rnbqkbnr/pppppppp/7/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -")).isInstanceOf(IllegalArgumentException.class);
    }

    // Testing invalid castling rights scenarios
    @Test
    public void invalidCastlingRights() {
        assertThatThrownBy(() -> new FenString(FenString.INITIAL_BOARD.replace("KQkq", "KQRkq"))).isInstanceOf(IllegalArgumentException.class);
        assertThatThrownBy(() -> new FenString(FenString.INITIAL_BOARD.replace("KQkq", "QQkk"))).isInstanceOf(IllegalArgumentException.class);
    }

    // Testing en passant target with invalid ranks
    @Test
    public void enPassantTargetInvalidRanks() {
        assertThatThrownBy(() -> new FenString("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq b2")).isInstanceOf(IllegalArgumentException.class);
        assertThatThrownBy(() -> new FenString("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq g7")).isInstanceOf(IllegalArgumentException.class);
    }

    // Testing move counters with invalid values
    @Test
    public void moveCountersInvalidValues() {
        assertThatThrownBy(() -> new FenString("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - -1 1")).isInstanceOf(NumberFormatException.class);
        assertThatThrownBy(() -> new FenString("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 -1")).isInstanceOf(NumberFormatException.class);
    }

    // Testing valid scenarios with minimum and maximum values for move counters
    @Test
    public void moveCountersValidExtremes() {
        FenString fsMin = new FenString("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
        assertThat(fsMin.getHalfmoveClock()).isEqualTo(0);
        assertThat(fsMin.getFullmoveCounter()).isEqualTo(1);

        // Assuming 999 is a valid maximum for the sake of this example
        FenString fsMax = new FenString("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 100 999");
        assertThat(fsMax.getHalfmoveClock()).isEqualTo(100);
        assertThat(fsMax.getFullmoveCounter()).isEqualTo(999);
    }