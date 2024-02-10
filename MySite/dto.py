class Dto():
    def __init__(self, title, review, quality, location, price, landlord, neighborhood, transportation):
        self.title = title
        self.review = review
        self.quality = quality
        self.location = location
        self.price = price
        self.landlord = landlord
        self.neighborhood = neighborhood
        self.transportation = transportation


class DtoGarage():
    def __init__(self, garage):
        self.garage = garage

    def convertBooleanToString(self, dto):
        if dto.garage is True:
            self.garage = 'Yes'
        else:
            self.garage = 'No'
        pass
