"""CP1404 Week 07 Practicals
Project Class for Project Management Program"""

from datetime import date


class Project:
    """Represent a project object."""

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion_percentage: float):
        """Construct a project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string representation of a project object"""
        return (f"Project={self.name}, Start Date={self.start_date}, Priority={self.priority}, "
                f"Cost Estimate={self.cost_estimate}, Completion Percentage={self.completion_percentage}")

    def __str__(self):
        return (f"{self.name}, a priority {self.priority} project estimated to cost {self.cost_estimate} started on "
                f"{self.start_date} and is {self.completion_percentage}% complete.")

    def __lt__(self, other):
        return self.priority < other.priority
