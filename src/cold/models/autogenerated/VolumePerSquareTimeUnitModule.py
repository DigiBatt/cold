
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class VolumePerSquareTimeUnit(SIDimensionalUnit):
    """
    Class representing the `VolumePerSquareTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_87deb5a8_7a85_49c3_97b2_e62c8484aa1a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VolumePerSquareTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VolumePerSquareTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_87deb5a8_7a85_49c3_97b2_e62c8484aa1a',
    
    class_name='VolumePerSquareTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_87deb5a8_7a85_49c3_97b2_e62c8484aa1a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VolumePerSquareTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    