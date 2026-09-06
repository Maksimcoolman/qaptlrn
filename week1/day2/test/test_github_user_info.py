from qaptlrn.week1.day2.test.github_user_info import get_github_user_info

def test_answer():
    data = get_github_user_info("octocat")
    assert 'login' in data
    assert 'id' in data
    assert data['login'] == "octocat"
    assert isinstance(data['public_repos'], int)
