
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuantumModule import Quantum







class StandardModelParticle(Quantum):
    """
    Class representing the `StandardModelParticle` entity, which inherits from:
    - Quantum

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c26a0340_d619_4928_b1a1_1a04e88bb89d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardModelParticle'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandardModelParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_c26a0340_d619_4928_b1a1_1a04e88bb89d',
    
    class_name='StandardModelParticle',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c26a0340_d619_4928_b1a1_1a04e88bb89d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardModelParticle',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    