
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class QuarticLengthPerTimeUnit(SIDimensionalUnit):
    """
    Class representing the `QuarticLengthPerTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6cfc5b82_b47b_47bc_bb45_c23c273d2e06'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'QuarticLengthPerTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = QuarticLengthPerTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_6cfc5b82_b47b_47bc_bb45_c23c273d2e06',
    
    class_name='QuarticLengthPerTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6cfc5b82_b47b_47bc_bb45_c23c273d2e06',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'QuarticLengthPerTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    