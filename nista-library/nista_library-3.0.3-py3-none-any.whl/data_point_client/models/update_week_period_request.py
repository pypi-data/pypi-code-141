from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.week_data_transfere import WeekDataTransfere
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWeekPeriodRequest")


@attr.s(auto_attribs=True)
class UpdateWeekPeriodRequest:
    """
    Attributes:
        execution_id (Union[Unset, None, str]):
        week_data (Union[Unset, None, WeekDataTransfere]):
        unit (Union[Unset, None, str]):
    """

    execution_id: Union[Unset, None, str] = UNSET
    week_data: Union[Unset, None, WeekDataTransfere] = UNSET
    unit: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        execution_id = self.execution_id
        week_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.week_data, Unset):
            week_data = self.week_data.to_dict() if self.week_data else None

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if week_data is not UNSET:
            field_dict["weekData"] = week_data
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        execution_id = d.pop("executionId", UNSET)

        _week_data = d.pop("weekData", UNSET)
        week_data: Union[Unset, None, WeekDataTransfere]
        if _week_data is None:
            week_data = None
        elif isinstance(_week_data, Unset):
            week_data = UNSET
        else:
            week_data = WeekDataTransfere.from_dict(_week_data)

        unit = d.pop("unit", UNSET)

        update_week_period_request = cls(
            execution_id=execution_id,
            week_data=week_data,
            unit=unit,
        )

        return update_week_period_request
