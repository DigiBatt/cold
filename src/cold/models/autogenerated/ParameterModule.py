
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumericalVariableModule import NumericalVariable







class Parameter(NumericalVariable):
    """
    Class representing the `Parameter` entity, which inherits from:
    - NumericalVariable

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d1d436e7_72fc_49cd_863b_7bfb4ba5276a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Parameter'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Parameter(
    
    class_iri='https://w3id.org/emmo#EMMO_d1d436e7_72fc_49cd_863b_7bfb4ba5276a',
    
    class_name='Parameter',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d1d436e7_72fc_49cd_863b_7bfb4ba5276a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Parameter',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    