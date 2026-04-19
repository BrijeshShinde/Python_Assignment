class Patient:
    def __init__(self, name, status):
        # status: 0 = Normal, 1 = Urgent, 2 = Super-Urgent
        self.name = name
        self.status = status

    def status_text(self):
        if self.status == 2:
            return "Super-Urgent"
        elif self.status == 1:
            return "Urgent"
        else:
            return "Normal"

    def __str__(self):
        return f"{self.name} ({self.status_text()})"
