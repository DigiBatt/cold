
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPowderModule import FormingFromPowder







class Presses(FormingFromPowder):
    """
    Class representing the `Presses` entity, which inherits from:
    - FormingFromPowder

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9d74a963_8c62_4c20_a413_93b786bfbecc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Presses'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Presses(
    
    class_iri='https://w3id.org/emmo#EMMO_9d74a963_8c62_4c20_a413_93b786bfbecc',
    
    class_name='Presses',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9d74a963_8c62_4c20_a413_93b786bfbecc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Presses',
        alias="class_name"
    )
    

    
    

    

    