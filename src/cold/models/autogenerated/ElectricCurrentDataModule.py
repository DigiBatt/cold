
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VectorModule import Vector



from .RawDataModule import RawData





from .QuantityModule import Quantity





class ElectricCurrentData(Vector, RawData):
    """
    Class representing the `ElectricCurrentData` entity, which inherits from:
    - Vector, RawData

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4920de95_3a48_4669_b762_5a0b5232b52f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentData'`
        - **Alias**: `class_name`
    
    - `hasQuantity` (`Optional[Quantity]`): 
        - **Default Value**: `None`
        - **Alias**: `hasQuantity`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4920de95_3a48_4669_b762_5a0b5232b52f',
    
    class_name='ElectricCurrentData',
    
    hasQuantity="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4920de95_3a48_4669_b762_5a0b5232b52f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentData',
        alias="class_name"
    )
    
    hasQuantity: Optional[Quantity] = Field(
        None,
        alias="hasQuantity"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasQuantity", pre=True, always=True)
    def validate_hasQuantity(cls, value):
        if value is not None and not isinstance(value, Quantity):
            raise ValueError(f"Field 'hasQuantity' must be an instance of 'Quantity' or its subclass.")
        return value
    
    

    

    