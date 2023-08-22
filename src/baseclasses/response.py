from pydantic.error_wrappers import ValidationError
from src.enums.global_enums import GlobalErrorMessage
from PIL import Image


class Response:
    def __init__(self, response):
        self.response = response
        if response.json():
            self.response_json = response.json()
            self.response_status = response.status_code
            self.response_time = response.elapsed.total_seconds()


    def validate(self, schema):
        """Validate response"""
        try:
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    parsed_object = schema.parse_obj(item)
                    self.parsed_object = parsed_object

            else:
                schema.parse_obj(self.response_json)
        except ValidationError as e:
            print(e.json())
            raise AssertionError(
                "Could not map received object to pydantic schema"
            )

    def assert_status_code(self, status_code):
        """Assert response status code"""
        if isinstance(status_code, list):
            assert self.response_status in status_code, (f"Wrong response status code {self.response_status} "
                                                         f"Error message {self.response_json}")
        else:
            assert self.response_status == status_code, (f"Wrong response status code {self.response_status} "
                                                         f"Error message {self.response_json}")

        return self

    def assert_value(self, key, value):
        """Assert response value"""

        assert self.response_json[key] == value, f"Value Error, response:  {self.response_json[key]} not equal to {value} "


        return self

    def assert_not_value(self, key, value):
        """Assert response value"""
        assert self.response_json[key] != value, f"Value Error, response:  {self.response_json} "
        return self

    def assert_equal(self, value1, value2):

        assert value1 == value2, f"Value Error, response: {value1} not equal to {value2}"
        return self

    def assert_minimum_response_time(self, time):
        """Assert response time"""
        assert self.response_time <= time, f"Response time {self.response_time}"
        return self

    def assert_size(self, size_height, size_width, image):
        """Assert response file size"""
        im = Image.open(image)
        width, height = im.size
        assert width == size_width
        assert height == size_height
        return self
    def __str__(self):

        return \
            f"\nStatus code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"