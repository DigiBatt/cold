
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoulometryModule import Coulometry







class CoulometricTitration(Coulometry):
    """
    Class representing the `CoulometricTitration` entity, which inherits from:
    - Coulometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CoulometricTitration'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CoulometricTitration'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CoulometricTitration(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CoulometricTitration',
    
    class_name='CoulometricTitration',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CoulometricTitration',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CoulometricTitration',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    