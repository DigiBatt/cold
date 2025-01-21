
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementUnitModule import MeasurementUnit







class DimensionlessUnit(MeasurementUnit):
    """
    Class representing the `DimensionlessUnit` entity, which inherits from:
    - MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3227b821_26a5_4c7c_9c01_5c24483e0bd0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DimensionlessUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DimensionlessUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3227b821_26a5_4c7c_9c01_5c24483e0bd0',
    
    class_name='DimensionlessUnit',
    
    hasDimensionString="example_value",
    
    qudtReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3227b821_26a5_4c7c_9c01_5c24483e0bd0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DimensionlessUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    