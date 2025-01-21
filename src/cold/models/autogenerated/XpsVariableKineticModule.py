
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpectroscopyModule import Spectroscopy







class XpsVariableKinetic(Spectroscopy):
    """
    Class representing the `XpsVariableKinetic` entity, which inherits from:
    - Spectroscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#XpsVariableKinetic'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'XpsVariableKinetic'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = XpsVariableKinetic(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#XpsVariableKinetic',
    
    class_name='XpsVariableKinetic',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#XpsVariableKinetic',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'XpsVariableKinetic',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    