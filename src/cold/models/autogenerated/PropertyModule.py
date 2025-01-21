
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CodedModule import Coded





from ..custom.NumericalPartModule import NumericalPart



from .MeasurementUnitModule import MeasurementUnit





class Property(Coded):
    """
    Class representing the `Property` entity, which inherits from:
    - Coded

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b7bcff25_ffc3_474e_9ab5_01b1664bd4ba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Property'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `hasNumericalPart` (`Optional[NumericalPart]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNumericalPart`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Property(
    
    class_iri='https://w3id.org/emmo#EMMO_b7bcff25_ffc3_474e_9ab5_01b1664bd4ba',
    
    class_name='Property',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    hasNumericalPart=None,
    
    hasMeasurementUnit=None,
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b7bcff25_ffc3_474e_9ab5_01b1664bd4ba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Property',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    hasNumericalPart: Optional[NumericalPart] = Field(
        None,
        alias="hasNumericalPart"
    )
    
    hasMeasurementUnit: Optional[MeasurementUnit] = Field(
        None,
        alias="hasMeasurementUnit"
    )
    

    
    @validator("hasNumericalPart", pre=True, always=True)
    def validate_hasNumericalPart(cls, value):
        if value is not None and not isinstance(value, NumericalPart):
            raise ValueError(f"Field 'hasNumericalPart' must be an instance of 'NumericalPart' or its subclass.")
        return value
    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    
    
    
    def __init__(self, value: float, unit: str, **kwargs):
        """Override __init__ for simplified instantiation.""" 
        # Dynamically create a MeasurementUnit instance 
        unit_instance = MeasurementUnit.from_class_name(unit) 
        super().__init__(
            hasNumericalPart=NumericalPart(hasNumericalValue=value),
            hasMeasurementUnit=unit_instance,
            **kwargs,
        )

    
    

    