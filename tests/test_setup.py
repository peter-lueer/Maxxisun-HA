import pytest

from homeassistant.core import HomeAssistant

from custom_components.maxxisun.const import DOMAIN
from custom_components.maxxisun.__init__ import async_setup_entry
from pytest_homeassistant_custom_component.common import MockConfigEntry


@pytest.mark.asyncio
async def test_async_setup_entry_initializes_data(hass: HomeAssistant, monkeypatch):
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            "email": "user@example.com",
            "ccu": "CCU-1",
            "token": "test-token",
            "API_POLL_INTERVAL": 30,
        },
    )
    entry.add_to_hass(hass)

    async def fake_forward_entry_setups(_entry, platforms):
        # Stub out platform forwarding during unit test
        assert platforms == ["sensor"]
        return None

    monkeypatch.setattr(
        hass.config_entries,
        "async_forward_entry_setups",
        fake_forward_entry_setups,
        raising=True,
    )

    result = await async_setup_entry(hass, entry)
    assert result is True

    assert DOMAIN in hass.data
    assert entry.entry_id in hass.data[DOMAIN]
    data = hass.data[DOMAIN][entry.entry_id]
    assert data["token"] == "test-token"
    assert data["API_POLL_INTERVAL"] == 30
