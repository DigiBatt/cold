
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class RichardsonConstantUnit(SIDimensionalUnit):
    """
    Class representing the `RichardsonConstantUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_754c3a5d_8ae8_41ff_b5f2_acbadb53c735'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RichardsonConstantUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RichardsonConstantUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_754c3a5d_8ae8_41ff_b5f2_acbadb53c735',
    
    class_name='RichardsonConstantUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_754c3a5d_8ae8_41ff_b5f2_acbadb53c735',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RichardsonConstantUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    