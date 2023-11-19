import requests
import typing as T

from src.core.interfaces.interfaces import BaseHardCode

class HardCode(BaseHardCode):
    def __init__(
        self,
        url: str | None = None,
        version: str | None = None,
        **kwargs
    ) -> None:
        self.req = requests
        self.url = url or 'https://restcountries.com'
        self.version = version or 'v3.1'
        self.endpoint: T.Optional[T.Union[str, None]] = f'{self.url}/{self.version}/' if self.url and self.version else None
        self.response_content = set()
        self.response_keys: list = [
            "tld",
            "cca2",
            "ccn3",
            "cca3",
            "cioc",
            "idd"
        ]

        super().__init__(**kwargs)


    @property
    def check_status(self) -> int:
        response = self.req.get(self.endpoint+'all')
        response_status = response.status_code
        if response_status == 200:
            try:
                response = response.json()
            except Exception as err:
                raise err
            self.response_content = response
        return response_status


    def get_response_content(self) -> list:
        information_keys = []

        if self.response_content and isinstance(self.response_content, list):
            for item in self.response_content:
                for key, _ in item.items():
                    if not key in self.response_keys:
                        information_keys.append(key)
                    else:
                        continue

                for info_key in information_keys:
                    print(info_key+': '+str(item.get(info_key)))

                break

        return information_keys


    def manipulating_content(self, information_keys: list):
        # print(information_keys)
        # for info_key in information_keys:
        pass


    # def start_process(self):
    #     response_req = self.req.get(self.endpoint+'/all')
    #     response_status = response_req.status_code
    #     response_content = response_req.content
    #     print(response_req)






if __name__ == '__main__':
    def main():
        instance = HardCode()
        instance.start_process()
    main()