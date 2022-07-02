from rest_framework.throttling import AnonRateThrottle


class CNNImagePostAnonThrottle(AnonRateThrottle):
    rate = '5/minute'
