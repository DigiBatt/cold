
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineElectrolyteModule import AlkalineElectrolyte







class AmmoniaSolution(AlkalineElectrolyte):
    """
    Class representing the `AmmoniaSolution` entity, which inherits from:
    - AlkalineElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f9e2e676_5cd1_4e22_a776_af45838d4027'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmmoniaSolution'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmmoniaSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f9e2e676_5cd1_4e22_a776_af45838d4027',
    
    class_name='AmmoniaSolution',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f9e2e676_5cd1_4e22_a776_af45838d4027',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmmoniaSolution',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    