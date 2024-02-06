class Dto():
    def __init__(self, title, description, rent_price, house_city, house_address, bedrooms, bathrooms, area, yard_area,
                 year, garage, review, owner_number):
        self.title = title
        self.description = description
        self.rent_price = rent_price
        self.house_city = house_city
        self.house_address = house_address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.area = area
        self.yard_area = yard_area
        self.year = year
        self.garage = garage
        self.review = review
        self.owner_number = owner_number

    def convertBooleanToString(self, dto):
        if dto.garage is True:
            self.garage = 'Yes'
        else:
            self.garage = 'No'
        pass
