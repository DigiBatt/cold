
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemiosisModule import Semiosis







class Cognition(Semiosis):
    """
    Class representing the `Cognition` entity, which inherits from:
    - Semiosis

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7cdc375d_d371_4d78_acd5_d51732f52126'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cognition'`
        - **Alias**: `class_name`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Cognition(
    
    class_iri='https://w3id.org/emmo#EMMO_7cdc375d_d371_4d78_acd5_d51732f52126',
    
    class_name='Cognition',
    
    hasSpatialPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7cdc375d_d371_4d78_acd5_d51732f52126',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cognition',
        alias="class_name"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    

    
    

    

    