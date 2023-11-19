import requests
import typing as T

from src.core.interfaces import BaseHardCode

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


    def get_response_content(self) -> dict:
        information_keys = list()
        checked_content = dict()

        if self.response_content and isinstance(self.response_content, list):
            for item in self.response_content:
                for key, _ in item.items():
                    if not key in self.response_keys:
                        information_keys.append(key)
                    else:
                        continue

                for info_key in information_keys:
                    # print(info_key+': '+str(item.get(info_key)))

                    checked_content[info_key] = item.get(info_key)

                break

        # print(checked_content)
        print(information_keys)

        return checked_content


    def manipulating_content(self, checked_content: dict):
        # print(checked_content)
        name = checked_content.get('name')
        independent = checked_content.get('independent')
        status = checked_content.get('status')
        un_member = checked_content.get('unMember')
        currencies = checked_content.get('currencies')
        capital = checked_content.get('capital')
        altSpellings = checked_content.get('altSpellings')
        region = checked_content.get('region')
        subregion = checked_content.get('subregion')
        languages = checked_content.get('languages')
        translations = checked_content.get('translations')
        lat_lng = checked_content.get('latlng')
        landlocked = checked_content.get('landlocked')
        borders = checked_content.get('borders')
        area = checked_content.get('area')
        demonyms = checked_content.get('demonyms')
        flag = checked_content.get('flag')
        maps = checked_content.get('maps')
        population = checked_content.get('population')
        gini = checked_content.get('gini')
        fifa = checked_content.get('fifa')
        car = checked_content.get('car')
        timezones = checked_content.get('timezones')
        continents = checked_content.get('continents')
        flags = checked_content.get('flags')
        coat_of_arms = checked_content.get('coatOfArms')
        start_of_week = checked_content.get('startOfWeek')
        capital_info = checked_content.get('capitalInfo')
        print(area)
        # pass


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