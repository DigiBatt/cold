
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MechanicalTestingModule import MechanicalTesting







class ShearOrTorsionTesting(MechanicalTesting):
    """
    Class representing the `ShearOrTorsionTesting` entity, which inherits from:
    - MechanicalTesting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ShearOrTorsionTesting'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ShearOrTorsionTesting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ShearOrTorsionTesting(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#ShearOrTorsionTesting',
    
    class_name='ShearOrTorsionTesting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#ShearOrTorsionTesting',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ShearOrTorsionTesting',
        alias="class_name"
    )
    

    
    

    

    