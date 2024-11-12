class Project:
    """Project class for storing details of a project."""

    def __init__(self, name, start_date, priority=0, cost_estimate=0, completion_percentage=0.0):
        """Initialises a project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date}, priority: {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completion : {self.completion_percentage}%")

    def is_complete(self):
        """Determines if the project has been completed."""
        return self.completion_percentage == 100
