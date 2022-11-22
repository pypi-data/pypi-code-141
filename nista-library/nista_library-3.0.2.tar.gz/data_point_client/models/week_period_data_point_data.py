from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.week_data_transfere import WeekDataTransfere
from ..types import UNSET, Unset

T = TypeVar("T", bound="WeekPeriodDataPointData")


@attr.s(auto_attribs=True)
class WeekPeriodDataPointData:
    """
    Attributes:
        status (Union[Unset, None, str]):
        error_message (Union[Unset, None, str]):
        unit (Union[Unset, None, str]):
        number_of_entries (Union[Unset, int]):
        week_data (Union[Unset, None, WeekDataTransfere]):
    """

    status: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    unit: Union[Unset, None, str] = UNSET
    number_of_entries: Union[Unset, int] = UNSET
    week_data: Union[Unset, None, WeekDataTransfere] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        error_message = self.error_message
        unit = self.unit
        number_of_entries = self.number_of_entries
        week_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.week_data, Unset):
            week_data = self.week_data.to_dict() if self.week_data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if unit is not UNSET:
            field_dict["unit"] = unit
        if number_of_entries is not UNSET:
            field_dict["numberOfEntries"] = number_of_entries
        if week_data is not UNSET:
            field_dict["weekData"] = week_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        unit = d.pop("unit", UNSET)

        number_of_entries = d.pop("numberOfEntries", UNSET)

        _week_data = d.pop("weekData", UNSET)
        week_data: Union[Unset, None, WeekDataTransfere]
        if _week_data is None:
            week_data = None
        elif isinstance(_week_data, Unset):
            week_data = UNSET
        else:
            week_data = WeekDataTransfere.from_dict(_week_data)

        week_period_data_point_data = cls(
            status=status,
            error_message=error_message,
            unit=unit,
            number_of_entries=number_of_entries,
            week_data=week_data,
        )

        week_period_data_point_data.additional_properties = d
        return week_period_data_point_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
