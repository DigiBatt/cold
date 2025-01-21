
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class MassLengthPerCubicTimeUnit(SIDimensionalUnit):
    """
    Class representing the `MassLengthPerCubicTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3371fb68_5f07_467c_ada6_5aa3da3808d0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MassLengthPerCubicTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MassLengthPerCubicTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3371fb68_5f07_467c_ada6_5aa3da3808d0',
    
    class_name='MassLengthPerCubicTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3371fb68_5f07_467c_ada6_5aa3da3808d0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MassLengthPerCubicTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    