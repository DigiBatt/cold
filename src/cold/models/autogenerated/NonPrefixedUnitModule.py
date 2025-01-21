
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementUnitModule import MeasurementUnit







class NonPrefixedUnit(MeasurementUnit):
    """
    Class representing the `NonPrefixedUnit` entity, which inherits from:
    - MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_868ae137_4d25_493e_b270_21ea3d94849e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NonPrefixedUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NonPrefixedUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_868ae137_4d25_493e_b270_21ea3d94849e',
    
    class_name='NonPrefixedUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_868ae137_4d25_493e_b270_21ea3d94849e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NonPrefixedUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    