
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScientificTheoryModule import ScientificTheory







class NaturalLaw(ScientificTheory):
    """
    Class representing the `NaturalLaw` entity, which inherits from:
    - ScientificTheory

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_db9a009e_f097_43f5_9520_6cbc07e7610b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NaturalLaw'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NaturalLaw(
    
    class_iri='https://w3id.org/emmo#EMMO_db9a009e_f097_43f5_9520_6cbc07e7610b',
    
    class_name='NaturalLaw',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_db9a009e_f097_43f5_9520_6cbc07e7610b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NaturalLaw',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    