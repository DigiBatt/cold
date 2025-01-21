
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectiveModule import Objective



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation





from .QuantityModule import Quantity





class MeasurementResult(Objective, SpatioTemporalTessellation):
    """
    Class representing the `MeasurementResult` entity, which inherits from:
    - Objective, SpatioTemporalTessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0f6f0120_c079_4d95_bb11_4ddee05e530e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasurementResult'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `hasQuantity` (`Optional[Quantity]`): 
        - **Default Value**: `None`
        - **Alias**: `hasQuantity`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasurementResult(
    
    class_iri='https://w3id.org/emmo#EMMO_0f6f0120_c079_4d95_bb11_4ddee05e530e',
    
    class_name='MeasurementResult',
    
    elucidation="example_value",
    
    VIMTerm="example_value",
    
    comment="example_value",
    
    hasQuantity="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0f6f0120_c079_4d95_bb11_4ddee05e530e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasurementResult',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    hasQuantity: Optional[Quantity] = Field(
        None,
        alias="hasQuantity"
    )
    

    
    @validator("hasQuantity", pre=True, always=True)
    def validate_hasQuantity(cls, value):
        if value is not None and not isinstance(value, Quantity):
            raise ValueError(f"Field 'hasQuantity' must be an instance of 'Quantity' or its subclass.")
        return value
    
    

    

    