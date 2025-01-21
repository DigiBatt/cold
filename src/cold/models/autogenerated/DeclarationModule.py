
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemiosisModule import Semiosis







class Declaration(Semiosis):
    """
    Class representing the `Declaration` entity, which inherits from:
    - Semiosis

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_47bf3513_4ae6_4858_9c45_76e23230d68d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Declaration'`
        - **Alias**: `class_name`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Declaration(
    
    class_iri='https://w3id.org/emmo#EMMO_47bf3513_4ae6_4858_9c45_76e23230d68d',
    
    class_name='Declaration',
    
    hasSpatialPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_47bf3513_4ae6_4858_9c45_76e23230d68d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Declaration',
        alias="class_name"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    

    
    

    

    