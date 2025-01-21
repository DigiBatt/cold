
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AgentModule import Agent







class Catalyst(Agent):
    """
    Class representing the `Catalyst` entity, which inherits from:
    - Agent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8ab1e656_38ff_48e6_ab09_293d76bc9044'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Catalyst'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Catalyst(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8ab1e656_38ff_48e6_ab09_293d76bc9044',
    
    class_name='Catalyst',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8ab1e656_38ff_48e6_ab09_293d76bc9044',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Catalyst',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    