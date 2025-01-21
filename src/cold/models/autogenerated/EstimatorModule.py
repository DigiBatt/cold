
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeterminerModule import Determiner







class Estimator(Determiner):
    """
    Class representing the `Estimator` entity, which inherits from:
    - Determiner

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4a1c73f1_b6f5_4d10_a3a6_5de90bac7cd0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Estimator'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Estimator(
    
    class_iri='https://w3id.org/emmo#EMMO_4a1c73f1_b6f5_4d10_a3a6_5de90bac7cd0',
    
    class_name='Estimator',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4a1c73f1_b6f5_4d10_a3a6_5de90bac7cd0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Estimator',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    