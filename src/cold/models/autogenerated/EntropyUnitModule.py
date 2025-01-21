
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class EntropyUnit(SIDimensionalUnit):
    """
    Class representing the `EntropyUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3ecff38b_b3cf_4a78_b49f_8580abf8715b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EntropyUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EntropyUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3ecff38b_b3cf_4a78_b49f_8580abf8715b',
    
    class_name='EntropyUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3ecff38b_b3cf_4a78_b49f_8580abf8715b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EntropyUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    