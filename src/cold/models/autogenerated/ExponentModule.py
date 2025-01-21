
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlgebricOperatorModule import AlgebricOperator







class Exponent(AlgebricOperator):
    """
    Class representing the `Exponent` entity, which inherits from:
    - AlgebricOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_223d9523_4169_4ecd_b8af_acad1215e1ff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Exponent'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Exponent(
    
    class_iri='https://w3id.org/emmo#EMMO_223d9523_4169_4ecd_b8af_acad1215e1ff',
    
    class_name='Exponent',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_223d9523_4169_4ecd_b8af_acad1215e1ff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Exponent',
        alias="class_name"
    )
    

    
    

    

    