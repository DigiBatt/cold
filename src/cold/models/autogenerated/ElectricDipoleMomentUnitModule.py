
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricDipoleMomentUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricDipoleMomentUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cab2be5c_4e71_4c15_8412_adb2a7f0831a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricDipoleMomentUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricDipoleMomentUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_cab2be5c_4e71_4c15_8412_adb2a7f0831a',
    
    class_name='ElectricDipoleMomentUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cab2be5c_4e71_4c15_8412_adb2a7f0831a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricDipoleMomentUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    