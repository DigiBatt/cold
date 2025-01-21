
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemiosisModule import Semiosis







class Deduction(Semiosis):
    """
    Class representing the `Deduction` entity, which inherits from:
    - Semiosis

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_39a4e2a4_d835_426d_b497_182d06e1caff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Deduction'`
        - **Alias**: `class_name`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Deduction(
    
    class_iri='https://w3id.org/emmo#EMMO_39a4e2a4_d835_426d_b497_182d06e1caff',
    
    class_name='Deduction',
    
    hasSpatialPart="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_39a4e2a4_d835_426d_b497_182d06e1caff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Deduction',
        alias="class_name"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    

    
    

    

    