
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicConstructModule import SymbolicConstruct



from .MeasurementUnitModule import MeasurementUnit



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation





from .MetricPrefixModule import MetricPrefix



from .UnitSymbolModule import UnitSymbol





class PrefixedUnit(SymbolicConstruct, MeasurementUnit, SpatioTemporalTessellation):
    """
    Class representing the `PrefixedUnit` entity, which inherits from:
    - SymbolicConstruct, MeasurementUnit, SpatioTemporalTessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c6d4a5e0_7e95_44df_a6db_84ee0a8bbc8e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PrefixedUnit'`
        - **Alias**: `class_name`
    
    - `hasMetricPrefix` (`Optional[MetricPrefix]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMetricPrefix`
    
    - `hasUnitSymbol` (`Optional[UnitSymbol]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PrefixedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_c6d4a5e0_7e95_44df_a6db_84ee0a8bbc8e',
    
    class_name='PrefixedUnit',
    
    hasMetricPrefix="example_value",
    
    hasUnitSymbol="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c6d4a5e0_7e95_44df_a6db_84ee0a8bbc8e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PrefixedUnit',
        alias="class_name"
    )
    
    hasMetricPrefix: Optional[MetricPrefix] = Field(
        None,
        alias="hasMetricPrefix"
    )
    
    hasUnitSymbol: Optional[UnitSymbol] = Field(
        None,
        alias="hasUnitSymbol"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasMetricPrefix", pre=True, always=True)
    def validate_hasMetricPrefix(cls, value):
        if value is not None and not isinstance(value, MetricPrefix):
            raise ValueError(f"Field 'hasMetricPrefix' must be an instance of 'MetricPrefix' or its subclass.")
        return value
    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, UnitSymbol):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'UnitSymbol' or its subclass.")
        return value
    
    

    

    