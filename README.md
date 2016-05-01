# GBFS #

Module interacting with endpoints implementing the [GBFS standard V1.0](https://github.com/NABSA/gbfs/blob/master/gbfs.md).

## Install ##
    git clone https://github.com/kjschiroo/Python-GBFS
    cd Python-GBFS
    python3 setup.py install

## Example ##

    > import gbfs
    > cl = gbfs.Client('https://api-core.niceridemn.org/gbfs/en/')
    > cl.system_information()
    # {
    #     "data": {
    #         "timezone": "US/Central",
    #         "name": "Nice Ride Minnesota",
    #         "system_id": "niceridemn",
    #         "operator": "Nice Ride Minnesota",
    #         "email": "customerservice@niceridemn.org",
    #         "start_date": "2010-06-09",
    #         "language": "en",
    #         "purchase_url": "https://www.niceridemn.org",
    #         "url": "http://www.niceridemn.org",
    #         "short_name": "Nice Ride MN",
    #         "phone_number": "1-877-551-6423"
    #     },
    #     "last_updated": 1462135264,
    #     "ttl": 60
    # }

## GBFS.Client ##
GBFS.Client(endpoint_url)

### functions ###
gbfs(self)

system_information(self)

station_status(self)

station_information(self)

free_bike_status(self)

system_hours(self)

system_calendar(self)

system_regions(self)

system_pricing_plans(self)

system_alert
