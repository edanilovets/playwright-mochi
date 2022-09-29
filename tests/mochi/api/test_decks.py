from playwright.sync_api import expect


def test_number_of_top_level_decks(api_request_context):

    response = api_request_context.get("/api/decks")

    expect(response).to_be_ok()
    decks = response.json()["docs"]
    top_level_decks = [d for d in decks if d.get("parent-id") is None]

    assert len(top_level_decks) == 6
