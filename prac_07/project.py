"""CP1404 Week 07 Practicals
Project Class for Project Management Program"""

from datetime import date


class Project:
    """Represent a project object."""

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion_percentage: int):
        """Construct a project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a representation of a project."""
        return (f"Project={self.name}, Start Date={self.start_date}, Priority={self.priority}, "
                f"Cost Estimate={self.cost_estimate}, Completion Percentage={self.completion_percentage}")

    def __str__(self):
        """Return a string version of a project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare the priority of two projects to determine if one is less than the other."""
        return self.priority < other.priority

    def is_complete(self):
        """Return true if project completion == 100"""
        return self.completion_percentage == 100
