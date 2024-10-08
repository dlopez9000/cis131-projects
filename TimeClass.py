# Darlene Lopez
# CIS 131
# Modify the class to store the time as the total number of seconds since midnight.

class Time:
    """Class Time with read-write properties using total seconds."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize the time as total seconds since midnight."""
        self._total_seconds = 0
        self.set_time(hour, minute, second)

    @property
    def hour(self):
        """Return the hour based on total seconds."""
        return self._total_seconds // 3600  # 1 hour = 3600 seconds

    @hour.setter
    def hour(self, hour):
        """Set the hour, adjusting total seconds."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._total_seconds = (self._total_seconds % 3600) + hour * 3600

    @property
    def minute(self):
        """Return the minute based on total seconds."""
        return (self._total_seconds % 3600) // 60  # 1 minute = 60 seconds

    @minute.setter
    def minute(self, minute):
        """Set the minute, adjusting total seconds."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._total_seconds = (self._total_seconds // 3600) * 3600 + minute * 60 + self.second

    @property
    def second(self):
        """Return the second based on total seconds."""
        return self._total_seconds % 60

    @second.setter
    def second(self, second):
        """Set the second, adjusting total seconds."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds = (self._total_seconds // 60) * 60 + second

    def set_time(self, hour=0, minute=0, second=0):
        """Set the time based on hour, minute, and second."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds = hour * 3600 + minute * 60 + second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, '
                f'second={self.second})')

    def __str__(self):
        """Print Time in 12-hour clock format."""
        hour_display = ('12' if self.hour in (0, 12) else str(self.hour % 12))
        return (f'{hour_display}:{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))
# Assuming the modified Time class code is defined above

# Create instances of the Time class
time1 = Time(4, 35, 15)  # 4:35:15 AM
print(time1)  # Should print time
print(repr(time1))  # Should print time

# Access the hour, minute, and second properties
print("Hour:", time1.hour)    # Should print: Hour
print("Minute:", time1.minute)  # Should print: Minute
print("Second:", time1.second)  # Should print: Second

# Modify the time
time1.hour = 5
time1.minute = 35
time1.second = 20
print(time1)  # Should print time
print(repr(time1))  # Should print non-military time

# Create another instance using total seconds
time2 = Time()
time2.set_time(14, 30, 20)  # Setting time to 2:30:20 PM
print(time2)  # Should print time shown
