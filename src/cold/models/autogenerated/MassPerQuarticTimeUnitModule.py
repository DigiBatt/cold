
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MassPerQuarticTimeUnit(SIDimensionalUnit):
    """
    Class representing the `MassPerQuarticTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_30261696_a8a4_44ce_9bf5_b18201a83c76'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassPerQuarticTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassPerQuarticTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_30261696_a8a4_44ce_9bf5_b18201a83c76',
    
    class_name='MassPerQuarticTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_30261696_a8a4_44ce_9bf5_b18201a83c76',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassPerQuarticTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    