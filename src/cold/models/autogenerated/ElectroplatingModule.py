
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatingManufacturingModule import CoatingManufacturing







class Electroplating(CoatingManufacturing):
    """
    Class representing the `Electroplating` entity, which inherits from:
    - CoatingManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_30e3edb5_0977_4b9b_9aed_5a4d16c1c07c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electroplating'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electroplating(
    
    class_iri='https://w3id.org/emmo#EMMO_30e3edb5_0977_4b9b_9aed_5a4d16c1c07c',
    
    class_name='Electroplating',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_30e3edb5_0977_4b9b_9aed_5a4d16c1c07c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electroplating',
        alias="class_name"
    )
    

    
    

    

    