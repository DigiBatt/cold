
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalOperatorModule import MathematicalOperator







class DifferentialOperator(MathematicalOperator):
    """
    Class representing the `DifferentialOperator` entity, which inherits from:
    - MathematicalOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f8a2fe9f_458b_4771_9aba_a50e76afc52d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DifferentialOperator'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DifferentialOperator(
    
    class_iri='https://w3id.org/emmo#EMMO_f8a2fe9f_458b_4771_9aba_a50e76afc52d',
    
    class_name='DifferentialOperator',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f8a2fe9f_458b_4771_9aba_a50e76afc52d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DifferentialOperator',
        alias="class_name"
    )
    

    
    

    

    