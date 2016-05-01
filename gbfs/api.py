import urllib
import json

GBFS_FILE = 'gbfs.json'
SYSTEM_INFORMATION_FILE = 'system_information.json'
STATION_STATUS_FILE = 'station_status.json'
STATION_INFO_FILE = 'station_information.json'
FREE_BIKE_STATUS_FILE = 'free_bike_status.json'
SYSTEM_HOURS_FILE = 'system_hours.json'
SYSTEM_CALENDAR_FILE = 'system_calendar.json'
SYSTEM_REGIONS_FILE = 'system_regions.json'
SYSTEM_PRICING_PLANS_FILE = 'system_pricing_plans.json'
SYSTEM_ALERTS_FILE = 'system_alerts.json'


class Error(Exception):
    pass


class UnimplementedFileError(Error):
    pass


class Client(object):

    def __init__(self, endpoint):
        self._process_and_store_endpoint(endpoint)

    def _process_and_store_endpoint(self, endpoint):
        if endpoint[-1] != '/':
            endpoint += '/'
        self._endpoint = endpoint

    def gbfs(self):
        return self._make_request(GBFS_FILE)

    def system_information(self):
        return self._make_request(SYSTEM_INFORMATION_FILE)

    def station_status(self):
        return self._make_request(STATION_STATUS_FILE)

    def station_information(self):
        return self._make_request(STATION_INFO_FILE)

    def free_bike_status(self):
        return self._make_request(FREE_BIKE_STATUS_FILE)

    def system_hours(self):
        return self._make_request(SYSTEM_HOURS_FILE)

    def system_calendar(self):
        return self._make_request(SYSTEM_CALENDAR_FILE)

    def system_regions(self):
        return self._make_request(SYSTEM_REGIONS_FILE)

    def system_pricing_plans(self):
        return self._make_request(SYSTEM_PRICING_PLANS_FILE)

    def system_alerts(self):
        return self._make_request(SYSTEM_ALERTS_FILE)

    def _make_request(self, api_file):
        url = self._endpoint + api_file
        req = urllib.request.urlopen(url)
        data = req.read()
        if data.strip() == '':
            raise UnimplementedFileError()
        return json.loads(data)
