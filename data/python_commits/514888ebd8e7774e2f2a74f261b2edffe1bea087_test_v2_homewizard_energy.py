### Batteries tests ###


async def test_batteries_without_authentication():
    """Test batteries request is rejected when no authentication is provided."""

    async with HomeWizardEnergyV2("example.com") as api:
        with pytest.raises(UnauthorizedError):
            await api.batteries()


async def test_batteries_with_invalid_authentication(aresponses):
    """Test batteries request is unsuccessful when invalid authentication is provided."""

    aresponses.add(
        "example.com",
        "/api/batteries",
        "GET",
        aresponses.Response(
            status=401,
            headers={"Content-Type": "application/json"},
            text='{"error": "user:unauthorized"}',
        ),
    )

    async with HomeWizardEnergyV2("example.com", token="token") as api:
        with pytest.raises(UnauthorizedError):
            await api.batteries()


@pytest.mark.parametrize(
    ("model", "fixtures"),
    [
        ("HWE-P1", ["batteries"]),
    ],
)
async def test_batteries_with_valid_authentication(
    model: str, fixtures: list[str], snapshot: SnapshotAssertion, aresponses
):
    """Test batteries request is successful when valid authentication is provided."""

    for fixture in fixtures:
        aresponses.add(
            "example.com",
            "/api/batteries",
            "GET",
            aresponses.Response(
                text=load_fixtures(f"{model}/{fixture}.json"),
                status=200,
                headers={"Content-Type": "application/json"},
            ),
        )

        async with HomeWizardEnergyV2("example.com", token="token") as api:
            batteries = await api.batteries()
            assert batteries is not None
            assert batteries == snapshot


async def test_batteries_returns_unexpected_response(aresponses):
    """Test batteries request is successful when valid authentication is provided."""

    aresponses.add(
        "example.com",
        "/api/batteries",
        "GET",
        aresponses.Response(
            status=500,
            headers={"Content-Type": "application/json"},
            text='{"error": "server:error"}',
        ),
    )

    async with HomeWizardEnergyV2("example.com", token="token") as api:
        with pytest.raises(RequestError) as e:
            await api.batteries()
            assert str(e.value) == "server:error"


async def test_batteries_put_without_authentication():
    """Test batteries request is rejected when no authentication is provided."""

    async with HomeWizardEnergyV2("example.com") as api:
        with pytest.raises(UnauthorizedError):
            await api.batteries(mode=Batteries.Mode.STANDBY)


async def test_batteries_put_with_invalid_authentication(aresponses):
    """Test batteries request is unsuccessful when invalid authentication is provided."""

    aresponses.add(
        "example.com",
        "/api/batteries",
        "PUT",
        aresponses.Response(
            status=401,
            headers={"Content-Type": "application/json"},
            text='{"error": "user:unauthorized"}',
        ),
    )

    async with HomeWizardEnergyV2("example.com", token="token") as api:
        with pytest.raises(UnauthorizedError):
            await api.batteries(mode=Batteries.Mode.STANDBY)


@pytest.mark.parametrize(
    ("model"),
    [
        ("HWE-P1"),
    ],
)
async def test_batteries_put_with_valid_authentication(
    model: str, snapshot: SnapshotAssertion, aresponses
):
    """Test batteries request is successful when valid authentication is provided."""

    aresponses.add(
        "example.com",
        "/api/batteries",
        "PUT",
        aresponses.Response(
            text=load_fixtures(f"{model}/batteries.json"),
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )

    async with HomeWizardEnergyV2("example.com", token="token") as api:
        batteries = await api.batteries(mode=Batteries.Mode.STANDBY)
        assert batteries is not None
        assert batteries == snapshot

