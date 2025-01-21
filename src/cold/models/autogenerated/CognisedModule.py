
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticObjectModule import SemioticObject







class Cognised(SemioticObject):
    """
    Class representing the `Cognised` entity, which inherits from:
    - SemioticObject

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_881606d0_6f2f_4947_bc8b_75c5b7b2b688'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cognised'`
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
    obj = Cognised(
    
    class_iri='https://w3id.org/emmo#EMMO_881606d0_6f2f_4947_bc8b_75c5b7b2b688',
    
    class_name='Cognised',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_881606d0_6f2f_4947_bc8b_75c5b7b2b688',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cognised',
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
    

    
    

    

    