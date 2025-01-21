
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IonModule import Ion







class Anion(Ion):
    """
    Class representing the `Anion` entity, which inherits from:
    - Ion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_5a5e8609_83bf_46d1_a1b0_eaafa27aaed4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Anion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Anion(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_5a5e8609_83bf_46d1_a1b0_eaafa27aaed4',
    
    class_name='Anion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_5a5e8609_83bf_46d1_a1b0_eaafa27aaed4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Anion',
        alias="class_name"
    )
    

    
    

    

    