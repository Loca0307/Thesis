
func TestChecker_ErrorGracePeriod(t *testing.T) {
	t.Parallel()

	t.Run("within grace period", func(t *testing.T) {
		t.Parallel()

		c, err := NewChecker(WithCheckerErrorGracePeriod(5 * time.Second))
		require.NoError(t, err)
		require.NotNil(t, c)

		check := NewCheck("test_check", func(_ context.Context) error {
			return errors.New("test error")
		})

		err = c.AddCheck(check)
		require.NoError(t, err)

		// Simulate a failure
		c.firstFailInCycle.Store(time.Now().UTC().Add(-2 * time.Second))

		res := c.Check(context.Background())
		require.Equal(t, StatusUp, res.Status)
	})

	t.Run("outside grace period", func(t *testing.T) {
		t.Parallel()

		c, err := NewChecker(WithCheckerErrorGracePeriod(5 * time.Second))
		require.NoError(t, err)
		require.NotNil(t, c)

		check := NewCheck("test_check", func(_ context.Context) error {
			return errors.New("test error")
		})

		err = c.AddCheck(check)
		require.NoError(t, err)

		// Simulate a failure
		c.firstFailInCycle.Store(time.Now().UTC().Add(-10 * time.Second))

		res := c.Check(context.Background())
		require.Equal(t, StatusDown, res.Status)
	})

	t.Run("multiple async checks", func(t *testing.T) {
		t.Parallel()

		c, err := NewChecker(WithCheckerErrorGracePeriod(5 * time.Second))
		require.NoError(t, err)
		require.NotNil(t, c)

		check1 := NewCheck("test_check_1", func(_ context.Context) error {
			return errors.New("test error")
		})

		check2 := NewCheck("test_check_2", func(_ context.Context) error {
			return errors.New("test error 2")
		})

		check3 := NewCheck("test_check_3", func(_ context.Context) error {
			return errors.New("test error 3")
		})

		err = c.AddCheck(check1)
		require.NoError(t, err)

		err = c.AddCheck(check2)
		require.NoError(t, err)

		err = c.AddCheck(check3)
		require.NoError(t, err)

		res := c.Check(context.Background())
		require.Equal(t, StatusUp, res.Status)
	})
}