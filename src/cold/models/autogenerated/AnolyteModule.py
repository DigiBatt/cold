
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LiquidElectrolyteModule import LiquidElectrolyte







class Anolyte(LiquidElectrolyte):
    """
    Class representing the `Anolyte` entity, which inherits from:
    - LiquidElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_865a40fc_2187_4549_a7e1_37aa2458448f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Anolyte'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Anolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_865a40fc_2187_4549_a7e1_37aa2458448f',
    
    class_name='Anolyte',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_865a40fc_2187_4549_a7e1_37aa2458448f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Anolyte',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    