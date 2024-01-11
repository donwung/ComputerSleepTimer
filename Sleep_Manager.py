class Sleep_Manager:
    def __init__(self, input_field):
        print("Sleep_Manager instantiated")
        self.input_field = input_field
        self.time_dict = {"hours": 0, "minutes": 0, "seconds": 0}

    # TODO: make another class to receive time to go to sleep AT

    def receive_time(self):
        print("receiving a time")
        new_time = self.input_field.get_input_time()
        self.time_dict = new_time
        print(self.time_dict)

    def convert_to_ms(self, time_dict):
        hours_to_ms = int(time_dict["hours"]) * 3600000
        minutes_to_ms = int(time_dict["minutes"]) * 60000
        seconds_to_ms = int(time_dict["seconds"]) * 1000
        # print(f"{str(time_dict['hours'])} hour -> {hours_to_ms} milliseconds")
        # print(f"{str(time_dict['minutes'])} hour -> {minutes_to_ms} milliseconds")
        # print(f"{str(time_dict['seconds'])} hour -> {seconds_to_ms} milliseconds")

        time_to_sleep_in_ms = hours_to_ms + minutes_to_ms + seconds_to_ms
        print(time_to_sleep_in_ms)
        return time_to_sleep_in_ms

    def set_sleep_time(self):
        print("setting sleep time")

    def go_to_sleep(self):
        print("COMPUTER IS BEING PUT TO SLEEP")
        print(f"sleeping in: {str(self.convert_to_ms(self.time_dict))} ms")


# TODO: 
# TODO: 
# TODO: create an inherited class to set sleep using sleep AT
