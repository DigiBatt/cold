
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class LengthTimeCurrentUnit(SIDimensionalUnit):
    """
    Class representing the `LengthTimeCurrentUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8515e948_bc2f_423b_8025_e4830f2b21dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LengthTimeCurrentUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LengthTimeCurrentUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_8515e948_bc2f_423b_8025_e4830f2b21dd',
    
    class_name='LengthTimeCurrentUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8515e948_bc2f_423b_8025_e4830f2b21dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LengthTimeCurrentUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    