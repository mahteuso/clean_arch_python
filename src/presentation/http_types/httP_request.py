class HttpRequest:

    def __init__(
        self,
        headers,
        body,
        query_params,
        path_params,
        url,
        ipv4
    ) -> None:

        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
