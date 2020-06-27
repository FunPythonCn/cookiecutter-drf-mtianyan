import requests


def gen(base_url, url):
    view_name = "".join([one.title() for one in url.split("/")]) + "View"
    url_txt = f"""
    path('{url}', {view_name}.as_view()),
    """
    head = {
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJjNmMzNjhiMTdlMGQ0ZGI5YTllZGYzMWNmNzhiMDhkNSIsImF1dGgiOiJhZG1pbiIsInN1YiI6ImFkbWluIn0.9YIDwVrwZ3nFtUrM4S1aWt8qLkexF3Ia-Sc3l3WPy0YbgNsyzAUBnViZiwLkejSJtU4ScgLYa7JFLK7B9fI3nw"
    }
    res = requests.get(base_url+url,headers=head).json()
    api_txt = f"""
class {view_name}(APIView):
    def get(self, request):
        return Response({res})
    """.replace("null",'None').replace("true", "True").replace("false", "False")

    print(url_txt)
    print(api_txt)


if __name__ == '__main__':
    base_url = "http://localhost:8000/"
    url = input("输入route:")
    gen(base_url, url)
