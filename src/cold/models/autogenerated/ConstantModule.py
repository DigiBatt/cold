
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumericalVariableModule import NumericalVariable







class Constant(NumericalVariable):
    """
    Class representing the `Constant` entity, which inherits from:
    - NumericalVariable

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8c64fcfa_23aa_45f8_9e58_bdfd065fab8f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Constant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Constant(
    
    class_iri='https://w3id.org/emmo#EMMO_8c64fcfa_23aa_45f8_9e58_bdfd065fab8f',
    
    class_name='Constant',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8c64fcfa_23aa_45f8_9e58_bdfd065fab8f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Constant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    