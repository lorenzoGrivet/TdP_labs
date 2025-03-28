from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    _id: int
    _event_type_id: int
    _tag_id: int
    _area_id: int
    _nerc_id: int
    _responsible_id: int
    _customers_affected: int
    _date_event_began: datetime
    _date_event_finished: datetime
    _demand_loss: int

    @property
    def id(self):
        return self._id

    @property
    def event_type_id(self):
        return self._event_type_id

    @property
    def tag_id(self):
        return self._tag_id

    @property
    def area_id(self):
        return self._area_id

    @property
    def nerc_id(self):
        return self._nerc_id

    @property
    def responsible_id(self):
        return self._responsible_id

    @property
    def customers_affected(self):
        return self._customers_affected


    def date_event_began(self):
        return self._date_event_began

    @property
    def date_event_finished(self):
        return self._date_event_finished

    @property
    def demand_loss(self):
        return self._demand_loss

    def __str__(self):
        # return (f"PowerOutage [id={self._id}, nerc={self._nerc_id}, customers_affected={self._customers_affected} "
        #         f"start_time={self._date_event_began}, end_time= {self._date_event_finished}]")

        return (f"id={self._id}, customers_affected={self._customers_affected} "
                f"start_time={self._date_event_began}, end_time= {self._date_event_finished}")

    def __hash__(self):
        return hash(self._id)


    def __eq__(self, other):
        return self._date_event_began == other._date_event_began



