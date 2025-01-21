
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricDisplacementFieldUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricDisplacementFieldUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6d753e0c_a967_4de4_ad22_c2fecb3913be'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricDisplacementFieldUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricDisplacementFieldUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_6d753e0c_a967_4de4_ad22_c2fecb3913be',
    
    class_name='ElectricDisplacementFieldUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6d753e0c_a967_4de4_ad22_c2fecb3913be',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricDisplacementFieldUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    