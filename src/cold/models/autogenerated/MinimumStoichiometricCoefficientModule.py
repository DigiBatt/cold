
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoichiometricCoefficientModule import StoichiometricCoefficient







class MinimumStoichiometricCoefficient(StoichiometricCoefficient):
    """
    Class representing the `MinimumStoichiometricCoefficient` entity, which inherits from:
    - StoichiometricCoefficient

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_86324806_4263_4d80_b5af_1a7be844ab5b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MinimumStoichiometricCoefficient'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MinimumStoichiometricCoefficient(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_86324806_4263_4d80_b5af_1a7be844ab5b',
    
    class_name='MinimumStoichiometricCoefficient',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_86324806_4263_4d80_b5af_1a7be844ab5b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MinimumStoichiometricCoefficient',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    