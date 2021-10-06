import api


class Tool:

    # 提取sessionId
    @classmethod
    def common_session_id(cls, response):
        # 提取session
        sessionId = response.get("data").get("sessionId")
        api.headers['x-auth-token'] = sessionId
        print("添加sessionId后的header为:", api.headers)

    # 断言
    @classmethod
    def common_assert(cls, response):
        # 断言状态码
        assert 0 == response.get("code")
        # 断言状态信息
        assert "SUCCESS" == response.get("msg")