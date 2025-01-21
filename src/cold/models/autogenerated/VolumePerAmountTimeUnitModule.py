
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class VolumePerAmountTimeUnit(SIDimensionalUnit):
    """
    Class representing the `VolumePerAmountTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bc73913a_3bb6_4205_8d36_79bc72ca9891'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VolumePerAmountTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VolumePerAmountTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_bc73913a_3bb6_4205_8d36_79bc72ca9891',
    
    class_name='VolumePerAmountTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bc73913a_3bb6_4205_8d36_79bc72ca9891',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VolumePerAmountTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    