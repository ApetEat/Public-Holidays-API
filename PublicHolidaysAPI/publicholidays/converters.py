

# Create your converters here.


class DateConverter(object):
    regex = '(20[1-9]{2})[-/.](0?[1-9]|1[0-2])[-/.](0?[1-9]|1[0-9]|2[0-9]|3[0-1])'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d/%d/%d' % (value[1], value[2], value[3])
