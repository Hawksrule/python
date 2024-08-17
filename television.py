class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """Sets default values for instance variables"""
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

    def power(self):
        """Toggles the television status, setting it to the opposite state"""
        self.status = not self.status

    def mute(self):
        """Toggles the muted status, setting it to the opposite state if the television is on"""
        if self.status:
            self.muted = not self.muted

    def channel_up(self):
        """Increments the channel until reaching max, at which point it restarts from min as long as the television is on"""
        if self.status:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        """Decrements the channel until reaching min, at which point it restarts from max as long as the television is on"""
        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        """Increments the volume until reaching max, as long as the television is on. Unmutes if muted."""
        if self.status:
            if self.volume != self.MAX_VOLUME:
                self.volume += 1
            self.muted = False

    def volume_down(self):
        """Decrements the volume until reaching min, as long as the television is on. Unmutes if muted."""
        if self.status:
            if self.volume != self.MIN_VOLUME:
                self.volume -= 1
            self.muted = False

    def __str__(self):
        """Returns a string representation of the television states including Power, Channel, and Volume"""
        if self.muted:
            return f"Power - {self.status}, Channel - {self.channel}, Volume - 0"
        else:
            return f"Power - {self.status}, Channel - {self.channel}, Volume - {self.volume}"


