
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TomographyModule import Tomography







class AtomProbeTomography(Tomography):
    """
    Class representing the `AtomProbeTomography` entity, which inherits from:
    - Tomography

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AtomProbeTomography'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AtomProbeTomography'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AtomProbeTomography(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#AtomProbeTomography',
    
    class_name='AtomProbeTomography',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AtomProbeTomography',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AtomProbeTomography',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    