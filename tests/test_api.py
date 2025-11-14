import pytest
import requests

BASE_URL = "http://localhost:5000/posts"  # your Flask backend URL

post_id = None  # global variable to store created post id

def test_get_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post():
    global post_id
    payload = {"title": "Test Post", "content": "This is a test."}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code in [200, 201]

    data = response.json()

    # Save the first field as post_id if '_id' doesn't exist
    post_id = data.get('_id') or data.get('id') or None

    # Optional: check title if it exists
    if 'title' in data:
        assert data['title'] == payload['title']

def test_update_post():
    global post_id
    if not post_id:
        pytest.skip("No post_id available, skipping update test")

    payload = {"title": "Updated Title", "content": "Updated content"}
    response = requests.patch(f"{BASE_URL}/{post_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    if 'title' in data:
        assert data['title'] == payload['title']

def test_delete_post():
    global post_id
    if not post_id:
        pytest.skip("No post_id available, skipping delete test")

    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code in [200, 204]
