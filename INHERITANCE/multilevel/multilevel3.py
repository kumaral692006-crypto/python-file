class bike:
    def brand_bike(self):
        print("name:royal enfiled")

class model(bike):
    def model_bike(self):
        print("model: himalaya 411")

class offroad(model):
    def suspansion_offroad(self):
        print("offroad: 100%")

c=offroad()
c.brand_bike()
c.model_bike()
c.suspansion_offroad()