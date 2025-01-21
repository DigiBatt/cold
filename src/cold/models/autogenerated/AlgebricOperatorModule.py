
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalOperatorModule import MathematicalOperator







class AlgebricOperator(MathematicalOperator):
    """
    Class representing the `AlgebricOperator` entity, which inherits from:
    - MathematicalOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3c424d37_cf62_41b1_ac9d_a316f8d113d6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlgebricOperator'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlgebricOperator(
    
    class_iri='https://w3id.org/emmo#EMMO_3c424d37_cf62_41b1_ac9d_a316f8d113d6',
    
    class_name='AlgebricOperator',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3c424d37_cf62_41b1_ac9d_a316f8d113d6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlgebricOperator',
        alias="class_name"
    )
    

    
    

    

    