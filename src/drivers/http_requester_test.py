from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    response_context = '<h1>OK!</h1>'
    requests_mock.get(url, status_code=200, text=response_context)
    http_requester = HttpRequester()
    http_response = http_requester.request_from_page()
    print(http_response)

    assert 'status_code' in http_response
    assert 'html' in http_response
    assert http_response['status_code'] == 200
    assert http_response['html'] == response_context