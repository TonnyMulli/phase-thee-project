class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a non-empty string")
        if not isinstance(hometown, str) or hometown == "":
            raise ValueError("Hometown must be a non-empty string")

        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    def concerts(self):
        return self._concerts

    def venues(self):
        venues = []
        for concert in self._concerts:
            if concert and concert.venue:
                venues.append(concert.venue)
        return list(set(venues))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts if concert is not None]


class Venue:
    def __init__(self, name, city):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not city or not isinstance(city, str):
            raise ValueError("City must be a non-empty string")
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        if isinstance(new_city, str) and new_city:
            self._city = new_city
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set([concert.band for concert in self._concerts]))


class Concert:
    all = []

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or not date:
            raise ValueError("Date must be a non-empty string")
        if not isinstance(band, Band):
            raise ValueError("Band must be an instance of Band")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be an instance of Venue")

        self._date = date
        self.band = band
        self.venue = venue

        if band is not None:
            band._concerts.append(self)
        if venue is not None:
            venue._concerts.append(self)
        if Concert.all is not None:
            Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be an instance of Band")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be an instance of Venue")

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
