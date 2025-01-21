
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeclarationModule import Declaration







class Determination(Declaration):
    """
    Class representing the `Determination` entity, which inherits from:
    - Declaration

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_10a5fd39_06aa_4648_9e70_f962a9cb2069'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Determination'`
        - **Alias**: `class_name`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Determination(
    
    class_iri='https://w3id.org/emmo#EMMO_10a5fd39_06aa_4648_9e70_f962a9cb2069',
    
    class_name='Determination',
    
    hasSpatialPart="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_10a5fd39_06aa_4648_9e70_f962a9cb2069',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Determination',
        alias="class_name"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    