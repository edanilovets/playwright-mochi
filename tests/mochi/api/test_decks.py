from playwright.sync_api import expect


def test_list_all_decks(api_request_context):

    response = api_request_context.get("/api/decks")

    assert response.ok
    json = response.json()
    # todo: add assertions

    assert json is not None
