class http:
    @classmethod
    def get(cls, url):
        try:
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            c.close()
            response = buffer.getvalue().decode('utf-8')
            return response
        except pycurl.error:
            return ' • CONNECTION ERROR BRO '

    @classmethod
    def post(cls, url, data, headers):
        try:
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.HTTPHEADER, [f"{name}:{value}" for name, value in headers.items()])
            c.setopt(c.WRITEDATA, buffer)
            data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
            c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
            c.perform()
            c.close()
            body = buffer.getvalue().decode('utf-8')
            return body
        except pycurl.error:
            return ' • CONNECTION ERROR BRO '
