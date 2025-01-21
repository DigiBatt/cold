
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MagneticFieldStrengthUnit(SIDimensionalUnit):
    """
    Class representing the `MagneticFieldStrengthUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e6b83139_ba92_4fbd_a8b2_c8dde55844a1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagneticFieldStrengthUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagneticFieldStrengthUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_e6b83139_ba92_4fbd_a8b2_c8dde55844a1',
    
    class_name='MagneticFieldStrengthUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e6b83139_ba92_4fbd_a8b2_c8dde55844a1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagneticFieldStrengthUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    