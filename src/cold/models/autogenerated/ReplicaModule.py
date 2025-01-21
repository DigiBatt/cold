
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ResemblanceIconModule import ResemblanceIcon



from .FunctionalIconModule import FunctionalIcon



from .IconModule import Icon







class Replica(ResemblanceIcon, FunctionalIcon, Icon):
    """
    Class representing the `Replica` entity, which inherits from:
    - ResemblanceIcon, FunctionalIcon, Icon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8533871a_01e4_4935_8c7b_cedf8fcc3fa3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Replica'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Replica(
    
    class_iri='https://w3id.org/emmo#EMMO_8533871a_01e4_4935_8c7b_cedf8fcc3fa3',
    
    class_name='Replica',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8533871a_01e4_4935_8c7b_cedf8fcc3fa3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Replica',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    